
# 4.2 La Bóveda

El componente de La Bóveda constituye el núcleo de la plataforma, ya que es el responsable del almacenamiento y gestión de todos los datasets. Este módulo permite alojar datasets con distintos niveles de acceso y monetización, incluyendo opciones de descarga gratuita, pago único, suscripciones por cuotas, y configuraciones de visibilidad pública o privada.

Uno de los aspectos más críticos de La Bóveda es la seguridad. Solo los usuarios que hayan adquirido un dataset o que hayan sido aprobados explícitamente pueden acceder a su contenido. El nivel de resguardo es tan alto que ni siquiera los administradores del sistema tienen acceso directo a los datos almacenados, garantizando así una separación estricta de responsabilidades y máxima confidencialidad.

Adicionalmente, este componente debe ser altamente resiliente y escalable, ya que se espera una carga intensiva tanto en volumen de datos como en frecuencia de acceso. La infraestructura debe soportar cargas en batch de datos, así como consultas analíticas complejas, sin comprometer la integridad ni el rendimiento del sistema.

Por estas razones, en esta sección se detalla el diseño de La Bóveda con énfasis en los aspectos de seguridad, escalabilidad, resiliencia y eficiencia, pilares fundamentales para asegurar su correcto funcionamiento dentro del ecosistema de la plataforma.

En cuanto a como se planean guardar los datasets a continuacióń se muestra un diagrama con la vista a alto nivel:

![image](../img/BovedaAltoNivel.png)

En la imagen se puede ver cómo se debe tener un almacenamiento central, el cual debe estar dividido lógicamente para los colectivos. Ya después cada colectivo tendrá sus datasets guardados junto con sus tablas, que en ocasiones pueden ser usadas en datasets distintos. Más adelante se verá cómo es que este enfoque será logrado.

## Diseño del Backend

El backend de este componente es más simple, ya que la mayor parte del peso cae en la estructura de la base de datos y su modelo de seguridad. En esta sección solo se comentarán dos funcionalidades: la funcionalidad de trazabilidad y cómo el API interactúa con Redshift.

**Trazabilidad:**

En este componente es sumamente importante que se tenga trazabilidad de quién ejecuta qué tarea. Por lo que, al hacer un query a Redshift, siempre se adjuntará como variable de sesión el ID de Cognito de la persona que pidió el query.

Luego, gracias a la funcionalidad de Amazon Redshift logs, se podrá ver detalladamente la información del query de la siguiente forma:

| Nombre de columna | Descripción                                         |
| ----------------- | --------------------------------------------------- |
| recordtime        | Hora en la que ocurrió el evento.                   |
| db                | Nombre de la base de datos.                         |
| user              | Nombre de usuario.                                  |
| pid               | ID del proceso asociado con la sentencia.           |
| userid            | ID del usuario.                                     |
| xid               | ID de la transacción.                               |
| query             | Un prefijo `LOG:` seguido del texto de la consulta. |

Ahora bien, estos logs sirven tanto para tener un registro de qué consultas se han hecho (para más adelante dar contexto Agentes sobre como consultar un dataset), como para llevar cuotas de uso de datasets que se usan por cuotas definidas.

Por ello, cuando estos logs lleguen a AWS CloudWatch, se disparará una Lambda Function que se encargue de obtener el query y también el ID del usuario que se seteó en la consulta. Luego, se revisará si el dataset al que se le realizó la consulta es de tipo cuota, y en dado caso se va a la tabla de cuota en RDS para hacer la deducción.

Para el resto de los casos (incluyendo cuando el dataset es de tipo cuota), se insertará el query en un índice de OpenSearch, el servicio gestionado de Elasticsearch que ofrece AWS. Gracias a la naturaleza de time series de Elastic Search, podremos almacenar estos logs de manera eficiente, organizándolos en índices mensuales por dataset con el formato de nombre `DATASETNAME-YYYY-MM`.
Esto evitará almacenamiento masivo y poco escalable típico de motores SQL, y además funcionará como una fuente sencilla para que los agentes de IA puedan alimentarse con los queries asociados a cada dataset.

