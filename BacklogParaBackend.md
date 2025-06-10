  ##### Microservicios



#### Modelo de Seguridad

La Bóveda es el componente central para el almacenamiento, recuperación y gestión segura de información sensible, como claves criptográficas, registros de trazabilidad, y documentos oficiales del ecosistema Data Pura Vida. Debido a su naturaleza crítica, implementa un modelo de seguridad reforzado basado en el cifrado extremo a extremo, control de acceso estricto, y auditoría detallada.

---

### 1. Acceso controlado por credenciales cifradas

- La Bóveda requiere que cada operación (consulta, recuperación, descarga) esté asociada a una clave tripartita cifrada(institución, Data Pura Vida, y usuario autorizado).
- Estas claves se desencriptan en memoria solamente al validar la autorización, y **nunca se almacenan en texto plano**.

---

### 2. Autenticación federada y MFA

- Toda solicitud a La Bóveda pasa por Cognito, utilizando autenticación federada (usuarios de instituciones) y verificación multifactor (OTP, correo institucional).
- Solo usuarios autenticados con rol institucional específico pueden acceder a recursos bajo su control.

---

### 3. Cifrado extremo a extremo (E2EE)

- Los documentos y registros almacenados en La Bóveda se cifran:
  - En tránsito (HTTPS/TLS 1.3)
  - En reposo (AES-256 en S3)
  - En acceso (desencriptado temporal en memoria RAM protegida)
- Se usa AWS KMS para gestionar las claves maestras asociadas a cada institución.

---

### 4. Control de acceso basado en roles (RBAC)

- Cada acción está protegida por un sistema de roles jerárquicos que determinan:
  - Qué usuarios pueden leer, escribir o auditar.
  - Qué instituciones tienen permisos sobre ciertos archivos o registros.
- Las políticas de autorización se verifican en el backend mediante decoradores de validación en FastAPI.

---

### 5. Firma digital y registro inmutable

- Toda operación en La Bóveda (subida, acceso, descarga, modificación) queda firmada digitalmente.
- Se genera una entrada en la bitácora inmutable, con:
  - ID del usuario
  - Timestamp
  - Acción realizada
  - Firma criptográfica

---

### 6. Detección de integridad y validación de hash

- Al momento de subir archivos, se calcula un hash SHA-256 del contenido original.
- Cada vez que se accede o descarga el documento, el sistema recalcula el hash y lo compara con el original.
- Si hay diferencia, se marca como archivo corrupto o alterado.

---

### 7. Registro de auditoría y trazabilidad

- Se mantiene un sistema de logs firmados y cifrados que registra:
  - Quién accedió a qué documento
  - Cuándo
  - Desde qué IP
  - Con qué resultado (éxito, error, rechazo)

- Esta información se puede consultar solo por usuarios con rol de auditor institucional o personal autorizado del Ministerio.

---

### Tecnologías involucradas

| Componente            | Función                                    |
|-----------------------|---------------------------------------------|
| AWS Cognito           | Autenticación federada + MFA               |
| JWT                   | Token de sesión con claims por institución |
| AWS S3 + KMS          | Almacenamiento cifrado                     |
| PostgreSQL / DynamoDB | Metadatos y claves tripartitas             |
| SHA-256               | Verificación de integridad de archivos     |
| FastAPI               | Control de acceso y validación de roles    |
| RabbitMQ              | Bitácora de auditoría y eventos internos   |




**AWS Lambda:**
Para funciones serverless que realicen tareas específicas y de corta duración, como el procesamiento de notificaciones o tareas de validación asíncronas.

**Configuración de Hardware:**  Aunque no gestionamos hardware directamente, sí configuraremos los recursos, como:
- **Memoria:** 1024 MB
- **Arquitectura:** arm64
- **Tiempo de ejecución:** Node.js 22.x
- **Almacenamiento efímero:** 512MB
- **Tiempo de espera:** 5s
- **Retry attempts:** 1


#####  Explicación de las capas – Diseño del Backend del Bioregistro

El backend del componente Bioregistro de Data Pura Vida está diseñado siguiendo principios de Clean Architecture, con separación clara de responsabilidades y desplegado como un microservicio independiente en EKS (AWS Kubernetes). A continuación se describen sus capas principales:

##### Capas del Backend

