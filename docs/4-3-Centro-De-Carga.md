

# 4.3 Centro de Carga

Este componente representa la primera etapa en el proceso de carga de datasets hacia La Bóveda. Su función principal es extraer datos desde múltiples fuentes, incluyendo:

- Archivos en formato:
  - CSV
  - Excel
  - JSON
- Conexiones a bases de datos:
  - SQL (MySQL, PostgreSQL, SQL Server y MariaDB)
  - MongoDB
- REST APIs externas

Todos los datos obtenidos se almacenan en estado crudo dentro de un bucket S3, sirviendo como punto de entrada para que el Motor de Transformación los procese e inserte posteriormente en Redshift, el núcleo analítico de La Bóveda.

## Diseño del Frontend

### Arquitectura del Cliente

**Client-Side Rendering con Renderizado Estático**

La arquitectura implementa **CSR** con contenido estático servido desde **S3** y **CloudFront** como CDN. Los bundles de React generados durante el build se almacenan en buckets S3 y se distribuyen globalmente através de CloudFront para optimizar latencia y disponibilidad.

**API única** desarrollada en **FastAPI** para toda la comunicación backend, centralizando autenticación, validación y procesamiento de datos.

**Gestión de Estado Durante Uploads Largos**

- **Persistencia automática** en `localStorage` para mantener progreso de uploads pausables/resumibles entre sesiones del navegador
- **Recovery automático** tras desconexiones de red mediante detección de sesiones interrumpidas y restauración del estado exacto
- **Optimización de memoria** para archivos grandes procesando muestras de 10KB usando FileReader API

### Patrones de Diseño de Objetos

#### Chain of Responsibility - Procesamiento de Fuentes de Datos

El sistema debe manejar múltiples tipos de fuentes de datos (archivos, APIs, bases de datos) de manera flexible y extensible. Cada fuente requiere validaciones y procesamientos específicos. Se activa al momento de seleccionar una fuente de datos en la interfaz de usuario.

**Implementación en Frontend:**

- **FileHandler**: Procesa archivos locales (CSV, Excel, JSON) con validación de formato, tamaño y estructura mediante drag-drop o input
- **APIHandler**: Gestiona conexiones con APIs externas, incluyendo testing de conectividad y autenticación OAuth2/API Keys
- **DatabaseHandler**: Maneja extracción directa de bases de datos con discovery de esquemas y selección de tablas

#### Strategy Pattern - Configuración por Tipo de Acceso

Los datasets requieren configuraciones completamente diferentes según su nivel de acceso (público, privado, pagado), con campos y validaciones específicas para cada tipo. Se activa durante el evento `onChange` del selector de tipo de dataset en el wizard de configuración.

**Implementación en Frontend:**

- **PublicStrategy**: Muestra campos de descripción extendida y metadatos de catalogación para datasets abiertos
- **PrivateStrategy**: Despliega controles granulares de permisos con listas de usuarios autorizados y configuración institucional
- **PaidStrategy**: Presenta formularios de pricing, términos de uso y métodos de pago con validación regulatoria

#### Builder Pattern - Configuración Paso a Paso

La configuración de datasets es compleja y requiere múltiples pasos con validaciones interdependientes. El patrón Builder permite construir la configuración gradualmente. Se activa durante la navegación del wizard de configuración, persistiendo automáticamente cada paso.

#### Singleton/Facade - Gateway Centralizado

Se necesita un punto único de comunicación con el backend para mantener consistencia en autenticación, manejo de errores y gestión de conexiones. Se activa durante toda interacción con el backend, desde validaciones hasta uploads finales.

**Implementación en Frontend:**

- **UploadGateway**: Instancia única que centraliza `sendChunk()`, `trackProgress()`, `validateFile()` y `saveConfiguration()`
- **Gestión de conexiones**: Pools HTTP reutilizables, manejo de tokens JWT y retry logic centralizado
- **Abstracción de complejidad**: Oculta múltiples endpoints backend detrás de métodos simples

#### Observer Pattern - Monitoreo Distribuido de Progreso

El progreso de upload debe actualizarse simultáneamente en múltiples componentes de la interfaz sin acoplarlos directamente. Se activa durante todo el proceso de carga con actualizaciones en tiempo real.

**Implementación en Frontend:**

- **UploadProgressObserver**: Actualiza barras de progreso con porcentajes y tiempo estimado
- **UIProgressObserver**: Actualiza componentes específicos mediante referencias React
- **NotificationObserver**: Envía alertas al sistema de messaging del usuario

#### Diagrama de Clases
El diagrama muestra la integración de todos los patrones de diseño implementados en el frontend. La arquitectura se organiza en **5 capas** claramente diferenciadas:

![alt text](../img/ClasesFrontCC.png)

1. **Capa Singleton/Facade**: UploadGateway mantiene una instancia única para toda comunicación con el backend, mientras ChunkUploadManager gestiona la fragmentación de archivos grandes

2. **Capa Chain of Responsibility**: AbstractSourceHandler coordina el procesamiento secuencial de diferentes fuentes de datos (archivos, APIs, bases de datos)

3. **Capa Builder**: DatasetConfigBuilder construye configuraciones paso a paso mediante el wizard interactivo

4. **Capa Strategy**: ConfigurationStrategy y sus implementaciones (Public, Private, Paid) manejan las diferentes configuraciones de acceso

5. **Capa Observer**: ProgressTracker notifica a múltiples observers para actualizar la interfaz de usuario en tiempo real

### Componentes Visuales

#### Flujo de Interacción del Usuario

```
Selección de fuente → validación formato/conectividad → preview con análisis IA →
configuración metadatos → configuración permisos → procesamiento ETDL →
monitoreo transformación → activación dataset
```

Cabe aclarar que el flujo de procesamiento ETDL se realiza de forma asíncrona, por lo que el usuario podrá salirse del portal web y esperar a que le llegue una notificación por correo, y las notificaciones propias de la aplicación.

#### Componentes Principales

- **FileDropZone**: Capacidades drag-drop para archivos hasta 500MB con validación automática y feedback visual inmediato
- **ConfigurationPanel**: Adaptativo que muestra opciones relevantes según el tipo de fuente seleccionada
- **PreviewComponent**: Visualización tabular de primeras 1000 filas con análisis automático de tipos de columnas
- **ProgressDisplay**: Monitoreo específico del proceso ETDL con estados detallados

#### Validación en Tiempo Real

- **Formato de archivo**: Validación `onChange` con `mimeTypeValidator` ejecutándose en menos de 100ms
- **Estructura de datos**: Análisis automático de headers CSV/Excel detectando columnas malformadas
- **Preview inteligente**: Integración con endpoint `/ai/suggest-metadata` para sugerencias automáticas de IA
- **Smart defaults**: Sugerencias automáticas basadas en tipo de archivo y políticas de seguridad

### Estructura de carpetas