A continuación un ejemplo de código de como se puede realizar dicha lambda function:

```python
import json
import re
import base64
import gzip
from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+psycopg2://usuario:password@host:puerto/dbname"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Cuotas(Base):
    __tablename__ = "Cuotas"
    Id = Column(Integer, primary_key=True)
    IdDataset = Column(Integer, ForeignKey("Dataset.Id"), nullable=False)
    CuotasRestantes = Column(Integer, nullable=False)

def lambda_handler(event, context):
    mensaje = event['awslogs']['data']

    #Es un zip, entonces viene por json en base64, por lo que se decodifica y luego extrae el contenido
    compressed_payload = base64.b64decode(mensaje)
    uncompressed_payload = gzip.decompress(compressed_payload)
    payload_json = json.loads(uncompressed_payload)

    session = Session()
    try:
        for log_event in payload_json["logEvents"]:
            message_text = log_event["message"]

            #Se busca datasetId en la query con regex
            match = re.search(r'/\*dataset:(\d+)\*/', message_text)
            if not match:
                continue
            dataset_id = int(match.group(1))

            ######
            # Aquí se revisa RDS para saber si es un dataset de pago por cuotas, y luego se hace
            # la inserción en el índice correspondiente de Opensearch
            ######

            cuota = session.query(Cuotas).filter(Cuotas.IdDataset == dataset_id).first()
            if cuota and cuota.CuotasRestantes > 0:
                cuota.CuotasRestantes -= 1
                session.commit()
                print(f"Cuotas restantes para dataset {dataset_id}: {cuota.CuotasRestantes}")
            else:
                print(f"No hay cuotas restantes o dataset {dataset_id} no encontrado")
    except Exception as e:
        session.rollback()
        print(f"Error procesando logs: {e}")
    finally:
        session.close()
```

**Interacción con API:**

Más adelante se verá cómo se implementa el RBAC en el sistema, pero el API también proveerá un tipo de RBAC por lógica. Se hará de la siguiente forma:

1. Llega consulta desde el frontend

```json
{
  "jwt": "el token de sesión del usuario",
  "dataset": "nombre del dataset"
}
```

- Con el JWT se obtiene el ID de Cognito de la persona.

2. Proceso de autorización

- Primero se revisa que el usuario sea parte del colectivo propietario del dataset:

  - En caso de que sí, entonces se le asigna el IAM Role correspondiente al colectivo y se pasa el query a la creación de queries.

- Ahora bien, si el usuario no es propietario, entonces se revisa la tabla de AccesoDataset para ver si tiene acceso al dataset.

  - Si no, entonces se rechaza la solicitud.

- Ahora bien, si no se rechaza, entonces se revisa si el dataset es por cuotas en la tabla de DatasetDePago; en caso de que sí, se revisan las cuotas restantes en la tabla de Cuotas.

  - Si no quedan, entonces se rechaza la conexión.

- Ya luego, si se pasó todo el proceso de autorización, se le asigna el rol de IAM correspondiente al dataset por medio de un STS que sirva solo para esa consulta.

### Servicios en AWS

Se mencionarán solo los servicios de AWS que aún no han sido descritos en algún punto de la arquitectura. En caso de querer ver todos los servicios de AWS que se usarán y como se desplegarán por medio de terraform ir a dicha sección después de la explicación de los microservicios.

**AWS Lambda:**
Para las funciones serverless que obtienen información de los datasets y la loguean.

**Configuración de Hardware:** Aunque no gestionamos hardware directamente, sí configuraremos los recursos, como:

- **Memoria:** 1024 MB
- **Arquitectura:** arm64
- **Tiempo de ejecución:** Node.js 22.x
- **Almacenamiento efímero:** 512MB
- **Tiempo de espera:** 5s
- **Retry attempts:** 1