```plaintext
[ API Layer (FastAPI Gateway) ]
          ↓
[ Service Layer (Application Logic) ]
          ↓
[ Domain Layer (Entities and Rules) ]
          ↓
[ Infrastructure Layer (Database, SumSub, Cognito, S3, RabbitMQ) ]
```
---

- ##### 1. API Layer (FastAPI)

- Punto de entrada del sistema.
- Expone rutas RESTful como `/register`, `/verify`, `/submit-docs`.
- Gestiona validaciones superficiales de entrada (schemas con Pydantic).
- Inyecta dependencias necesarias (servicios, repositorios).

- ##### 2. Service Layer (Application Logic)

- Contiene la lógica de negocio del Bioregistro: validaciones cruzadas, coordinación de flujos, llamadas a SDKs externos.
- Ejemplos:
  - Validar que el representante legal esté previamente registrado como persona física.
  - Activar flujos de SumSub (KYC/KYB) y asociarlos al usuario.
  - Generar y almacenar llaves criptográficas tripartitas para organizaciones.

- ##### 3. Domain Layer (Modelos y Reglas del Negocio)

- Define las entidades del sistema como `Persona`, `Organización`, `DocumentoLegal`, `ClaveTripartita`.
- Aplica validaciones estructurales, reglas de integridad y eventos de dominio.
- Estas clases no dependen de tecnologías externas ni del framework (independencia del dominio).

- ##### 4. Infrastructure Layer

- Conecta el dominio con el mundo externo.
- Incluye:
  - **PostgreSQL**: almacena usuarios, organizaciones y relaciones.
  - **DynamoDB**: guarda estructuras más dinámicas como flujos temporales y metadatos de SumSub.
  - **RabbitMQ**: cola de eventos para acciones asincrónicas (verificación, notificaciones).
  - **S3**: almacenamiento de PDFs y evidencia de verificación.
  - **Cognito**: autenticación de usuarios físicos con MFA.
  - **SumSub SDK**: validación de identidad, prueba de vida y compliance KYC/KYB.


##### Servicios de AWS y Configuración de Hardware
El proyecto **Portal Data Pura Vida** utilizará una amplia gama de servicios de AWS para construir una plataforma robusta y segura. La asignación de hardware será flexible y se adaptará en tiempo real al consumo de los servicios.


**Amazon EKS(Elastic Kubernetes Service):**
Se utilizará para desplegar los microservicios del backend.

**Configuración de Hardware:**
EKS abstrae la infraestructura subyacente. Se configurarán grupos de con instancias EC2.

- **Versión de Kubernetes:** 1.29 (o la más reciente compatible).
- **Tipo de nodo:** Amazon EC2.
- **Tipo de instancia:** t3.medium (2 vCPU, 4 GB RAM) o superior.
- **Almacenamiento:** AWS S3 para almacenamiento de objetos y datasets.


**Servicios de Red:**

**AWS Application Load Balancer (ALB):**
Para distribuir el tráfico de entrada a los microservicios desplegados en EKS.

**Configuración de Hardware:** Es un servicio gestionado, no requiere configuración de hardware directa, ni recursos. Se dimensionará automáticamente.


**Servicios de Almacenamiento:**

**Amazon S3 (Simple Storage Service):**

**Para Datos No Estructurados:**
Almacenamiento escalable y seguro para grandes volúmenes de documentos cargados por los usuarios (cédulas, actas, etc.).

**Configuración de Hardware:** Servicio de almacenamiento de objetos, ilimitadamente escalable. No requiere configuración de hardware directa.

Sin embargo, al crear el bucket en el S3 el cifrado será un **SSE-S3**. Tambien al realizar carga de archivos se utilizará un tipo de almacenamiento **estándar**.

**DynamoDB:**
Base de datos NoSQL para gestionar metadatos dinámicos, configuraciones y datos de alto rendimiento que requieren baja latencia y alta concurrencia (ej., llaves de seguridad, registros de actividad).

**Configuración de Hardware:** Servicio completamente gestionado y serverless. La configuración se basa en las unidades de capacidad de lectura/escritura.

**Servicios de Bases de Datos:**
**DynamoDB:**
Ya descrito en almacenamiento.

**Servicios de IA:**

**AWS SageMaker:**
Plataforma integral para crear, entrenar y desplegar modelos de machine learning personalizados (para validación de documentos con IA).

**Configuración de Hardware:**
**Entrenamiento del modelo:**
- **Tipos de instancia:** ml.g4dn.xlarge
- **Número de instancias:** 1–4 (según volumen de datos)
- **Tamaño de disco:** mínimo 100 GiB (ajustable)
- **Algoritmo:** OCR + modelo de clasificación
- **Almacenamiento de datos en S3**