```
centro-carga-frontend/
├── src/
│   ├── api/                  # Comunicación con FastAPI
│   │   ├── uploadAPI.js      # Funciones para carga de archivos
│   │   ├── validationAPI.js  # Validaciones server-side
│   │   └── metadataAPI.js    # Gestión de metadatos IA
│   ├── models/               # Entidades de dominio
│   │   ├── Dataset.js        # Modelo principal de dataset
│   │   ├── DatasetConfig.js  # Configuración completa
│   │   ├── UploadProgress.js # Estado de progreso detallado
│   │   └── ValidationResult.js # Resultados de validación
│   ├── components/           # Atomic Design Pattern
│   │   ├── atoms/            # Componentes básicos reutilizables
│   │   │   ├── UploadButton.jsx
│   │   │   ├── FileInput.jsx
│   │   │   ├── ProgressBar.jsx
│   │   │   └── ValidationMessage.jsx
│   │   ├── molecules/        # Combinaciones de atoms
│   │   │   ├── ConfigItem.jsx
│   │   │   ├── ColumnPreview.jsx
│   │   │   ├── PricingPanel.jsx
│   │   │   └── FileMetadata.jsx
│   │   ├── organisms/        # Componentes complejos
│   │   │   ├── FileDropZone.jsx
│   │   │   ├── DatasetConfigForm.jsx
│   │   │   ├── PreviewPanel.jsx
│   │   │   └── ValidationSummary.jsx
│   │   └── templates/        # Layouts de página
│   │       ├── UploadLayoutTemplate.jsx
│   │       ├── WizardTemplate.jsx
│   │       └── ConfigurationTemplate.jsx
│   ├── hooks/                # Custom hooks (ViewModel)
│   │   ├── useFileUpload.js  # Manejo completo de carga
│   │   ├── useDatasetConfig.js # Configuración de datasets
│   │   ├── useDataPreview.js # Preview y análisis de datos
│   │   └── useMetadataAI.js  # Generación automática IA
│   ├── services/             # Lógica de negocio
│   │   ├── UploadManager.js  # Gestión de cargas (Singleton/Facade)
│   │   ├── ValidationService.js # Validaciones (Chain of Responsibility)
│   │   ├── MetadataExtractor.js # Extracción de metadatos
│   │   └── ProgressTracker.js # Seguimiento progreso (Observer)
│   └── utils/                # Utilidades compartidas
│       ├── fileValidators.js # Validadores específicos por tipo
│       ├── formatters.js     # Formateadores de datos
│       └── constants.js      # Constantes del módulo
```

### Tecnologías Integradas

#### Stack Principal

- **React 18**: Base del frontend con hooks y context API
- **Tailwind CSS**: Styling siguiendo Atomic Design principles
- **Formik + Yup**: Formularios robustos con validación completa
- **Plotly**: Visualización de datos durante preview
- **Axios**: HTTP client con interceptors configurados

#### Servicios AWS

- **S3**: Almacenamiento de bundles estáticos
- **CloudFront**: CDN global para servir el web app

### Diagrama del Frontend

![alt text](../img/frontCentrodeCarga.png)

## Diseño del Backend

### Microservicios del Componente

**1. dataset-upload-service**

Este servicio administra la carga inicial de datasets por parte de usuarios desde múltiples fuentes como archivos Excel, CSV, JSON, APIs o conexiones directas a bases de datos SQL y NoSQL.

Los componentes internos incluyen:

- **UploadController:** Expone los endpoints RESTful para gestionar las solicitudes de carga y configuración inicial de datasets.

  - `/upload/dataset:` Permite subir archivos directamente.

  - `/upload/dataset/api:` Configura y prueba conexiones con APIs externas.

- **ValidationManager:** Realiza la validación inicial de estructura, formato y tipo de archivos recibidos. Se utiliza un patrón Strategy para validar los distintos tipos de datos. Esto Permitirá que si en un futuro se quieren agregar nuevos tipos de fuentes sea posible de manera fácil

- **TemporaryStorageHandler:** Almacena temporalmente y de forma cifrada datasets en AWS S3 hasta su validación y transformación.

- **UploadFlowCoordinator:** Coordina el flujo completo desde la carga hasta la validación y notificación. Funciona como un patrón Observer.

El flujo principal para cargar un dataset desde un archivo es el siguiente:

1. Inicio del proceso de carga:

- El frontend llama a `POST /upload/dataset`

```json
{
  "userId": "uuid-del-usuario",
  "datasetName": "Nombre del dataset",
  "fileType": "CSV",
  "fileContent": "base64-string"
}
```

- Antes de continuar cabe aclarar como es que se extraerán los datos:
  - Archivos CSV, JSON, Excel se pasaran a base64 para poder ser enviados por https y luego se almacenarán en el S3.
  - Para el caso de APIs es muy similar, porque es equivalente a pasar archivos en formato JSON.

- Para Mongo y las bases de Datos SQL es un tanto distinta la situación, ya que se ocupan distintos parámetros que con los otros archivos, que son más sencillos.

- Primero que todo el JSON del POST debe verse algo así:

  ```json
  {
    "userId": "uuid-del-usuario",
    "datasetName": "Nombre del dataset",
    "fileType": "TipoDeSQl|Mongo",
    "connString": "https://host:puerto@usuario:contrasena",
    "Datasets": ["Tabla1", "Tabla2", "tabla3"]
    }
  ```
  - Hace falta especificar cual es la fuente, cual es su Connection String, y cuales son las tablas/colleciones que deben ser traidas.


2. Recepción y almacenamiento temporal:

- El UploadController recibe la solicitud y extrae la información del archivo.

- Invoca a `TemporaryStorageHandler.storeTemporary()` pasando el archivo decodificado, el nombre del dataset y el userId.

`El TemporaryStorageHandler` ejecuta un flujo como el siguiente:

```python
import base64
import uuid
import boto3
from cryptography.fernet import Fernet

class TemporaryStorageHandler:
    def __init__(self, s3_client, encryption_key):
        self.s3 = s3_client
        self.fernet = Fernet(encryption_key)

    def storeTemporary(self, base64_file, dataset_name, user_id):
        decoded = base64.b64decode(base64_file)
        encrypted = self.fernet.encrypt(decoded)
        file_id = str(uuid.uuid4()) + ".csv"
        s3_key = f"temp/{user_id}/{file_id}"
        self.s3.put_object(Bucket="data-temp-storage", Key=s3_key, Body=encrypted)
        return {
            "s3_url": f"s3://data-temp-storage/{s3_key}",
            "file_id": file_id
        }
```

- El resultado se guarda en una tabla en DynamoDB llamada `DatasetUploadTemp` con estado "uploaded".

- Cabe aclarar que ese ejemplo tan solo será para los archivos de tipo CSV, JSON, y excel, para los de SQL y Mongo se hará lo siguiente:
  - **SQL/Mongo**: Se enviará un archivo de pyspark que mapeee las tablas/ seleccionadas al S3 de data-temp-storage con formato parquet.



3. Validación inicial:

- ValidationManager toma la URL del archivo en S3 desde DatasetUploadTemp.

- Descarga el archivo cifrado, lo descifra, y realiza validaciones básicas:

  - Revisión de encabezados.
  - Coherencia de tipos de datos por columna.
  - Detección de campos vacíos y estructura tabular.
  - Nombre unico de Dataset.
  - Revisa si todos los registros vienen con un timestamp (este no es un criterio de rechazo, es de contexto).