**AWS OpenSearch:**

Para el sistema de logs para posterior entrenamiento de Agentes de IA.

**Configuración del Dominio OpenSearch:**

- **Versión del motor**: OpenSearch 2.3
- **Tipo de instancia**: t3.small.search
- **Cantidad de instancias**: 2 (con zone awareness activado para alta disponibilidad)
- **Almacenamiento EBS**: 20 GB, tipo gp3
- **Encriptación**:
  - En tránsito (TLS 1.2 mínimo)
  - En reposo (AES-256)
- **Seguridad**:
  - Autenticación interna con usuario admin
  - Acceso vía HTTPS obligatorio
  - Index Lifecycle Management (ILM):
- **Política de rollover**:
  - Máximo 5GB por índice
  - Máximo 1 día por índice
- **Retención**:
  - Borrado automático de índices después de 30 días

## Diseño de los Datos

### Topología de Datos

- **Tipo:** OLAP + OLTP

  - Para La Bóveda se empleará un enfoque híbrido, utilizando una base de datos OLAP para el almacenamiento de los distintos datasets y una base de datos OLTP para toda la parte administrativa relacionada con personas, colectivos, cuotas y gestión de acceso a los datasets.
  - En cuanto al OLTP, como se describió previamente en la sección del Bioregistro, se utilizará una base de datos en RDS con PostgreSQL para almacenar la información de usuarios y colectivos. En esta sección se utilizará la misma base de datos, pero se agregarán nuevas tablas para registrar accesos a datasets, gestionar los registros de datasets y asociar tablas a los distintos datasets. Estas nuevas tablas serán detalladas más adelante en el diagrama correspondiente.
  - Para el almacenamiento OLAP se utilizará Amazon Redshift, un OLAP orientado a columnas, diseñado específicamente para manejar grandes volúmenes de datos y consultas complejas a escala. Se optará por la versión Redshift Serverless, que permite el uso bajo demanda sin necesidad de configurar nodos, escalando automáticamente según la carga de trabajo. Esta versión también replica automáticamente los datos en tres zonas dentro del mismo Availability Zone y ofrece failover automático mediante snapshots. Además, se configurarán respaldos automáticos incrementales los martes y viernes a la 1 a.m.
  - Se aprovecharán dos funcionalidades clave de Redshift: las Federated Queries, que permitirán consultar directamente las tablas administrativas almacenadas en RDS; y el almacenamiento interno de Redshift, que ofrece un modelo columnar altamente eficiente para los datos analíticos.
  - Cabe aclarar que no se detallarán las especificaciones técnicas para RDS ya que fueron mencionadas previamente en el Bioregistro.

- **Tecnología Cloud**:

  - RDS para PostgreSQL.
  - Amazon Redshift.

- **Polítcias y Reglas**:

  - Single-region: Solo se usará una región para RDS y Redshift, us-east-1
  - Backups automáticos: Tanto RDS como Redshift harán backups automáticos a las 1 de la mañana y lo subirán a un S3.
  - Backups cruzados: Para proteger los respaldos en caso de que la región de aws caiga (poco probable), se cargaran adicionalmente en un S3 Bucket en us-west-1. Esto se hará cada semana los viernes a las 2 de la mañana, ya que su prioridad es menor.
  - Failover Automático: Redshift tiene nativamente integrado la opción de hace failover. Con RDS se logrará por medio del uso de Multi-AZ.