**Despliegue del modelo:**
- **Tipo de instancia:** ml.c5.large
- **Modo de despliegue:** Real-time endpoint


**Servicios de Seguridad y Cumplimiento:**
**AWS KMS (Key Management Service):**
Para la administración y protección de claves criptográficas utilizadas para cifrar datos sensibles.

**Configuración de Hardware:** Servicio gestionado, serverless. No requiere configuración de hardware.

**AWS Secrets Manager:**
Gestión segura de claves API, credenciales y tokens, con rotación automática.

**Configuración de Hardware:** Servicio gestionado, serverless. No requiere configuración de hardware.


**Servicios de Gestión y Monitoreo:**
**AWS IAM (Identity and Access Management):**
Gestión de identidades y permisos para usuarios y servicios de AWS.

**Configuración de Hardware:** Servicio gestionado.

**AWS CloudWatch:**
Monitoreo y métricas para toda la infraestructura de AWS.

**Configuración de Hardware:** Servicio gestionado.

**AWS CloudTrail:**
Auditoría de acciones realizadas en la cuenta de AWS.

**Configuración de Hardware:** Servicio gestionado.

**Servicios de Integración y ETL:**
**RabbitMQ (en EKS):**
Broker de mensajería para comunicación asíncrona entre microservicios. Se desplegará como un StatefulSet en EKS.

**Configuración de Hardware:**
- **Tipo de instancia del agente:** mq.m5.large (2 vCPU 8 GB de RAM)
- **Versión del motor del agente:** 3.13
- **Configuración de red:** Acceso privado


**Apache Airflow:**
Orquestador de workflows para automatizar y monitorear procesos ETL con Spark

**Configuración de Hardware:**
- **Versión de Airflow:** 2.10.3 o superior
- **Clase de entorno:** mw1.medium
- **Número mínimo de procesos de trabajo:** 1
- **Número máximo de procesos de trabajo:** 5
- **Número mínimo de servidores web:** 2
- **Número máximo de servidores web:** 3
- **Recuento de programadores:** 3

**AWS Glue:**
Servicio ETL gestionado. Si se utiliza, puede reducir la necesidad de gestionar un clúster de Spark propio en EKS.

**Configuración de Hardware:** Servicio serverless, gestionado por AWS. Se paga por el tiempo de ejecución. No requiere configuración de hardware directa.

##### Microservicios en los Componentes
El proyecto **Portal Data Pura Vida** se estructurará en microservicios, lo que permitirá una mayor flexibilidad, escalabilidad y mantenibilidad. La comunicación entre muchos de estos microservicios será Event-Driven, utilizando RabbitMQ como broker de mensajería para desacoplar los componentes y permitir un procesamiento asíncrono.

**Microservicio: bioreg_auth_svc (Autenticación y Gestión de Usuarios)**

**Descripción:** Maneja el registro, login y la gestión de perfiles de usuario. Interactúa con AWS Cognito para la autenticación y Cognito User Pools para almacenar los datos de usuario.

**Funcionalidad:**
-   Registro de personas físicas y jurídicas.
- Login de usuarios y organizaciones.
- Gestión de perfiles (actualización de datos).
- Asignación y revocación de llaves de seguridad para organizaciones.
- Permite a una persona administrar múltiples organizaciones.

**Herramientas:**
- Python/FastAPI: Para la lógica de la API REST.
- AWS Cognito SDK (Boto3): Para interactuar con Cognito para el registro, autenticación, MFA y gestión de usuarios.
- PostgreSQL (RDS): Para almacenar datos diferenciados según el tipo de entidad (información personal, societaria, legal, tributaria) y la relación entre usuarios y organizaciones.
- DynamoDB: Podría usarse para almacenar configuraciones dinámicas de formularios o metadatos de usuario con alta concurrencia.

**Microservicio: bioreg_doc_validation_svc (Validación Documental con IA)**

**Descripción:** Se encarga de recibir, almacenar y validar los documentos subidos por los usuarios (cédulas, actas, registros tributarios) utilizando inteligencia artificial.

**Funcionalidad:**
- Recepción y almacenamiento seguro de documentos en AWS S3.
- Disparo de flujos de validación automática de documentos mediante IA.
- Marcado de registros como "pendientes" y su posterior aprobación.