```python
import pandas as pd
from cryptography.fernet import Fernet
import boto3

class ValidationManager:
    def __init__(self, s3_client, encryption_key):
        self.s3 = s3_client
        self.fernet = Fernet(encryption_key)

    def validate(self, s3_key):
        try:
            obj = self.s3.get_object(Bucket="data-temp-storage", Key=s3_key)
            decrypted = self.fernet.decrypt(obj['Body'].read())
            df = pd.read_csv(pd.compat.StringIO(decrypted.decode('utf-8')))
            assert df.columns is not None
            assert not df.isnull().all(axis=1).any()
            return True
        except Exception as e:
            logger.error(f"Error en validación de dataset: {str(e)}")
            raise
```

4. Notificación y confirmación:

- `UploadFlowCoordinator` utiliza RabbitMQ para enviar mensajes al notification-service, el cual notifica al usuario por correo electrónico o bien por notificación del sistema en caso de estar online, sobre el éxito de la carga inicial y los siguientes pasos para configurar detalladamente el dataset.

```py
import pika
import json

class UploadFlowCoordinator:
    def __init__(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq-host'))
        self.channel = connection.channel()
        self.channel.queue_declare(queue='notification-queue')

    def notify_success(self, user_id, dataset_id):
        message = {
            "type": "upload_success",
            "user_id": user_id,
            "dataset_id": dataset_id,
            "message": "El dataset fue cargado y validado exitosamente."
        }
        self.channel.basic_publish(
            exchange='',
            routing_key='notification-queue',
            body=json.dumps(message)
        )
```

5. Respuesta al frontend:

```json
{
  "datasetId": "uuid-del-dataset",
  "status": "initial-validation-passed"
}
```

**2. dataset-configuration-service**

Una vez el dataset haya sido cargado en el microservicio anterior, sigue el este que permite configurar el comportamiento, incluyendo privacidad, acceso, monetización y periodicidad de actualización. A continuación los componentes internos:

- **ConfigurationController:** Expone los endpoints para definir políticas de configuración por dataset.

  - `/config/dataset/access`
  - `/config/dataset/payment`
  - `/config/dataset/delta`

- **PermissionHandler:** Valida si el usuario tiene permisos administrativos sobre el dataset.

- **PaymentModelService:** Aplica lógica de monetización basada en reglas.

- **DeltaUploadManager:** Define y activa las configuraciones de carga periódica.

**Flujo completo de configuración de un dataset:**

1. Definición de acceso

- El frontend realiza una solicitud `POST /config/dataset/access` con el datasetId y el tipo de acceso:

```json
{
  "datasetId": "uuid-del-dataset",
  "access": "public|private|restricted",
  "allowedUsers": ["uuid-user1", "uuid-user2"]
}
```

- `ConfigurationController` llama a `PermissionHandler.validateOwnership()` para validar que el usuario tenga permisos sobre ese dataset.

- Si pasa la validación, se actualiza `AccesoDataset` en RDS con el nuevo tipo de acceso.

2. Configuración de monetización

- Se llama a `POST /config/dataset/payment`:

```json
{
  "datasetId": "uuid-del-dataset",
  "model": "subscription|per_request|free",
  "price": 9.99,
  "period": "monthly"
}
```

- `ConfigurationController` delega a `PaymentModelService`, que valida el modelo y registra las condiciones en la tabla `DatasetDePago`.

3. Configuración de cargas incrementales

- Solicitud `POST /config/dataset/delta`:

```json
{
  "datasetId": "uuid-del-dataset",
  "cron": "0 0 * * *",
  "connectionId": "secreto-en-secrets-manager",
  "mode": "delta",
  "triggerMethod": "timed_pull|callback",
  "IgnoreColumns": "true|false"
}
```

- `DeltaUploadManager` invoca a `SecurityController.retrieve()` del security-service para obtener credenciales.

- Para el parámetro del Cron se definirán en la UI como posibles tiempos:

  - A una hora específica del día: 1:00, 7:00, 13:00, 22:00, etc.
  - Opción para ejecutar cada 12, 6, 3 horas.

- Para el parámetro de mode están las siguientes opciones.

  - Delta: Permite hacer cargas diferenciales. **Esta opción solo se permitirá si el dataset de la fuente tiene: timestamps en cada registro, garantiza que las PKs (o equivalente) no cambian y son incrementales**.
  - Complete: Solicita que se cargue todo el dataset desde 0 y se deseche el que hay en Redshift.

- Para triggerMethod existen dos opciones:

  - Callback: no se registra el dataset como timed_pull y se asumirá que solo se puede actualizar on demand.
  - Si triggerMethod es timed_pull entonces se registrará en `DatasetCrons` de RDS cada cuanto se hace el pull de los datos, cual es la fuente de datos (el connection string o URL), que tipo es (SQL, MongoDB o API), y el modo en el que opera (Complete o Delta).

- Para IgnoreColumns existen dos opciones:
  - Si se desea que se ignoren columnas nuevas que vengan en los datasets posteriores a la primera carga.
  - Si se desea que cuando venga una nueva columna en una tabla se le añada a toda la tabla destino en redshift.

Respuesta al frontend:

```json
{
  "status": "configured",
  "datasetId": "uuid-del-dataset"
}
```

4. Políticas de acceso y restricción

El sistema de configuración permite definir restricciones adicionales sobre el acceso a datasets privados o pagos. Estas políticas se aplican automáticamente en los microservicios de consulta y son definidas por el usuario administrador del dataset a través de `ConfigurationController`.

- El sistema de permisos evita accesos no autorizados mediante `RBAC` gestionadas por `PermissionHandler`. El sistema de ingresos a los datasets ya fue explicado previamente en el microservicio de la Bóveda, aquí aplica el mismo

Respuesta al frontend:

```json
{
  "status": "configured",
  "datasetId": "uuid-del-dataset"
}
```

5. Además se envía un mensaje por RabbitMQ a la cola que el motor de transformación lee para saber que tiene que procesar un nuevo dataset.

**3. security-service**

Este servicio centraliza el manejo seguro de credenciales y parámetros sensibles relacionados con fuentes de datos externas utilizadas por otros microservicios como dataset-upload-service y dataset-configuration-service. Contiene los siguientes componentes:

- **SecurityController:** Expone endpoints REST para almacenar y recuperar secrets que se encuentran cifrados.

  - `/security/store`: Almacena secretos de conexión (usuario, contraseña, API key).
  - `/security/retrieve`: Devuelve los secretos descifrados para uso interno de microservicios.

- **EncryptionManager:** Se encarga del cifrado y descifrado utilizando AES-256, e integra políticas de rotación automática de llaves.

- **SecretsManagerHandler:** Utiliza AWS Secrets Manager para persistencia de secretos de forma segura y auditable.

Flujos principales del microservicio:

1. Almacenamiento de credenciales

- Cuando un dataset se configura para carga por conexión externa, el frontend envía:

```json
{
  "connectionName": "prod-db",
  "username": "usuario",
  "password": "secreto123",
  "type": "postgres"
}
```