- **Beneficios**:
  - Usar RDS con PostgreSQL y Redshift dentro de la misma región reduce la latencia entre los servicios y simplifica la arquitectura, lo que también ayuda a controlar costos.
  - PostgreSQL es una base de datos open source, por lo que no se incurre en costos adicionales por licencias.
  - Amazon Redshift está optimizado para cargas masivas y consultas analíticas complejas, con escalabilidad automática en su versión serverless, lo que mejora el rendimiento sin necesidad de gestionar infraestructura.
  - Tanto RDS como Redshift están plenamente integrados en el ecosistema AWS, facilitando la gestión de seguridad, monitoreo y respaldo con servicios nativos.
  - AWS garantiza altos niveles de disponibilidad y cumplimiento de SLA para ambos servicios, lo que aporta estabilidad y confiabilidad a la plataforma.
  - Redshift tiene integración nativa con servicios como AWS Glue.
  - Redshift puede adherirse a RDS para interactuar con el facilmente:
    ```sql
    CREATE EXTERNAL SCHEMA rds_schema
    FROM POSTGRES
    DATABASE 'admin_db'
    URI 'my-db-instance.abc123xyz.us-east-1.rds.amazonaws.com'
    PORT 5432
    IAM_ROLE 'arn:aws:iam::cuenta-dpv:role/admin-dpv'
    SECRET_ARN 'arn:aws:secretsmanager:us-east-1:123456789012:secret:MySecret'
    ```
  - Redshift permite copiar en Batch archivos de Parquet desde un S3 y mapearlos a tablas en su almacenamiento interno:
    ```sql
      COPY esquema.tabla_destino
      FROM 's3://tu-bucket/ruta/a/parquets/'
      IAM_ROLE 'arn:aws:iam::cuenta-dpv:role/admin-dpv'
      FORMAT AS PARQUET;
    ```

### RLS

No se usará RLS ya que el acceso a datasets se hace por tablas, entonces una vez un usuario tenga acceso a un dataset, podrá ver todo el contenido que este tenga; no habrán filas a las que esté restringido. Nuestro diseño es seguro porque en una misma tabla solo se guarda información correspondiente a un solo colectivo. Puede ser que esa tabla se comparta entre datasets del colectivo, pero igual no pasa nada, dado que el acceso sigue siendo por tabla. En la siguiente sección se dirá cómo se gestiona el acceso por tabla.

### Tenency, Seguridad y Privacidad

- **Modelo**: Singe-Access-Point, RBAC, Multi-Tenant

  - El Single-Acess-Point será obligatorio, ya que solo las clases de RDSRepository y RedshiftRepository podrán interactuar con los sistemas de bases de datos.
  - Se usará la opción de Multi-Tenant que ofrece Redshift, para de ese modo asignar un Schema distinto para que cada colectivo guarde sus datasets.
  - Para hacer el manejo de RBAC se usarán LakeFormation, IAM de AWS, y el API (Especificado en el Backend).
  - Para implementar el Lakeformation y IAM se usarán 2 tipos de roles generales que luego serán divididos según corresponda:
    - Rol IAM de Colectivo: Siempre que se crea un nuevo dataset se crean tags de LakeFormation para que den permiso de acceso a las tablas de dicho dataset, Luego esas tags se asignan al rol IAM. Lo tendrán los admin del colectivo y sus representantes.
    - Rol de Dataset: Se creará un rol de IAM específico para cada dataset. Se crearan las tags del mismo modo que con el rol anterior, solo que en este caso el Rol de IAM será especifico al acceso a las tablas del dataset. De esta manera cuando una persona acceda a un dataset solo podrá si previamente se le asigno este rol.
  - Cuando se vayan a ejecutar las consultas en Redshfit, se agregará como variable de sesión a la consulta el Id del usuario en Cognito.
  - Cabe aclarar que hay un Rol de IAM por defecto asociado al tag de lakeformation "dataset=public-free", esto permite que cualquier usuario pueda ver un Dataset. Será asignado a los datasets que son gratis y públicos.