**Herramientas:**
- Python/FastAPI: Para exponer una API para la carga de documentos.
- AWS S3 SDK: Para la carga y descarga de documentos.
- AWS SageMaker SDK: Para invocar modelos de Machine Learning desplegados en SageMaker para el análisis de documentos.
- Hugging Face Transformers: Para modelos preentrenados de embeddings semánticos que puedan ayudar en la clasificación y validación de texto en documentos.
- LangChain / OpenAI (GPT-4): Para procesamiento de lenguaje natural y clasificación semántica de texto extraído de documentos.
- RabbitMQ: Event-Driven: Una vez que un documento es cargado en S3, el bioreg_doc_validation_svc podría publicar un evento (document_uploaded) en RabbitMQ. Esto activaría un consumidor que iniciaría el proceso de validación por IA.

**Microservicio: bioreg_kyc_aml_svc (Interacción con SumSub)**
**Descripción:** Gestiona la interacción con el sistema de terceros SumSub para realizar las comprobaciones KYC (Know Your Customer) y AML (Anti-Money Laundering), incluyendo pruebas de vida y biometría.

**Funcionalidad:**
- Envío de datos de usuario y documentos a SumSub.
- Gestión de las respuestas y resultados de SumSub (aprobado/rechazado).
- Integración con el SDK de SumSub para pruebas de vida y biometría.

**Herramientas:**
- Python/FastAPI: Para la lógica de negocio y exposición de endpoints.
- Requests (Python Library): Para hacer llamadas a la API de SumSub.
- AWS Secrets Manager: Para almacenar de forma segura las credenciales de la API de SumSub.
- RabbitMQ: Event-Driven: Tras la validación inicial de documentos, el bioreg_doc_validation_svc podría publicar un evento (document_validated_for_kyc) que el bioreg_kyc_aml_svc consumiría para iniciar el proceso de KYC/AML con SumSub. De manera inversa, los webhooks de SumSub podrían publicar eventos en un endpoint del bioreg_kyc_aml_svc que luego dispararía eventos internos (ej., kyc_aml_status_updated) en RabbitMQ.

**Microservicio: bioreg_ip_whitelist_svc (Gestión de IPs y Restricciones)**
**Descripción:** Gestiona las listas blancas de IP y aplica restricciones de acceso al portal solo desde IPs de Costa Rica.

**Funcionalidad:**
- Almacenar y gestionar IPs institucionales o listas blancas.
- Validar la IP de origen de las solicitudes entrantes.

**Herramientas:**
- Python/FastAPI: Para la lógica de negocio y exposición de endpoints para la gestión de IPs.
- DynamoDB: Para almacenar las listas de IPs permitidas debido a su capacidad de alto rendimiento y baja latencia para búsquedas frecuentes.

**Motor de Transformación (Componente Transversal)**
Este componente se encarga de la transformación, validación y preparación de datos complejos, especialmente en relación con la verificación de completitud y validez de documentos y la generación de claves criptográficas.

**Microservicio: transform_data_merger_svc (Merger de Tablas/Datos)**
**Descripción:** Se encarga de consolidar y transformar datos de diversas fuentes o tablas en una única representación unificada. Por ejemplo, podría fusionar datos de documentos extraídos con información de Cognito y PostgreSQL para crear un perfil completo del usuario/organización.

**Funcionalidad:**
- Lectura de datos de múltiples fuentes (S3, PostgreSQL, DynamoDB).
- Aplicación de lógica de transformación (limpieza, normalización, enriquecimiento).
- Unión y agregación de datos.
- Escritura de los datos transformados.

**Herramientas:**
- Apache Spark (usando PySpark) en EKS: Para el procesamiento distribuido y la transformación de grandes volúmenes de datos. Es ideal para unir N tablas en 1 y aplicar transformaciones complejas.
- Apache Airflow en EKS: Para orquestar los pipelines de Spark. Airflow definiría las dependencias y el orden de ejecución de los trabajos de Spark.
- AWS S3 SDK: Para leer y escribir datos en S3 (data lakes, archivos temporales).
- Event-Driven: Este microservicio podría ser activado por eventos, por ejemplo, un evento (document_validated_and_extracted) publicado por el bioreg_doc_validation_svc que indica que los datos de un documento han sido extraídos y están listos para ser fusionados con otros datos del perfil de usuario. Airflow podría entonces disparar un trabajo de Spark.