- `SecurityController` recibe la solicitud y llama a `SecretsManagerHandler`, para que llame a EncryptionManager para cifrar los datos.

`SecretsManagerHandler` almacena el secreto bajo una clave.

```py
class EncryptionManager:
    def encrypt(self, data):
        return self.fernet.encrypt(data.encode()).decode()

class SecretsManagerHandler:
    def store_secret(self, key, secret_data):
        client.put_secret_value(SecretId=key, SecretString=secret_data)
```

- Un punto muy importante a aclarar es que para poder identificar el secreto en aws secret manager, se le pondrá el mismo id que el utilizado en la tabla de datasets de la bóveda. De esta forma se puede extraer con facilidad el secret cuando se ocupe hacer pull de datos.

2. Recuperación de credenciales

Otro microservicio solicita el secreto con un secretId:

```json
{
  "secretId": "id123"
}
```

- `SecurityController` consulta a `SecretsManagerHandler` y luego llama a `EncryptionManager.decrypt()` para descifrar antes de devolverlo.

```py
class EncryptionManager:
    def decrypt(self, token):
        return self.fernet.decrypt(token.encode()).decode()
```

Respuesta:

```json
{
  "username": "usuario",
  "password": "secreto123",
  "type": "postgres",
  "dataset": "dataset4"
}
```

4. Notificación

Se envía una notificación al usuario sobre el resultado de la validación utilizando el notification-service.

```json
{
  "status": "validated_with_warnings",
  "reportUrl": "https://s3.amazonaws.com/reports/datasetId_validation.pdf"
}
```

**4. notification-service**

Este servicio permite comunicar eventos relevantes del sistema a los usuarios finales y a sistemas administrativos mediante colas de mensajes, correo electrónico o notificaciones en la aplicación. Tiene los siguientes componentes:

- **NotificationListener:** Escucha los mensajes que llegan a la cola `notification-queue` de RabbitMQ y lo procesa con los handlers segun el tipo de evento.

- **EmailSender:** Envia emails a los usuarios utilizando Amazon SES.

- **WebhookNotificationHandler:** Envía notificaciones a servicios externos vía HTTP POST (por ejemplo, para sistemas de auditoría externos).

- **AdminAuditHandler:** Registra eventos críticos como fallos de validación o problemas de pago en un log especial para revisión administrativa.

Tabla de rutas posibles:

| Tipo de evento      | Handlers                                             |
| ------------------- | ---------------------------------------------------- |
| `upload_success`    | `EmailNotificationHandler`, `AppNotificationHandler` |
| `validation_failed` | `EmailNotificationHandler, AdminAuditHandler`        |
| `external_alert`    | `WebhookNotificationHandler`                         |
| `quota_exceeded`    | `AppNotificationHandler`, `EmailNotificationHandler` |
| `admin_warning`     | `AdminAuditHandler`, `EmailNotificationHandler`      |

**Flujo típico de notificación por evento exitoso:**

1. Otro microservicio (por ejemplo `upload-service` o `validation-service`) publica un mensaje a RabbitMQ con estructura:

```json
{
  "type": "upload_success",
  "user_id": "uuid-user",
  "dataset_id": "uuid-dataset",
  "message": "Tu dataset fue cargado y validado exitosamente."
}
```

2. NotificationListener consume el mensaje y delega la tarea al handler correspondiente:

```py
import pika
import json

class NotificationListener:
    def __init__(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq-host'))
        self.channel = connection.channel()
        self.channel.queue_declare(queue='notification-queue')

    def start_listening(self):
        def callback(ch, method, properties, body):
            data = json.loads(body)
            if data['type'] == 'upload_success':
                EmailNotificationHandler.send_success_email(data['user_id'], data['dataset_id'])
                AppNotificationHandler.add_to_feed(data['user_id'], data['message'])

        self.channel.basic_consume(queue='notification-queue', on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()
```

3. El correo es enviado mediante EmailNotificationHandler.`send_success_email()` y la notificación se agrega al feed del usuario.

Respuesta esperada:

```json
{
  "status": "notified",
  "user_id": "uuid-user",
  "dataset_id": "uuid-dataset"
}
```

### Diagramas de Clases

**1. dataset-upload-service**

Primeramente, los patrones de diseño orientados a objetos utilizados son los siguientes:

- Morado: Representa un facade.
- Amarillo: Representa un observer.
- Naranja: Representa un dependency injection.
- Verde: Representa un strategy.
- Celeste: Muestra un factory.
- Café: Representa un singleton.

Ahora bien, las clases están organizadas de la siguiente manera:

El punto de entrada es el UploadController, que actúa como facade para que el API general del backend se comunique con este microservicio. Este controlador delega las llamadas a un observer mediante el EventManager, encargado de notificar a la lógica de negocio correspondiente según el tipo de llamada realizada al UploadController.

Dentro de esa lógica se encuentran el TemporaryStorageHandler, ValidationManager (Usa un patrón Strategy ya que el tipo de archivo condiciona como se procede en la validación) y UploadFlowCoordinator, que reciben como dependencias los servicios de la segunda capa de facade.

En esta segunda capa se encuentran:

- RabbitMQMessager: abstrae el envío de mensajes al exchange del bioregistro.
- FileHandler: Se encarga de guardar y traer los archivos en S3, y guardar su path en la tabla `DatasetUploadTemp` de DynamoDB.
- DBDumper: Se encarga de hacer los dumps que el FileHandler ocupe, usa un strategy ya que los de SQL y Mongo se hacen de formas distintas.

Finalmente, existe una capa de repositorios gestionada mediante el patrón Factory. Además, cada conexión se maneja utilizando el patrón Singleton.

![identity clases](../img/ClasesCentroCarga1.png)

**2. dataset-configuration-service**

Primeramente, los patrones de diseño orientados a objetos utilizados son los siguientes:

- Morado: Representa un facade.
- Amarillo: Representa un observer.
- Naranja: Representa un dependency injection.
- Celeste: Muestra un factory.
- Café: Representa un singleton.

Ahora bien, las clases están organizadas de la siguiente manera:

El punto de entrada es el ConfigurationController, que actúa como facade para que el API general del backend se comunique con este microservicio. Este controlador delega las llamadas a un observer mediante el EventManager, encargado de notificar a la lógica de negocio correspondiente según el tipo de llamada realizada al ConfigurationController.

Dentro de esa lógica se encuentran el PermissionHandler, PaymentModelService y DeltaUploadManager, que reciben como dependencias los servicios de la segunda capa de facade.

En esta segunda capa se encuentran:

- DatasetManager: Se encarga de crear configuraciones para los datasets como tipos de pago, tipos de carga, autorizaciones.
- FileHandler: Se encarga traer los archivos en S3.
- SecurityRequester: se comunica con el security-service para autorizar a cambios en datasets.

Finalmente, existe una capa de repositorios gestionada mediante el patrón Factory. Además, cada conexión se maneja utilizando el patrón Singleton.

![identity clases](../img/ClasesCentroCarga2.png)

**3. security-service**

Primeramente, los patrones de diseño orientados a objetos utilizados son los siguientes:

- Morado: Representa un facade.
- Amarillo: Representa un observer.
- Naranja: Representa un dependency injection.

Ahora bien, las clases están organizadas de la siguiente manera:

El punto de entrada es el SecurityController, que actúa como facade para que el API general del backend se comunique con este microservicio. Este controlador delega las llamadas a un observer mediante el EventManager, encargado de notificar a la lógica de negocio correspondiente según el tipo de llamada realizada al SecurityController.

Dentro de esa lógica se encuentran el SecretsManagerHandler, que recibe con inyección dependencias los servicios de la segunda capa de facade.

En esta segunda capa se encuentran:

- AWSSecretHandler: Se encarga de cargar y obtener secretos de AWS Secret Manager .
- EncryptionManager: Se encarga del proceso de encripción y desencripción.

![identity clases](../img/ClasesCentroCarga3.png)

**4. notification-service**

Primeramente, los patrones de diseño orientados a objetos utilizados son los siguientes:

- Morado: Representa un facade.
- Celeste: Muestra un factory.
- Verde: Representa un strategy.
- Naranaja: Dependency Injection.
- Café: Representa un Singleton Pattern.

Ahora bien, las clases están organizadas de la siguiente manera:

Se cuenta con una clase abstracta NotificationListener que provee la lógica y conexión a RabbitMQ. Esta clase es reutilizada por dos componentes principales:

- EmailSender: escucha mensajes destinados a ser reenviados por correo electrónico a través de AWS SES utilizando el SESService.
- NotificationConsumer: detecta la llegada de nuevas notificaciones que deben mostrarse dentro de la aplicación.

Además, existe una capa encargada de escuchar conexiones de usuarios al frontend para enviar notificaciones en tiempo real mediante el WebSocketController. En segundo plano, el NotificationConsumer verifica si llegan nuevas notificaciones. Si el usuario está conectado, se le muestran inmediatamente; de lo contrario, se almacenan en DynamoDB a través del NotificationManager, para que en la próxima conexión el WebhookNotificationHandler se las muestre.

Finalmente, existe una capa de repositorios gestionada mediante el patrón Factory. Cada conexión es manejada utilizando el patrón Singleton.

![identity clases](../img/ClasesCentroCarga4.png)

### Servicios de AWS

**Amazon S3**
El servicio de **AWS S3** será el almacén principal para la carga de datos en crudo de los datasets este será utilizado por **TemporaryStorageHandler** en **dataset-upload-service**. También es importante mencionar que este servicio servirá para el acceso a los datasets por **validation-service** para el análisis de los datos.

**Configuración de Hardware:** Servicio de almacenamiento de objetos, ilimitadamente escalable. No requiere configuración de hardware directa.

**AWS KMS:**
Los datasets necesitan ser protegidos para ello utilizamos **AWS KMS** ya que este servicio nos será de utilidad para proporcionar las claves criptográficas para el cifrado y descifrado de los datos.
Se utilizará para proteger los datasets almacenados temporalmente en **S3** por **TemporaryStorageHandler** en **dataset-upload-service** y para el cifrado/descifrado de secretos gestionados por el **security-service**.

**Configuración de Hardware:** Servicio gestionado, serverless. No requiere configuración de hardware. Sin embargo, se pueden configurar la creación de claves.

- **Tipo de clave:** Simétrico
- **Uso de claves:** Cifrado y descifrado
- **Origen del material de claves:** KMS
- **Regionalidad:** Clave de una sola región

**AWS SES**
Será el servicio para el envío de correos electrónicos transaccionales a los usuarios finales (ej., notificación de carga exitosa, fallo de validación), gestionado por el **EmailNotificationHandler** dentro del **notification-service**.

**Configuración de Hardware:**
Para configurar un SES simplemente necesitamos dirigirnos a crear una identidad. En tipo de identidad utilizaremos **Dirección de correo electrónico**, luego en **Dirección de correo electrónico** colocamos el correo electrónico que utilizaremos (ej. notificacionesDatos@gmail), luego nos llega una notificación al correo donde tendremos que verificar la dirección de correo electrónico.

### Sistema de Monitoreo

El monitoreo del Componente del Centro de Carga de Datos se implementará siguiendo una estrategia de observabilidad integral que permita supervisar en tiempo real el comportamiento, rendimiento y seguridad de todo el proceso de ingesta inicial de datasets.

**Métricas y Rendimiento**

**AWS CloudWatch** será el servicio para monitoreo más importante se encargara de recopilar y almacenar métricas operacionales del Componente del Centro de Carga de Datos. Se monitorizarán aspectos críticos como:

**Métricas de Negocio:**

- Cantidad de datasets cargados exitosamente por formato (CSV, Excel, JSON).
- Tasa de éxito en la validación inicial de esquema y estructura del archivo.
- Tiempo promedio del proceso completo de carga (desde la recepción hasta el almacenamiento temporal en S3).
- Volumen de datos (en GB) ingesados diariamente.
- Cantidad de notificaciones de carga enviadas (éxito/fracaso).

**Métricas de Infraestructura:**

- **S3 (data-temp-storage):** Latencia de operaciones PutObject, GetObject, ListObjects; cantidad de PutRequests, GetRequests; tasa de errores (4xx, 5xx).
- **RDS/DynamoDB:** Latencia de conexiones, ReadIOPS, WriteIOPS, utilización de recursos para las tablas DatasetUploadTemp y DatasetMetadata.
- **AWS RabbitMQ:** Tamaño de la cola de notificaciones de notification-queue, mensajes entrantes/salientes, latencia de conexión al broker.
- **AWS KMS:** Tasa de solicitudes y errores en las operaciones de cifrado/descifrado de las claves usadas por dataset-upload-service.

**Prometheus** complementará a CloudWatch recopilando métricas específicas como las del microservicio de **dataset-upload-service** a través de un **endpoint** dedicado. Esto permitirá obtener métricas más granulares sobre el comportamiento interno de la aplicación, como:

- Los contadores de operaciones específicas (ej., validation_attempts_total, encryption_calls_total).
- Los histogramas de distribución de tiempos (ej., file_parsing_duration_seconds, db_write_duration_seconds).

**Visualización y Dashboards**
**Grafana** se utilizará como plataforma principal de visualización, integrándose tanto con CloudWatch como con Prometheus para crear dashboards interactivos que permitan:

- **Dashboard Operacional de Carga:** Vista en tiempo real del estado general del proceso de carga de datos. Mostrará el volumen de cargas activas, la distribución de archivos por formato, la tasa de éxito/fracaso de las cargas, y el estado de salud de los pods de dataset-upload-service y sus dependencias (S3, DBs, MQ).

- **Dashboard de Rendimiento de Carga:** Monitoreo específico de las latencias. Incluirá el tiempo promedio del proceso de carga, la latencia de escritura en S3, la latencia de registro de metadatos en DBs, y el consumo de recursos (CPU/memoria) del **dataset-upload-service**.

- **Dashboard de Calidad y Seguridad de Carga:** Seguimiento de eventos relacionados con la calidad inicial y la seguridad del proceso de carga. Mostrará la tasa de errores en la validación inicial de esquema, intentos de acceso no autorizado a recursos de carga vía security-service, y monitoreo de las operaciones de cifrado.