- **Ejemplos**

  - A continuación como es que se crean las tags con LakeFormation para acceder a tablas en Redshift:

    ```python
    import boto3

    client = boto3.client('lakeformation')

    # Se crea el nombre y key del tag
    client.create_lf_tag(
        TagKey='dataset',
        TagValues=['Colectivo1234']
    )

    #Se le asignan recursos de redshift
    client.assign_lf_tags_to_resource(
        Resource={
            'Table': {
                'CatalogId': 'AWS_ACCOUNT_ID',
                'DatabaseName': 'datalake',
                'Name': 'Tabla1'
            }
        },
        LFTags=[
            {
                'TagKey': 'dataset',
                'TagValues': ['Colectivo1234']
            }
        ]
    )
    ```

  - Ya en la sección de registration-service del bioregistro se específico como crear un rol de IAM, ahora a continuación se muestra como asignarle tags de LakeFormation:
    ```python
    client.grant_permissions(
        Principal={ # A que rol de IAM se asigna
            'DataLakePrincipalIdentifier': 'arn:aws:iam::YOUR_ACCOUNT_ID:group/DPV_DataAccess_Empresas2024'
        },
        Resource={ # Que tags de Lakeformation se le asiginan
            'LFTagPolicy': {
                'ResourceType': 'TABLE',
                'Expression': [
                    {
                        'TagKey': 'dataset',
                        'TagValues': ['empresas2024']
                    }
                ],
                'ResourceType': 'TABLE'
            }
        },
        Permissions=['SELECT', 'DESCRIBE'], #que pueden realizar sobre los datos
        PermissionsWithGrantOption=[]
    )
    ```
  - Ahora bien, un ejemplo de como se puede adjuntar como elemento de la Sesión el ID de cognito:

    ```python
    from sqlalchemy import create_engine, text

    #Crear el engine con los parámetros de Redshift
    engine = create_engine("postgresql+psycopg2://usuario:contraseña@host:puerto/base_de_datos")

    cognito_id = 'abc-123-cognito-sub-id'

    with engine.connect() as conn:
        conn.executeu(text("SET session.cognito_user_id = :cognito_id"), {"cognito_id": cognito_id})

        result = conn.execute(text("SELECT * FROM public.algo LIMIT 10;"))
        for row in result:
            print(row)
    ```

- **Encripción**:

  - Toda la información estará encriptada gracias al Encryption at Rest

- **Cloud**:

  - Amazon RDS para PostgreSQL con RLS.
  - LakeFormation, para manejar los permisos modulares a tablas
  - AWS IAM, para dar permisos específicos asociados con políticas de LakeFormation
  - Encryption at rest en Redshift gracias a AWS KMS
  - Encryption at rest en RDS gracias a AWS KMS

- **Beneficios**:
  - Gracias a que solo abrá un single point of acces, la intrusión de un tercero a la base de datos de usuarios es muy poco probable.
  - Gracias a que en la sesión de la consulta se adjunta el Id del usuario en Cognito, se tiene trazabilidad de quien ejecute que consulta.
  - Tener multi-tenant agrega una capa de separación lógica que evita que entre colectivos puedan acceder a espacios que no les corresponde.
  - En caso de que alguién tenga acceso a la base de datos no podrá hacer nada ya que todo está encriptado.
  - Ya que para poder acceder a una tabla se ocupa tener el rol efímero de IAM que a su vez tenga los tags necesarios de LakeFormation, inclusive los administradores de la base de datos no van a poder ver que contenido tienen las tablas. Solo aquellos con los permisos podrán.
  - Gracias a que Redshfit internamente es una base de datos columnar las consultas pueden ser realizadas de manera más eficiente ya que solo trae a memoria la información necesario y no todos los datos de un registro.

### Conexión a Base de datos

- **Modelo**: Transaccional vía Statements / Store Procedures y ORM

Usaremos SQLAlchemy como ORM para interactuar con PostgreSQL y Redshift dentro de la aplicación. Además se usarán Store Procedures para operaciones más complejas como las consultas a datasets desde el módulo de Centro de visualización y Consumo.

- **Patrones de POO**:

  - Factory: Usamos el patrón Factory para la creación de las clases RDSFactory, RDSRepository, RedshiftFactory,RedshiftRepository.