**Microservicio: transform_crypto_key_gen_svc (Generación de Claves Criptográficas)**
**Descripción:** Genera claves criptográficas simétricas y asimétricas para cada entidad/persona y gestiona su protección y distribución mediante un sistema de llave tripartita.

**Funcionalidad:**
- Generación segura de pares de claves y claves simétricas.
- División de claves en tres partes.
- Almacenamiento seguro de las partes de la clave.

**Herramientas:**
- Python/FastAPI: Para la lógica de negocio y exposición de endpoints.
- AWS KMS SDK: Para proteger las claves maestras y para operaciones de cifrado/descifrado si se utilizan directamente con KMS. Una parte de la llave tripartita podría ser custodiada por KMS.
- AWS Secrets Manager: Para almacenar de forma segura las partes de las claves (las partes custodiadas por Data Pura Vida).
- Event-Driven: Una vez que un registro de usuario/organización es completamente validado y aprobado, el bioreg_auth_svc o un proceso de Airflow podría publicar un evento (registration_approved_for_key_generation) que este microservicio consumiría para iniciar la generación y distribución de claves.

**Componentes Compartidos**
Estos componentes no son microservicios per se, sino servicios o herramientas que soportan a múltiples microservicios.

**RabbitMQ (en EKS):**
**Descripción:** Broker de mensajería central para la comunicación asíncrona entre microservicios. Permite desacoplar los productores de los consumidores, mejorar la resiliencia y permitir un procesamiento más eficiente de tareas intensivas.
o Uso en Event-Driven: Es el corazón del enfoque Event-Driven. Todos los eventos de negocio (ej., user_registered, document_uploaded, kyc_status_updated, registration_approved) se publicarían como mensajes en colas de RabbitMQ, y los microservicios relevantes consumirían estos mensajes para reaccionar a los cambios de estado.

**Herramientas:** RabbitMQ (desplegado en EKS).

**Apache Spark (en EKS):**
**Descripción:** Framework para procesamiento distribuido. Utilizado principalmente en el "Motor de Transformación" para ETL, validación y transformación de datos a gran escala.

**Uso:** Para el transform_data_merger_svc y para tareas de validación complejas que requieran procesamiento masivo de datos.
**Herramientas:** Spark, clúster de Spark en EKS.

**Apache Airflow:**
**Descripción:** Orquestador de workflows. Automatiza y monitorea los procesos ETL y de validación que involucran a Spark y otros servicios.

**Uso:** Para definir DAGs (Directed Acyclic Graphs) que representan los flujos de datos y procesamiento. Por ejemplo, un DAG podría:
- Detectar nuevos documentos en S3.
- Disparar un trabajo de Spark para extraer datos.
- Esperar la finalización.
- Disparar otro trabajo de Spark para la fusión de datos.
- Notificar al sistema de bioregistro sobre el estado final.

**Herramientas:** Airflow.

***AWS SageMaker:**
**Descripción:** Plataforma para ML. Se utiliza para entrenar y desplegar modelos personalizados de IA para la validación documental.

**Uso:** Como backend para el bioreg_doc_validation_svc para la lógica de IA. Los modelos entrenados se desplegarían como endpoints de inferencia de SageMaker, a los que el microservicio de validación documental haría llamadas.

**Herramientas:** AWS SageMaker Studio, SageMaker Training Jobs, SageMaker Endpoints.

**AWS KMS:**
**Descripción:** Gestión de claves criptográficas. Es un servicio fundamental de seguridad que se integra con otros servicios de AWS para proteger datos.

**Uso:** Para cifrar datos en reposo en S3, RDS, DynamoDB. También, directamente con el transform_crypto_key_gen_svc para la gestión de las partes de las claves criptográficas.

**Herramientas:** AWS KMS API/SDK.

**AWS CloudWatch / Grafana / Prometheus:**
**Descripción:** Herramientas de observabilidad y monitoreo.

**Uso:** Monitorear el rendimiento de los microservicios en EKS, las bases de datos, los trabajos de Spark y Airflow, y los servicios de AWS en general. Las métricas y logs se recopilarán en CloudWatch, y Grafana/Prometheus se usarán para dashboards personalizados.

**Herramientas:** AWS CloudWatch, Grafana, Prometheus (con sus exporters para EKS y servicios).


**AWS SageMaker:**
Plataforma integral para crear, entrenar y desplegar modelos de machine learning personalizados (para validación documental con IA).