**Logs y Trazabilidad**
El sistema de logging aprovechará **CloudWatch Logs** para centralizar todos los registros generados por los componentes del Centro de Carga de Datos. Se implementará un esquema de logging estructurado que facilite:

- **Trazabilidad Completa con AWS X-Ray:** Cada transacción de carga tendrá un identificador único de correlación (ID de traza X-Ray) que permitirá seguir su flujo desde la recepción del archivo, pasando por la interacción con S3, KMS, el registro de metadatos en RDS/DynamoDB, y la interacción con security-service o validation-service, hasta la notificación final.

- **Auditoría y Diagnóstico**
  - **CloudWatch Logs Insights:** Permite la consulta interactiva de logs para identificar rápidamente la causa raíz de cualquier incidencia (ej., errores en el procesamiento de un tipo de archivo específico).
  - **AWS CloudTrail:** Registra todas las llamadas a la API de AWS realizadas por el dataset-upload-service y sus roles asociados (ej., s3:PutObject, kms:Encrypt, secretsmanager:GetSecretValue), esencial para auditoría y seguridad.

**Sistema de Alertas y Notificaciones**
Se configurará un sistema proactivo de alertas utilizando **CloudWatch Alarms** que notificará al equipo de operaciones cuando se detecten condiciones anómalas:

- **Alertas Críticas (respuesta inmediata requerida):**

  - Fallo total del **dataset-upload-service** o indisponibilidad de su **endpoint** de **health check**.
  - Tasa de error (HTTP 5xx en el UploadController o en S3) superior al 5% en una ventana de 5 minutos.
  - Fallo en la conexión con servicios críticos (S3, RDS/DynamoDB, KMS, Amazon MQ).
  - Detección de un incremento súbito de errores en operaciones de cifrado/descifrado (KMS).
  - Errores críticos registrados en CloudWatch Logs por el dataset-upload-service (ej., Unhandled Exception).

- **Alertas de Advertencia (revisión prioritaria):**

  - Degradación del rendimiento con latencias de carga de datasets superiores a 30 segundos.
  - Uso de recursos (CPU, memoria) del pod de **dataset-upload-service** por encima del 80% de capacidad.
  - Incremento inusual en las validaciones iniciales de datasets fallidas.
  - Acumulación de objetos sin procesar en el bucket data-temp-storage por más de un umbral de tiempo.

- **Alertas Informativas (seguimiento regular):**
  - Resumen diario de métricas operacionales de carga (ej., total de cargas exitosas del día).
  - Reporte semanal de tendencias de volumen de datos ingesados.

**Monitoreo de Cumplimiento y Seguridad**
Dado el manejo de datos sensibles en la carga, se implementarán controles específicos de monitoreo para garantizar el cumplimiento normativo y la seguridad:

- **Auditoría de Accesos a Datos Cargados:** Registro detallado usando CloudTrail y CloudWatch Logs de todos los accesos PutObject, GetObject al bucket data-temp-storage, identificando quién accedió, cuándo y con qué propósito.
- **Verificación de Cifrado:** Monitoreo continuo del estado de cifrado de datos en reposo en S3 mediante políticas de bucket y eventos de KMS, asegurando que todos los archivos cargados estén cifrados correctamente.
- **Monitoreo de Acceso a Secretos:** Seguimiento de los intentos de acceso y las rotaciones de credenciales en AWS Secrets Manager utilizadas por el dataset-upload-service para conectarse a fuentes externas o bases de datos.

**Health Checks y Disponibilidad**
Los microservicios del Centro de Carga implementarán múltiples niveles de verificación de salud que serán monitoreados continuamente por Kubernetes y los sistemas de monitoreo:

- **Liveness Probe:** Verificación básica de que el dataset-upload-service está activo y respondiendo, ejecutada cada 10 segundos por Kubernetes.
- **Readiness Probe:** Verificación comprehensiva de que el dataset-upload-service puede procesar solicitudes de carga, incluyendo conectividad con S3, KMS, bases de datos (RDS/DynamoDB) y Amazon RabbitMQ.
- **Deep Health Checks:** Verificaciones periódicas más exhaustivas que validan la integridad de configuraciones críticas (ej., validación de esquemas de carga), la disponibilidad de claves de cifrado, y la correcta operación del flujo completo de carga de un archivo de prueba simulado.

**Análisis y Mejora Continua**
El sistema de monitoreo no solo detectará problemas, sino que proporcionará insights para la mejora continua del proceso de carga:

- **Análisis de Tendencias:** Identificación de patrones en el volumen y tipo de cargas (ej., picos horarios, aumento de un formato específico) para optimizar recursos y predecir necesidades futuras.
- **Detección de Anomalías:** Uso de las capacidades de CloudWatch para identificar comportamientos inusuales (ej., caída repentina en el número de cargas exitosas) que podrían indicar problemas emergentes.
- **Reportes de Capacidad:** Proyecciones basadas en datos históricos de volumen de carga y uso de recursos para planificar el crecimiento de la infraestructura de almacenamiento (S3) y cómputo (EKS).
- **Optimización de Costos:** Análisis del uso de recursos de S3, EKS y DBs para identificar oportunidades de optimización de costos sin comprometer el rendimiento.

### Modelo de seguridad detallado

El backend del componente Centro de Carga gestiona información crítica relacionada con datasets, incluyendo la carga, validación y categorización. Dado su rol esencial, se implementará un modelo de seguridad robusto y granular orientado a prevenir accesos no autorizados, asegurar integridad, confidencialidad, trazabilidad y disponibilidad continua de los datos.

1. Control de Acceso Granular

| Rol del usuario  | Descripción                                         | Permisos sobre recursos del Centro de Carga                                                                |
| ---------------- | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `Carga:viewer`   | Usuario con acceso de solo lectura                  | Visualizar historial de cargas, detalles de configuración, esquema de columnas y metadatos                 |
| `Carga:editor`   | Usuario autorizado a diseñar y actualizar cargas    | Crear cargas nuevas, definir esquema de columnas, asociar metadata, configurar delta                       |
| `Carga:approver` | Validador de configuraciones previas a la ejecución | Aprobar configuraciones antes de ser activadas, validar transformaciones, confirmar integridad estructural |
| `Carga:admin`    | Administrador completo del módulo de carga          | Modificar permisos de carga, eliminar configuraciones, visualizar trazabilidad completa, forzar cargas     |

Ejemplo de flujo de autorización en RDS (PostgreSQL):

- **AccesoADataset**: registra qué personas tienen acceso a cada dataset.
- **DatasetDePago y TipoDePago**: gestionan la configuración de pagos asociados a datasets, incluyendo su categorización.
- **DatasetCrons**: define el modo de carga que tendrán los datasets recurrentes (Delta, Complete), y el tipo de fuente del que pueden venir (Base de datos o API). Esta tabla será consultada por Airflow para aplicar los DAGs correspondientes de forma automatizada.
- **Tablas**: Esta tabla almacena a que Dataset pertenecen las distintas tablas de Redshift .
1. Un usuario autenticado realiza una solicitud para modificar una configuración de carga.