- **Beneficios**:

  - El código es independiente del motor de base de datos relacional, lo que permite cambiarlo fácilmente si es necesario. Se puede usar el mismo tanto para RDS como Redshift.
  - El desarrollo es más ágil que escribir SQL puro.
  - Se protege contra vulnerabilidades como SQL Injection.
  - Se puede garantizar el cumplimiento de las propiedades ACID.

- **Pool de Conexiones**
  Usaremos el pool integrado en SQLAlchemy (QueuePool), el cual es dinámico. El tamaño base del pool será de 10 conexiones, y podrá escalar hasta 15 conexiones simultáneas.

  - **Beneficios**:
    - La escalabilidad se ajusta bajo demanda.
    - Proporciona mayor estabilidad en ambientes productivos.

- **Drivers**
  Para PostgreSQL y Redshift utilizaremos el driver nativo psycopg2, integrado con SQLAlchemy, lo cual ofrece mejor rendimiento.

  - **Beneficios**:
    - Para PostgreSQL un driver nativo rápido, se aprovecha lo mejor.

### Diseño para IA

**Implementaciones comunes a todas las tablas**

Dado que es imposible predecir con exactitud el contenido específico de cada dataset, se aplicarán ciertas implementaciones transversales a todas las tablas de Redshift para facilitar su interpretación por parte de agentes de AI:

- Cada registro deberá incluir una columna llamada **CategoriaSemantica**, que permitirá dar contexto sobre el tipo de información contenida en la tabla.
- Se añadirá también una columna de **Descripción**, destinada a ofrecer una breve explicación sobre el contenido de cada fila, brindando aún más contexto semántico.
- Estas columnas serán incorporadas automáticamente durante el proceso del motor de transformación.
- Se registrarán todos los logs hechos a Opensearch, donde los módelos de inteligencia artificial podrán ver que consultas se le hacen a un dataset específico, y de esta forma puedan dar resultados de mayor calidad.

**Justificación**

La orientación de **La Bóveda** hacia un diseño habilitado a agentes de AI responde a las siguientes necesidades:

- Las consultas provenientes del centro de visualización y consumo podrán realizarse mediante lenguaje natural. Para que los agentes puedan generar consultas SQL adecuadas, necesitan contar con metadatos descriptivos y semánticos que les permitan comprender la estructura y el contenido del dataset.
- En casos donde los datasets deban actualizarse tras una nueva carga o un cambio de esquema en la fuente original, los agentes deben tener suficiente contexto para rediseñar el modelo o adaptar la carga posterior de forma correcta y autónoma.
- Mantener un registro de las consultas en una base de datos de time series permitirá proporcionar contexto actualizado y frecuente a los agentes de IA para futuras operaciones sobre los datasets.
- Al utilizar una base de datos time series, se garantiza que la información registrada sea siempre reciente y relevante, facilitando análisis y respuestas más precisas por parte de los agentes.

### Diagrama de Base de Datos

A continuación se presenta el diagrama de base de datos correspondiente al módulo de La Bóveda. En él se muestra cómo se utiliza la misma base de datos de RDS que en el bioregistro, ya que su rol es meramente administrativo.

Se puede ver cómo existe una tabla que almacena la información principal de los datasets, y que se asocia con PersonaFisica para poder revisar quiénes tienen acceso a dichos datasets. Además, para mantener el diseño normalizado, se tiene una tabla extra que guarda los datasets de pago y dice si son por cuota o pago único, además de su costo. La tabla de Cuotas que guarda cuántas consultas le restan a un usuario con respecto a un dataset, y finalmente una tabla llamada tablas, ya que almacena a que tablas pertenece un dataset.

Con respecto a la estructura de Redshift, esta es imprescindible, por ello no se muestra en el diagrama; dependerá completamente de lo que suban los usuarios. Eso sí, definitivamente estará separada por schema para cada colectivo.

![image](../img/DiagramaBDBoveda.png)