2. El backend identifica que el usuario tiene rol `Carga:editor` y autentica su token internamente.

3. Se ejecuta una función almacenada en PostgreSQL:


```SQL
SELECT actualizar_configuracion_carga(:id_config, :nueva_metadata, :usuario);
```


4. Dentro de la función `actualizar_configuracion_carga`, se valida que el usuario tenga permisos equivalentes al rol editor en la tabla `roles_usuario`:

```SQL
IF NOT EXISTS (SELECT 1 FROM roles_usuario WHERE usuario = $3 AND rol = 'editor') THEN
  RAISE EXCEPTION 'Acceso no autorizado';
END IF;
```

5. Si pasa la validación, se actualizan los campos correspondientes; en caso contrario, se bloquea la operación y se registra un intento fallido en la bitácora de auditoría.

**2. Cifrado de Información**

#### Cifrado en tránsito

Todas las comunicaciones entre el frontend del centro de carga, los microservicios y los servicios de almacenamiento (Amazon S3 y RDS), se ejecutan mediante HTTPS con TLS 1.3. Igualmente, EKS fuerza el uso de TLS con certificados actualizados gestionados mediante AWS Certificate Manager.

#### Cifrado en reposo

Cada tipo de dato gestionado por el Centro de Carga está protegido mediante mecanismos nativos de cifrado proporcionados por los servicios utilizados:

| Tecnología      | Elementos cifrados                                | Mecanismo de cifrado                       | Particularidades de seguridad                                                        |
| --------------- | ------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------ |
| Amazon S3       | Archivos de datasets cargados + metadata asociada | AWS KMS                                    | Bucket con políticas que rechazan cargas no cifradas y control de acceso restringido |
| Amazon RDS      | Configuraciones estructurales                     | Cifrado de disco automático con claves KMS | Acceso restringido a través de funciones y roles internos                            |
| Amazon DynamoDB | Estados de carga, historial de ejecución          | Cifrado nativo activado automáticamente    | Acceso limitado por política IAM de microservicio                                    |

**Adicionalmente**

- Los archivos cargados son escaneados y validados antes de ser almacenados. Solo si cumplen con los requisitos del esquema de columnas aprobado y no presentan fallos estructurales o semánticos, se escriben en el bucket correspondiente, con nombre aleatorio y metadata cifrada.

- En caso de rechazo en el proceso de validación, el archivo se descarta y se registra el evento en la bitácora para trazabilidad.

**3. Auditoría y Trazabilidad**

#### Elementos auditados

- Solicitudes de creación, modificación y eliminación de configuraciones de carga.
- Procesos de validación estructural y semántica.
- Aprobaciones manuales o automáticas.
- Errores detectados en archivos cargados.
- Consultas sobre configuraciones y ejecuciones pasadas.

#### Origen y estructura del registro

1. Identificador de usuario y rol.
2. Timestamp exacto de la operación.
3. Tipo de operación realizada.
4. IP de origen o microservicio emisor.
5. Resultado de la acción (éxito, error, rechazo por validación).

#### Tecnologías utilizadas

- **Amazon CloudWatch Logs:** Registro estructurado de eventos en tiempo real.

- **Amazon DynamoDB Streams:** Replicación de eventos sensibles a una tabla de auditoría histórica.

#### Acceso y resguardo

El acceso a los registros está restringido a roles con privilegios de auditoría mediante políticas IAM. Se implementan estrategias de rotación, almacenamiento cifrado y retención mínima de 12 meses.

**4. Monitoreo y Gestión de Incidentes**

#### 4.1 Monitoreo en Tiempo Real

- **Prometheus:** Se utiliza para recolectar métricas personalizadas relacionadas con la carga de datasets, como el tiempo promedio de validación de un archivo o la tasa de éxito en las cargas de datos.

- **AWS CloudWatch:** Monitorea los logs generados por los microservicios del Centro de Carga, enviando alertas cuando se detectan patrones anómalos, como fallos recurrentes o tiempos de espera demasiado largos en el procesamiento de datos.

#### 4.2 Gestión de Incidentes

Esta sección está diseñada para identificar y responder rápidamente ante cualquier tipo de evento que pueda comprometer la integridad del sistema o la seguridad de los datos.

1. **Detección de Incidentes:** Se utilizan reglas de alerta configuradas en CloudWatch para detectar incidentes como errores en la carga de datos, archivos rechazados por validaciones o caídas de servicios externos (como bases de datos o APIs).

2. **Clasificación:** Se evalúa la gravedad del incidente y se clasifica como crítico, medio o bajo.

| **Clasificación de Incidente** | **Descripción**                                                                                                                                                                         | **Ejemplo**                                                                                                                                                                              | **Acción Requerida**                                                                                                                            |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Crítico**                    | Incidentes que afectan directamente la operación del sistema y pueden comprometer la seguridad o la integridad de los datos. Requieren una acción inmediata para restaurar el servicio. | - Caída de base de datos (Amazon RDS) durante una carga de datos. <br> - Exposición accidental de datos sensibles.                                                                       | - Restauración inmediata desde backups. <br> - Notificación a los administradores a través de AWS SNS. <br> - Reinicio automático de servicios. |
| **Medio**                      | Incidentes que afectan el rendimiento o la funcionalidad del sistema. Se pueden retrasar procesos o requerir una intervención manual.                                                   | - Error en la validación de un archivo de carga que retrasa la operación pero no detiene el flujo. <br> - Lento procesamiento de un dataset debido a un error de configuración temporal. | - Notificación al equipo de soporte. <br> - Revalidación y reintento de carga.                                                                  |
| **Bajo**                       | Incidentes menores que no afectan el funcionamiento principal del sistema, pero que requieren atención para evitar que se conviertan en problemas mayores.                              | - Un archivo rechazado por un error de formato menor. <br> - Una solicitud de visualización de metadatos que no devuelve resultados por una pequeña falla en el frontend.                | - Registro del incidente en el sistema de auditoría. <br> - Resolución del error en la próxima actualización.                                   |

3. **Respuesta Automática:** En caso de un incidente, se utiliza AWS Lambda para ejecutar funciones que puedan mitigar el impacto.

```py
import json
import boto3
import logging

# Configurar el cliente de S3
s3_client = boto3.client('s3')
lambda_client = boto3.client('lambda')

# Configurar el cliente de SNS para notificaciones
sns_client = boto3.client('sns')

# Nombre del bucket y archivo que estamos tratando de cargar
bucket_name = 'nombre-del-bucket'
file_key = 'ruta/al/archivo/dataset.csv'

# Tema de SNS para notificación de incidentes
sns_topic_arn = 'arn:aws:sns:region:account-id:topic-name'

# Función Lambda para manejar el incidente
def lambda_handler(event, context):
    try:
        # Intentamos cargar el archivo desde S3 nuevamente (simulando la carga de datos)
        response = s3_client.upload_file(file_key, bucket_name, file_key)
        logging.info(f"Archivo cargado exitosamente: {file_key}")

        # Si la carga fue exitosa, enviar una notificación de éxito
        send_notification("Carga de datos exitosa", "El archivo se cargó correctamente.")

        return {
            'statusCode': 200,
            'body': json.dumps('Carga exitosa')
        }

    except Exception as e:
        logging.error(f"Error en la carga de datos: {str(e)}")

        # Enviar una notificación de error
        send_notification("Error en la carga de datos", f"Ocurrió un error: {str(e)}")

        # Reintentar la carga, si la operación falló
        logging.info(f"Reintentando carga para el archivo: {file_key}")
        return retry_load()

# Función para reintentar la carga del archivo
def retry_load():
    try:
        # Intentar subir el archivo a S3 nuevamente
        s3_client.upload_file(file_key, bucket_name, file_key)
        logging.info("Carga reintentada exitosa.")
        send_notification("Carga reintentada exitosa", f"El archivo {file_key} se ha cargado exitosamente después del reintento.")

        return {
            'statusCode': 200,
            'body': json.dumps('Carga reintentada exitosa')
        }

    except Exception as e:
        logging.error(f"Error en el reintento de carga: {str(e)}")
        send_notification("Error en el reintento de carga", f"Ocurrió un error en el reintento: {str(e)}")

        return {
            'statusCode': 500,
            'body': json.dumps('Fallo en la carga después del reintento')
        }

# Función para enviar notificaciones a SNS
def send_notification(subject, message):
    response = sns_client.publish(
        TopicArn=sns_topic_arn,
        Message=message,
        Subject=subject
    )
    logging.info(f"Notificación enviada: {response}")

```

4. **Notificación de Incidentes:** Cuando un incidente es clasificado como crítico AWS SNS envía notificaciones a los administradores y responsables de la seguridad.

### Elementos de Alta Disponibilidad

**1. Almacenamiento Distribuido**

Se utiliza Amazon S3 para el almacenamiento seguro de los datos de carga, incluyendo archivos de configuración, logs y otros datos asociados con el proceso. Con una política de replicación cruzada de objetos y versionado, cualquier archivo cargado se replica automáticamente a otra zona de disponibilidad. Con esto se cumple la disponibilidad de los datos en caso de fallo en una zona. Para los datos como logs de operaciones, se usa Amazon DynamoDB con activación de Point-in-Time Recovery para asegurar la disponibilidad continua de los metadatos asociados con las cargas.

| Recurso        | Tecnología    | Implementación                                | Activación                     | Ubicación   |
| -------------- | ------------- | --------------------------------------------- | ------------------------------ | ----------- |
| Datos de Carga | **Amazon S3** | Replicación cruzada entre zonas y versionado  | Cada vez que se carga/modifica | `us-east-1` |
| Metadatos      | **DynamoDB**  | Backup continuo con recuperación en el tiempo | En cada operación de escritura | `us-east-1` |

**2. Monitoreo y Alertas**

Se utiliza AWS CloudWatch para obtener métricas de disponibilidad de los recursos del backend del Centro de Carga como el uso de CPU, memoria y latencia. Por otro lado, se configura Prometheus para la recolección de métricas personalizadas sobre los microservicios que gestionan las cargas de trabajo y las interacciones del sistema, con visualización de las métricas en Grafana.

| Tecnología     | Función                                         | Ubicación                           | Ejecución                           |
| -------------- | ----------------------------------------------- | ----------------------------------- | ----------------------------------- |
| **CloudWatch** | Monitoreo de métricas de infraestructura AWS    | Servicios de AWS                    | En tiempo real y continuo           |
| **Prometheus** | Recolección de métricas específicas del sistema | Dentro del clúster EKS              | Cada vez que se actualizan métricas |
| **Grafana**    | Visualización de datos para diagnóstico         | Conectado a CloudWatch y Prometheus | Monitoreo constante                 |

**3. Balanceo de carga**

#### 3.1 Distribución de Solicitudes a Microservicios

Las solicitudes entrantes, como las que requieren la carga de datos o la consulta de estado, son dirigidas al Application Load Balancer de AWS. Este ALB distribuye las solicitudes entre las diferentes instancias de los microservicios encargados de procesar los datos.

- Si el Centro de Carga recibe varias solicitudes simultáneas para cargar grandes volúmenes de datos desde Amazon S3, el ALB distribuye estas solicitudes entre las instancias disponibles que gestionan el procesamiento de estos archivos.

#### 3.2 Auto Scaling para Manejo de Picos de Tráfico

El Centro de Carga está configurado con Auto Scaling Groups (ASG) para ajustarse automáticamente a los picos de tráfico. Cuando el volumen de solicitudes sube, el Auto Scaling agrega nuevas instancias para manejar la mayor carga.

- Si se detecta un aumento en el tráfico durante un periodo de alta demanda, el Auto Scaling aumenta automáticamente el número de instancias disponibles para manejar las nuevas solicitudes de carga sin que se experimenten fallos en el sistema.

#### 3.3 Integración con Kubernetes

El Centro de Carga también se beneficia del uso de Amazon EKS para gestionar microservicios. El ALB trabaja en dirigir el trafico a contenedores específicos dentro del clúster de Kubernetes, mejorando la distribución de solicitudes.

- En un escenario donde se requiere escalar dinámicamente los microservicios, el Ingress Controller en combinación con el ALB asegura que el tráfico se distribuya equitativamente entre los contenedores de Kubernetes.

### Diagrama del Backend

A continuación se presenta el diagrama del backend del Centro de carga. En él se evidencia cómo todo el ecosistema de AWS interactúa con los distintos microservicios desplegados en el clúster de Kubernetes provisto por EKS. También se describen los clases internas de cada microservicio, los patrones utilizados, y cómo interactúan entre sí.

Se muestra cómo la contenerización de cada microservicio se realizará utilizando Docker, y cómo el monitoreo interno será gestionado por Prometheus. Además se visualiza el cluster autogestionado de Spark para extraer datasets de fuentes externas.

![image](../img/DiagramaBackendCC.svg)


## Diseño de los Datos

La influencia de este componente sobre la base de datos es mínima, ya que reutiliza la misma instancia de RDS compartida con La Bóveda y el Bioregistro, cuyas especificaciones ya fueron detalladas previamente. Del mismo modo, las configuraciones para DynamoDB y S3 se mantienen idénticas a las de esos componentes.
El único aporte nuevo se encuentra reflejado en el diagrama de base de datos que se presenta a continuación.

### Diagrama de Base de Datos

A continuación se presenta el diagrama de base de datos correspondiente al módulo del Centro de Carga. Este diagrama incluye las tablas clave que componen el componente, entre ellas:

- **AccesoADataset**: registra qué personas tienen acceso a cada dataset.
- **DatasetDePago y TipoDePago**: gestionan la configuración de pagos asociados a datasets, incluyendo su categorización.
- **DatasetCrons**: define el modo de carga que tendrán los datasets recurrentes (Delta, Complete), y el tipo de fuente del que pueden venir (Base de datos o API). Esta tabla será consultada por Airflow para aplicar los DAGs correspondientes de forma automatizada.

![image](../img/DiagramaBDCentroCarga.png)
