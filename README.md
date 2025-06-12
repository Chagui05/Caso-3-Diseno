# Caso-3-Diseno

## 1. Planeamiento

En esta sección se detallan los aspectos relacionados con la comprensión del problema, la forma en que se dividirá el trabajo dentro del equipo, los hitos en los que se estructura el desarrollo del proyecto y los mecanismos que permitirán evaluar si se está avanzando conforme a lo planificado.

### 1.1 Estructura del Equipo, Stakeholders, Key Players

#### Estructura Interna

El equipo de trabajo consiste de 5 integrantes:

- Santiago Chaves Garbanzo
- Anthony Fuentes
- Luis David Blanco
- Gabriel Gutiérrez
- Jefferson Salas Cordero

Todos tenemos asignaciones distintas dentro del proyecto, pero como vamos a trabajar con metodología Kanban, cualquiera puede hacerse cargo de cualquier tarea. Basta con elegirla en ClickUp y ponerse a trabjar.

Además, una pieza muy importante en el proyecto será Rodrigo Núñez, el cuál actuará como Product Owner de Data Pura Vida, y consultor de diseño de software en caso de que tengamos algún tipo de duda.

#### Stakeholders y Key Players:

Se identificaron los principales actores que influyen o se ven afectados por el desarrollo de la plataforma. A continuación, se presenta una matriz que los muestra:

![matrizstakeholders](img/matriz-stakeholders.png)

Como se puede observar, los principales interesados en que el proyecto avance son el Product Owner y el equipo de trabajo, ya que están comprometidos con lograr que el producto final cumpla con los objetivos planteados desde el inicio.

La población general, aunque no tiene un alto nivel de poder dentro del proyecto, demuestra un gran interés. Una plataforma de este tipo promovería la transparencia en el acceso a datos y aportaría a un Costa Rica con mayor disponibilidad de información para todos (incluso aunque parte del contenido sea privado).

Por otro lado, el actor con mayor poder es el gobierno, al ser quien financia el proyecto. Su interés se considera moderado, posiblemente por cierto escepticismo respecto al impacto que la plataforma podría tener sobre su reputación.

Finalmente, aquellos actores que incurren en prácticas como el lavado de dinero o evasión fiscal son los menos interesados, ya que el sistema ofrecería mayor visibilidad sobre los datos, lo cual podría exponer dichas irregularidades.

Ahora bien, ya que se conocen los stakeholders principales se puede evidenciar que los key players son tanto el Product Owner, como el Equipo de trabajo, ya que serán los encargados de que el proyecto tenga exito.

#### Sistemas y Ecosistemas de Software Existentes:

En Costa Rica no existe ningún sistema ni ecosistema previo que funcione como antecedente directo de Data Pura Vida, por lo que no se anticipan problemas de integración con plataformas existentes. Si bien existen herramientas puntuales, como el API del TSE para consultas por cédula, estas no representan un obstáculo, ya que los requerimientos del proyecto contemplan la capacidad del sistema para aceptar datos provenientes de APIs externas.

### 1.2 Gestión de la Comunicación y Documentación del proyecto

Para la comunicación interna del equipo se utilizará Slack. A través de esta herramienta se coordinará la asignación de tareas en ClickUp, y también se notificará cuando una tarea haya sido finalizada. Antes de marcarla como completada, la tarea deberá pasar al estado de "Esperando Aprobación" en ClickUp, para que Rodrigo pueda revisarla y aprobarla.

Además, se utilizará Discord para realizar al menos una reunión semanal, en la cual se discutirán avances generales del proyecto. En caso de surgir dudas más complejas, se invitará al profesor para que pueda brindar orientación.

La documentación principal del proyecto se mantendrá en el README del repositorio de GitHub Chagui05/Caso-3-Diseno. En ese archivo se incluirán todos los detalles relevantes. Si existieran anexos, como la hoja de requerimientos o la entrevista con el profesor, se agregarán al mismo repositorio en archivos separados con nombres descriptivos, y se hará referencia a ellos desde el README. Toda la documentación será escrita en formato Markdown.

### 1.3 Entendimiento del problema

Para entender adecuadamente el problema, el equipo realizó una entrevista al Product Owner, basada en una serie de preguntas que surgieron tras revisar la especificación del proyecto. Las respuestas obtenidas fueron registradas en el archivo RespuestaEntrevista, y permitieron extraer información clave, como por ejemplo:

- La plataforma debe permitir el registro de personas físicas primero, y luego dar la posibilidad de vincularlas como administradoras de organizaciones.
- La validación de cuentas puede involucrar múltiples métodos: revisión manual, validaciones automatizadas y uso de servicios externos como SumSub.
- La inclusión de IBAN y datos de tarjetas en el registro busca filtrar usuarios no comprometidos y evitar registros superficiales.
- Se recomienda restringir el acceso por IP solo a la sección de registro, o permitir el registro de IPs confiables para quienes estén en el extranjero.
- Los datos cargados (sin importar el origen) deben convertirse a un formato unificado tras aplicar el proceso ETDL (relacional, documental, etc.).
- El sistema debe validar estructura, formato y contenido de los datasets, considerando reglas como formatos de fechas, booleanos y tipos de datos.
- El motor de visualización de dashboards debe permitir a los usuarios crear sus propios paneles, compartirlos y gestionarlos.
- La arquitectura de backend puede ser definida libremente por el equipo (monolítica o microservicios), según convenga al diseño general.
- Se permite la integración con herramientas de IA, siempre que se respeten los criterios de autorización definidos por la administración de la plataforma.
- El portal web de backoffice será administrado por una organización gubernamental registrada dentro del sistema, actuando como custodio de la información.

A partir de esta información, se desarrollaron los siguientes diagramas de flujo que ilustran las tareas clave identificadas dentro del sistema:

- Diagrama de registro:

El siguiente diagrama presenta una visión general del proceso de registro en nuestra plataforma. No incluye detalles técnicos ni especificaciones sobre los campos dinámicos que varían según el tipo de entidad registrada; su objetivo es ilustrar de forma abstracta y comprensible cómo se estructura el flujo de registro dentro del sistema.

![matrizstakeholders](img/entendimientoRegistro.png)

- Diagrama de Ingesta y configuración de un dataset

Subir y configurar un dataset en la plataforma no es nada trivial, por eso se armaron estos dos diagramas que separan el proceso en dos partes.

El primer diagrama muestra cómo se le pide al usuario que suba el dataset: qué datos tiene que dar, qué información se necesita para la IA, y cómo se valida el archivo que subió (formato, estructura, nombres de columnas, etc.).

![matrizstakeholders](img/subidaDataset1.png)

El segundo diagrama arranca una vez que el dataset ya fue validado. Ahí se definen cosas como si el conjunto de datos va a ser público, privado o de pago, y qué métodos de acceso y cobro se van a aplicar.

![matrizstakeholders](img/subidaDataset2.png)

Es importante aclarar que en el diagrama II no se detalla paso a paso lo que hace el motor ETDL, pero sí se deja claro que va a encargarse de tareas como: detectar duplicados, relacionar datos con otros ya cargados, ajustar el modelo según las conexiones que encuentre, y aplicar automáticamente un flujo con extracción, transformación, limpieza, detección de contexto, modelado y carga con ayuda de AI.

#### Componentes del Sistema

Con el fin de lograr una arquitectura modular, segura y mantenible, el sistema se divide en macrocomponentes. Cada uno aborda un conjunto específico de requerimientos funcionales y no funcionales. En esta sección se listan los componentes y sus principales responsabilidades. La implementación técnica y subdivisión de estos se detalla más adelante en el documento.

##### Bioregistro

Este módulo gestiona el proceso de incorporación de personas físicas y jurídicas a la plataforma. Abarca desde el llenado de formularios hasta la validación de identidad y la emisión de credenciales digitales. Debe cumplir con regulaciones AML y estándares avanzados de identidad digital.

Requerimientos:

- El componente debe permitir el registro de personas físicas, jurídicas, instituciones, cámaras, grupos y empresas.
- El formulario de registro debe adaptarse dinámicamente según el tipo de entidad seleccionada.
- El registro de usuarios debe estar asegurado con MFA y biometría, cumpliendo estándares de identidad digital avanzada.
- El componente debe solicitar y capturar información personal, societaria, legal y tributaria según el tipo de entidad.
- El componente debe revisar que cuando se van a asignar personas físicas a la organización al crearla, efectivamente formen parte de dicho conjunto.
- El registro debe pasar por una etapa de validación interna manual para el registro de empresas
- El componente debe implementar validación automática por inteligencia artificial de los documentos subidos.
- El componente debe exigir a los representantes legales el registro como individuos con: identidad digital, biometría, prueba de vida y autenticación multifactor (MFA).
- Cada organización debe recibir llaves de seguridad que le permitan delegar o revocar accesos a sus usuarios.
- Un usuario debe poder administrar múltiples organizaciones desde una única cuenta.
- El componente debe capturar datos preliminares de cuentas IBAN y/o tarjetas de crédito como parte del registro.
- El componente debe enviar una notificación por correo electrónico cuando un registro sea aprobado.
- El componente debe exigir documentos específicos según el tipo de entidad: cédulas físicas o jurídicas, actas, RTN, dirección, etc.
- El componente debe permitir registrar direcciones IP institucionales (listas blancas) para permitir acceso autorizado.
- El componente debe permitir únicamente IPs costarricenses en el registro
- El sistema debe proteger las claves generadas mediante un esquema de llave tripartita, distribuidas entre Data Pura Vida y dos custodios.

##### La Bóveda

La Bóveda es el almacén central de datos del sistema, diseñado para ser seguro, escalable y auditable. Unifica todos los datos cargados, sin importar su formato de origen, y permite relaciones entre datasets. Cifra la información en tránsito y reposo, controla el acceso por roles y entidades, y mantiene trazabilidad completa del uso y movimientos de los datos. Está pensada para soportar millones de registros con alto rendimiento y cumplir estándares de gobierno de datos.

Requerimientos:

- La Bóveda tiene que almacenar los datos en un solo formato, por más de que las fuentes externas sean de distintos tipos (relacionales, documentales, csv, excel)
- La Bóveda debe permitir especificar columnas que relacionan un dataset con otros datasets del ecosistema.
- La Bóveda debe de estar monitoreada en todo momento para detectar movimientos sospechosos, para dar contenido de uso de un dataset, y para asegurar trazabilidad y diagnóstico rápido de fallas.
- Debe ser resiliente, auditable y alineado con estándares de gobierno de datos.
- Debe permitir crecimiento dinámico sin perder eficiencia.
- Debe escalar a millones de registros y miles de usuarios concurrentes.
- Mantener trazabilidad de datos usados, no usados y descartados.
- Todos los datos cargados deben estar protegidos mediante cifrado, incluso frente al personal técnico ("ingenieros de la plataforma").
- Cifrar toda la data en tránsito y en reposo, dejando trazabilidad auditable.
- Permitir almacenamiento masivo de datos estructurados y semiestructurados.
- Controlar accesos lógicos por entidad, usuario o tipo de dato.
- Implementar control de acceso a nivel de rol (RBAC) y a nivel de fila (RLS) o equivalentes.

##### Centro de Carga

Este módulo permite a los usuarios cargar sus datasets a la plataforma. Desde acá pueden definir qué datos desean cifrar, especificar el formato de origen y configurar otros parámetros clave para asegurar que la carga se procese correctamente.

Requerimientos:

- Permitir a los usuarios decidir qué datos compartir dentro del ecosistema.
- Requerir que cada dataset tenga un nombre único.
- Soportar múltiples métodos de carga de datos: archivos Excel, CSV, JSON, APIs y conexiones directas a bases de datos SQL y NoSQL.
- Requerir nombre, descripción y metadata útil para IA sobre las columnas del dataset.
- Permitir configurar los parámetros de conexión de forma cifrada para cada medio de carga.
- Los parámetros de conexión de bases de datos y APIs deben almacenarse de forma cifrada.
- Permitir configurar si el dataset es público o privado, gratuito o pagado, permanente o con disponibilidad temporal.
- El sistema de permisos debe prevenir accesos no autorizados a datasets privados o pagos.
- Asignar permisos de acceso a los datasets privados.
- Permitir definir montos de acceso para datasets con modelo de cobro.
- Restringir acceso a datos por tiempo, volumen o frecuencia de consulta.
- Indicar si la carga es única o recurrente, completa o por deltas.
- Configurar parámetros para carga por deltas: campos diferenciales, frecuencia (timed pull) o mediante callbacks.
- Habilitar control granular de acceso por institución, persona o grupo.

##### Motor de Transformación

Este módulo es clave para garantizar que los datasets se almacenen correctamente en la Bóveda. Se encarga de recibir datos desde distintas fuentes, validar que el formato coincida con el indicado en el formulario de ingesta y, en caso contrario, rechazar la carga. Una vez superada esta validación, aplica todo el proceso de ETDL y mapea los datos al formato interno de la Bóveda.

Requerimientos:

- Validar el formato, estructura y contenido de cada dataset cargado sea correcto, o bien adaptarlo al interno de la Bóveda (formatos de fecha, booleans, etc.).
- Validar el formato, estructura y contenido de cada dataset cargado coincida con lo especificado en el proceso de carga.
- Automatizar el proceso de carga mediante un motor de IA que aplique un flujo ETDL (extracción, transformación, limpieza, detección de contexto, modelado y carga).
- Aplicar IA para normalizar, rediseñar modelos de datos y vincularlos automáticamente.
- Detectar duplicidades, optimizar relaciones y ajustar el modelo de datos automáticamente según las interrelaciones detectadas.
- Monitorear el proceso completo con métricas de transferencia, carga, limpieza, eliminación, modelado, volumen, datos omitidos, datos consultados y tasa de éxito.
- El sistema debe ser capaz de procesar cargas recurrentes y automatizadas sin intervención manual.
- Soportar cargas delta con identificación de cambios.
- Realizar merges eficientes sin pérdida de integridad.

##### Centro de Visualización y Consumo

Este módulo está compuesto por 3 subcomponentes clave:

1. **Generador de dashboards**: permite a los usuarios diseñar y crear gráficos de forma rápida y amigable para visualizar cualquier dataset.

Requerimientos:

- El sistema debe permitir la construcción de dashboards personalizados de forma manual.
- El sistema debe permitir construir dashboards manualmente o mediante prompts inteligentes que generen visualizaciones automáticas.
- El sistema debe permitir representar visualmente los datos en tablas, gráficos, conteos, tendencias y predicciones.
- El sistema debe permitir a los usuarios guardar sus dashboards personalizados.
- El sistema debe permitir compartir dashboards con otros usuarios o hacerlos públicos dentro de la plataforma.
- La interfaz de construcción de dashboards debe ser segura, intuitiva y con capacidad de respuesta en tiempo real.

2. **Visualización y Consumo**: ofrece una interfaz para revisar esas visualizaciones y realizar análisis de datos directamente sobre los dashboards.

Requerimientos:

- El sistema debe permitir visualizar todos los datasets accesibles como una fuente consolidada.
- El sistema debe bloquear toda exportación directa de datos y gráficos desde el portal.
- El sistema debe mostrar datos de forma preliminar en modo de construcción de dashboard y luego con datos reales al ejecutar consultas
- El sistema debe deshabilitar temporalmente el acceso a datasets cuando se superen los límites de consumo.
- El sistema debe registrar todas las transacciones y consumos de datos en un historial accesible para cada usuario.
- El sistema debe mostrar métricas de uso: volumen de datos consultados, número de consultas realizadas, tiempo restante o límites alcanzados.
- El sistema no debe permitir en ningún momento la descarga directa de datasets o gráficos generados.
- La visualización de datos debe realizarse exclusivamente dentro del portal, sin opciones de exportación, captura o embedding externo.
- Los límites de consumo deben aplicarse en tiempo real, sin permitir bypasses o reintentos abusivos.

3. **Consumo para IA**: Este subcomponente es el regulador de consumo de IA, define límites y los métodos de ingesta disponibles desde el sistema para los usuarios.

Requerimientos:

- El sistema debe permitir el acceso sistema a sistema únicamente para alimentar modelos de IA aprobados.
- La entrega de datos para modelos de IA debe ser monitoreada, registrada y limitada a contextos aprobados explícitamente por Data Pura Vida.
- El sistema debe ofrecer plataformas limitadas y controladas para esta alimentación de IA. Solo permitirá 2 por usuario.
- El sistema debe minimizar al máximo el riesgo de descargas indirectas mediante presunción de uso en IA.
- Los datos deben ser envíados en un formato que no permita poder ser desencriptado para otro uso que no sea alimentar IA (por ejemplo uso de embeddings).

##### Marketplace

Este módulo está enfocado en ofrecer una interfaz amigable que permita a los usuarios encontrar datasets de forma eficiente, con descripciones claras y navegación fluida. Además, incluye una sección adicional para buscar dashboards creados por otros usuarios, facilitando el descubrimiento y reutilización de visualizaciones dentro de la plataforma.

Requerimientos:

- La experiencia de compra de datasets debe ser fluida, transparente y accesible desde los dashboards personales.
- Incluir un módulo de compra donde se visualicen datasets disponibles bajo acceso pagado.
- Permitir seleccionar un dataset, visualizar precio, términos de uso, duración del acceso y condiciones de cobro.
- Soportar múltiples métodos de pago: tarjeta de crédito, débito y otros mecanismos nacionales compatibles.
- Mostrar confirmaciones de transacción y activar el acceso según condiciones (tiempo, volumen, frecuencia).
- El sistema debe mostrar opciones para renovar o ampliar los paquetes de acceso en caso de superar el límite.

##### Backoffice Administrativo

Este módulo concentra las herramientas de backoffice necesarias para la gestión integral de la plataforma. Su enfoque está en el control, la seguridad, la gobernanza de datos y la trazabilidad completa de las operaciones.

Requerimientos:

- Administrar usuarios: validación de identidad, membresía y roles.
- Gestionar reglas de carga de datos (formatos, estructuras, validaciones).
- Configurar conexiones externas (APIs, BDs, callbacks).
- Activar, desactivar y supervisar objetos de datos, pipelines y flujos.
- Revocar o regenerar llaves de seguridad (simétricas, asimétricas, tri-partitas).
- Administrar custodios de llaves y flujos de confirmación mancomunada.
- Auditar operaciones por usuario, fecha, acción y resultado.
- Generar reportes de uso, calidad, integración y anomalías.
- Monitorear el estado operativo de servicios y tareas.
- Extraer evidencias para procesos legales bajo autorización.
- Gestionar permisos y accesos mediante RBAC.
- Debe ofrecer una interfaz robusta y segura solo para personal autorizado.
- Debe permitir gestión flexible pero estricta de accesos y configuraciones.

#### Prototipado

Se desarrolló un prototipo funcional de la página del Bioregistro Verde con el objetivo principal de probar el comportamiento de los formularios dinámicos. Este prototipo no incluye procesos de prueba de vida ni captura de datos biométricos, y tampoco recolecta la información final que se almacenará en el sistema definitivo. Su propósito es demostrar, a alto nivel, cómo el formulario se adapta dinámicamente según las selecciones del usuario.

A continuación las imágenes del flujo de recolección de data de una persona física:

![alt text](img/userReg0.png)

![alt text](img/userReg1.png)

![alt text](img/userReg2.png)

![alt text](img/userReg3.png)

Además, se adjunta el proceso de registar compañía pública:

![alt text](img/orgPub0.png)
![alt text](img/orgPub1.png)
![alt text](img/orgPub2.png)
![alt text](img/orgPub3.png)
![alt text](img/orgPub4.png)
![alt text](img/orgPub5.png)

Si deseá probar el prototipo visite el siguiente [link](https://gentle-signup-wizard.lovable.app/).

### 1.4 Customer Journeys

Este Service Blueprint representa el recorrido completo de un ciudadano dentro del ecosistema Data Pura Vida, desde el descubrimiento de la plataforma hasta la creación, publicación y monitoreo de un dashboard personalizado con datos públicos.

El diagrama detalla no solo las acciones del usuario, sino también los touchpoints del sistema, los procesos internos (backstage) y las herramientas de soporte involucradas en cada etapa. Además, se integran las emociones del usuario para identificar oportunidades de mejora en la experiencia.

Las líneas de interacción, visibilidad e interacción interna permiten visualizar claramente los límites entre lo que el ciudadano ve, lo que ocurre detrás del sistema y las herramientas tecnológicas que lo sustentan.

Este blueprint se organiza en **seis** fases principales:

1. Conciencia: El ciudadano conoce la existencia de la plataforma.

2. Ingreso: Accede y se autentica de forma segura.

3. Exploración: Navega los datasets disponibles.

4. Creación: Construye un dashboard visual con datos abiertos.

5. Publicación: Comparte su dashboard con otros usuarios.

6. Monitoreo: Consulta métricas de visualización y uso.b

![alt text](img/journey1.png)

Este Service Blueprint representa el recorrido completo de una empresa dentro del ecosistema Data Pura Vida, desde el descubrimiento de la plataforma hasta la publicación y monitoreo de un dataset privado con fines de monetización.

Este blueprint se organiza en siete fases principales:

1. Conciencia: La empresa conoce la plataforma y sus posibilidades de monetización.

2. Registro: Se registra como entidad jurídica mediante un proceso validado.

3. Carga de datos: Sube su dataset en formatos compatibles como archivos o APIs.

4. Configuración: Define permisos, privacidad, cifrado y condiciones de acceso.

5. Validación de valor: Evalúa la calidad y el potencial del dataset con ayuda de IA.

6. Publicación: Hace público el dataset con opciones de pago o acceso controlado.

7. Monitoreo: Supervisa ingresos, visualizaciones y transacciones en tiempo real.

![alt text](img/JourneyIP.png)

**Fases principales:**

1. Registro: Un representante oficial crea una cuenta institucional y sube los documentos requeridos.
2. Validación: La plataforma aplica validaciones automáticas y manuales con ayuda de IA.
3. Configuración: La institución decide qué datos compartir y con qué restricciones.
4. Carga: Se conecta una base de datos externa para carga automatizada.
5. Publicación: El dataset queda disponible para actores autorizados mediante pago.
6. Seguimiento: La institución consulta métricas de acceso y consumo.

![alt text](img/journey2.png)

### 1.5 Plan de ejecución del proyecto

#### Plan de Diseño

El proyecto se estructura en cinco hitos principales que marcarán su progreso:

- Planeamiento del Proyecto
- Supuestos del Proyecto
- Stack Tecnológico
- Diseño de los Componentes
- Validación de los requerimientos

Cada uno de estos hitos cuenta con un plazo definido para su ejecución, lo cual se puede observar en el siguiente diagrama de Gantt:

![gantt](img/gantt.png)

Dentro de cada hito se contemplan varias tareas. Cada integrante del equipo debe seleccionar una tarea según su disponibilidad. Un hito se considera finalizado únicamente cuando todas sus tareas han sido completadas y se encuentran en el tablero de completado en ClickUp.

Además, como se indicó anteriormente, se realizarán reuniones semanales para verificar que el proyecto avance conforme al plan establecido.

Además, como se dijo previamente, se harán reuniones semanales para verificar que el proyecto se esté realizando según lo dice el plan.

#### Plan de Ejecución para Desarrolladores

Este plan indica cómo avanzar progresivamente en la construcción del sistema, desde preparar el entorno hasta desplegar y probar los módulos principales. No detalla cómo funciona cada módulo, sino cómo se implementan y conectan entre sí, con sus respectivos entregables por etapa.

##### 1. Preparación del Entorno de Desarrollo

**Objetivo:** Sentar las bases para que todo el equipo trabaje de forma coordinada, segura y replicable.

**Actividades:**

- Establecer repositorio con control de versiones.
- Configurar ambientes separados para desarrollo, pruebas y producción.
- Montar infraestructura local (contenedores, redes internas, secretos).
- Habilitar flujos básicos de CI/CD y documentación técnica inicial.

**Entregables:**

- Repositorio con estructura base.
- Manual de instalación local y buenas prácticas.
- Plantilla de CI/CD con al menos una validación básica.
- Ambiente de desarrollo replicable con un comando (ej. Docker Compose).

##### 2. Implementación del Bioregistro

**Objetivo:** Habilitar la incorporación de personas físicas y jurídicas a la plataforma.

**Actividades:**

- Crear formulario de registro adaptativo por tipo de entidad.
- Implementar simulaciones de validación automática y revisión manual.
- Gestionar jerarquías usuario–organización y generación de llaves.
- Activar sistema de notificaciones y control geográfico básico.

**Entregables:**

- Flujo funcional de registro completo.
- Formulario con lógica adaptativa por entidad.
- Simulación de validaciones automáticas y manuales.
- Sistema de emisión de llaves y notificación por correo.

##### 3. Habilitar el Centro de Carga de Datos

**Objetivo:** Permitir a los usuarios cargar datasets desde distintas fuentes.

**Actividades:**

- Desarrollar interfaz de carga de archivos (CSV, Excel, JSON).
- Capturar metadatos básicos (nombre, descripción, privacidad, etc.).
- Simular conexión con bases de datos externas.
- Almacenar cargas en espacio temporal con trazabilidad.

**Entregables:**

- Módulo de carga funcional con validaciones mínimas.
- Interfaz para configuración de metadatos y privacidad.
- Log de cargas realizadas para trazabilidad.
- Cargas almacenadas provisionalmente.

##### 4. Desarrollar el Motor de Transformación

**Objetivo:** Procesar los datos cargados, limpiarlos y convertirlos a un formato interno.

**Actividades:**

- Validar estructura y contenido de cada carga.
- Aplicar lógica básica de transformación (normalización, fechas, duplicados).
- Generar versiones limpias de los datos.
- Conectar a almacenamiento de datos validado (La Bóveda).

**Entregables:**

- Flujo de transformación activo con trazabilidad.
- Reportes de validación y errores por dataset.
- Datos transformados almacenados de forma estructurada.
- Métricas básicas del proceso (tiempo, éxito, errores).

##### 5. Configurar La Bóveda

**Objetivo:** Consolidar y proteger los datos procesados para su consumo posterior.

**Actividades:**

- Crear repositorio único para los datasets internos.
- Implementar segmentación de acceso por rol, entidad y tipo de dato.
- Establecer cifrado básico en tránsito y reposo.
- Documentar relaciones entre datasets si aplica.

**Entregables:**

- Sistema de almacenamiento central con control de accesos.
- Datasets organizados y protegidos.
- Trazabilidad de acceso a cada dataset.
- Esquema inicial de relaciones entre datasets (si corresponde).

##### 6. Activar la Visualización y los Dashboards

**Objetivo:** Permitir a los usuarios explorar datos mediante gráficos sin exportarlos.

**Actividades:**

- Crear constructor básico de dashboards con tablas y gráficos.
- Activar vistas previas con datos ficticios y reales.
- Controlar consumo (frecuencia, volumen, consultas).
- Habilitar compartir dashboards con otros usuarios.

**Entregables:**

- Módulo visual con constructor de dashboards funcional.
- Dashboards guardables y compartibles.
- Lógica de límites de uso aplicada.
- Registro de interacciones y consultas realizadas.

##### 7. Simular el Consumo para Modelos de IA

**Objetivo:** Simular acceso regulado a datasets por sistemas externos autorizados.

**Actividades:**

- Definir reglas de uso y límites por usuario y contexto.
- Habilitar endpoints simulados para "entrenamiento" de IA.
- Registrar y auditar cada consulta o consumo.
- Aplicar restricciones estrictas para evitar abuso.

**Entregables:**

- API simulada para consumo por IA.
- Sistema de seguimiento y límites aplicado.
- Log de accesos con usuario, contexto y volumen consultado.
- Validación de cumplimiento de reglas definidas.

##### 8. Prototipar el Marketplace de Datos

**Objetivo:** Permitir explorar, adquirir y acceder a datasets bajo condiciones.

**Actividades:**

- Crear buscador y navegador de datasets públicos y pagos.
- Mostrar precios, términos y opciones de compra.
- Simular proceso de adquisición y activación de accesos.
- Gestionar historial de compras y permisos vigentes.

**Entregables:**

- Interfaz funcional del marketplace.
- Flujo de compra simulado con activación de acceso.
- Historial de transacciones por usuario.
- Permisos temporales aplicados tras cada compra.

##### 9. Activar el Backoffice Administrativo

**Objetivo:** Brindar herramientas de gestión y supervisión al equipo administrador.

**Actividades:**

- Crear panel seguro para personal autorizado.
- Visualizar registros, cargas y actividad por componente.
- Permitir aprobación/rechazo de registros y cargas.
- Generar reportes y estadísticas de uso.

**Entregables:**

- Panel de administración con control de usuarios y datos.
- Visualización de actividad y estado del sistema.
- Herramientas para revisión y auditoría básica.
- Generación de reportes automáticos.

##### 10. Pruebas Integradas y Simulación de Casos Reales

**Objetivo:** Asegurar que todo funcione de forma integrada.

**Actividades:**

- Simular flujos completos: registro → carga → transformación → consumo.
- Usar casos reales o sintéticos para testear extremos del sistema.
- Validar reglas de permisos, límites y visualización.
- Documentar fallos, mejoras y tiempos de respuesta.

**Entregables:**

- Casos de prueba documentados.
- Resultados de pruebas con observaciones.
- Validación de flujos completos con usuarios simulados.
- Lista de bugs o ajustes para corregir.

##### 11. Despliegue Controlado y Evaluación

**Objetivo:** Publicar la plataforma en un entorno accesible para validación final.

**Actividades:**

- Preparar un entorno de pruebas compartido (local o nube).
- Desplegar todos los módulos de forma conectada.
- Habilitar usuarios de prueba para feedback externo.
- Preparar una demo pública o privada para presentación.

**Entregables:**

- Versión desplegada en entorno de pruebas.
- Acceso limitado para usuarios externos (testers/docentes).
- Feedback recolectado para iteración.
- Material de presentación o demo funcional lista.

### 1.6 WBS del sistema

Como parte del análisis inicial del sistema **Data Pura Vida**, se realizó una descomposición de alto nivel para identificar los límites del sistema y los actores involucrados. A continuación, se presenta el diagrama de contexto basado en las técnicas descritas para la identificación del sistema y sus límites:

![Work Breakdown Structure](img/WorkBreakdownStructure.jpg)

Esta representación facilita el entendimiento general del sistema y servirá como base para la posterior descomposición en subsistemas, componentes funcionales y diseño arquitectónico detallado.

#### Propósito del diagrama

- **Identificación de límites del sistema:** El diagrama establece una frontera clara entre lo que está dentro y fuera del alcance del desarrollo, lo cual es crucial para evitar ambigüedades durante el diseño detallado.

- **Visualización de los actores externos:** Permite entender quiénes interactúan con el sistema y con qué propósito.

- **Detección de puntos de integración:** Ayuda a anticipar necesidades de interoperabilidad, seguridad, formatos de intercambio de datos y protocolos de comunicación.

#### Consideraciones adicionales

Este diagrama será utilizado como punto de partida para:

- La descomposición en subsistemas o módulos funcionales, agrupando responsabilidades afines.

- La definición de casos de uso y escenarios de interacción.

- La elaboración de la arquitectura técnica, donde se identificarán servicios, componentes y flujos de datos internos.

En resumen, este modelo de contexto es una herramienta clave para asegurar un entendimiento compartido del dominio del problema y sentar las bases de una solución técnica coherente, escalable y alineada con los objetivos del proyecto.

### 1.7 Evaluación de Riesgos

#### Metodología ISO 31000

La evaluación de riesgos sigue los principios de **ISO 31000** para la gestión de riesgos del proyecto Data Pura Vida.

#### Marco de Evaluación:

La evaluación de riesgos utiliza una matriz de probabilidad versus impacto basada en criterios específicos del proyecto Data Pura Vida y su contexto de diseño de sistemas complejos.

#### Escala de probabilidad:

- Muy Alta (100%) : Es prácticamente seguro que el riesgo ocurrirá durante el proyecto (9 de cada 10 proyectos similares)
- Alta (80%) : Es muy probable que el riesgo se materialice (7-8 de cada 10 casos)
- Medios (60%) : Hay una posibilidad moderada de que ocurra (5-6 de cada 10 casos)
- Baja (40%) : Es poco probable pero posible que suceda (3-4 de cada 10 casos)
- Muy Baja (20%) : Es muy poco probable que se materialice (1-2 de cada 10 casos)

#### Escala de Impacto:

- Muy Alto (100%) : Falla completa del proyecto, rediseño total necesario, o retraso superior a 4 semanas
- Alto (80%) : Compromete objetivos principales del proyecto, retraso de 2-4 semanas, o afecta múltiples componentes críticos
- Medio (60%) : Afecta la calidad del diseño o genera retraso de 1-2 semanas, requiere trabajo adicional significativo
- Bajo (40%) : Impacto menor en cronograma (3-7 días) o calidad, se puede resolver con ajustes menores
- Muy Bajo (20%) : Impacto mínimo (menos de 3 días), no afecta objetivos principales del proyecto

#### Riesgos para el Diseño de Data Pura Vida

| ID      | Categoría         | Riesgo                                               | Descripción Detallada                                                                                                                                                                           | Probabilidad        | Impacto             | Clasificación   | Estrategia     | Plan de Respuesta                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------- | ----------------- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------------- | --------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **R01** | **Diseño**        | **Complejidad arquitectónica del ecosistema**        | Diseñar una arquitectura que integre efectivamente portal web, API backend, datalake, backoffice y múltiples sistemas de seguridad requiere experiencia en arquitecturas distribuidas complejas | **Muy Alta (100%)** | **Muy Alto (100%)** | **🔴 EXTREMO**  | **MITIGAR**    | **Prevención:** Definir máximo 5 patrones arquitectónicos (Semana 1), crear ADRs (Architecture Decision Records) para cada decisión, revisión arquitectónica obligatoria cada viernes 1h con validación técnica<br>**Contingencia:** Crear spike de 16h para diseñar arquitectura simplificada (3 capas: Frontend-API-Data), eliminar microservicios y usar monolito modular, reducir integraciones complejas a APIs REST estándar |
| **R02** | **Alcance**       | **Subestimación del alcance del diseño**             | El tiempo asignado puede ser insuficiente para diseñar completamente todos los componentes técnicos con el nivel de detalle requerido para un sistema de esta magnitud                          | **Muy Alta (100%)** | **Medio (60%)**     | **🟠 ALTO**     | **MITIGAR**    | **Prevención:** Planning Poker diario 30min, re-estimación miércoles, time tracking obligatorio en ClickUp, descomponer tareas en máximo 8h cada una<br>**Contingencia:** Si desvío > 150% en 3 tareas: reducir nivel de detalle en diagramas de secuencia (de completos a conceptuales), simplificar especificaciones APIs (menos endpoints), priorizar componentes críticos primero, redistribuir trabajo en 1 día               |
| **R03** | **Documentación** | **Inconsistencias en la documentación técnica**      | Generar documentación técnica coherente entre arquitectura de alto nivel, especificaciones de APIs, modelos de datos, diagramas de seguridad y patrones de integración                          | **Alta (80%)**      | **Alto (80%)**      | **🟠 ALTO**     | **MITIGAR**    | **Prevención:** Templates estándar GitHub, peer review obligatorio, checklist calidad por componente<br>**Contingencia:** Auditoría documental semanal viernes 2h, refactoring inmediato de documentos inconsistentes, responsable: Santiago Chaves                                                                                                                                                                                |
| **R04** | **Tiempo**        | **Cronograma optimista para la complejidad**         | El tiempo asignado puede ser insuficiente para diseñar completamente todos los componentes técnicos con el nivel de detalle requerido para un sistema de esta magnitud                          | **Muy Alta (100%)** | **Medio (60%)**     | **🟠 ALTO**     | **MITIGAR**    | **Prevención:** Re-estimación semanal con burndown charts, escalación automática si > 20% desvío, buffer de 2 días por semana<br>**Contingencia:** Redistribuir tareas inmediatamente, asignar 2 personas a componentes críticos (Bio Registro y La Bóveda), reducir documentación detallada a documentación funcional, completar diseño básico de todos los componentes                                                           |
| **R05** | **Técnico**       | **Complejidad del motor de transformación**                | Especificar técnicamente un motor que procese automáticamente múltiples formatos, detecte duplicados, relacione datos y aplique transformaciones inteligentes es altamente complejo             | **Media (60%)**     | **Muy Alto (100%)** | **🟠 ALTO**     | **MITIGAR**    | **Prevención:** Spike 16h Apache Spark + PySpark (Luis David), prototipo 3 casos (CSV→PostgreSQL, JSON→S3, API→DynamoDB), validar 10MB en <30min<br>**Contingencia:** Motor simplificado con AWS Glue + transformaciones predefinidas, o integración Talend Open Studio (setup 1 semana)                                                                                                                                           |
| **R06** | **Seguridad**     | **Diseño de sistema de cifrado tripartito**          | Especificar correctamente un sistema de llaves criptográficas divididas entre tres custodios, incluyendo protocolos de recuperación y validación mancomunada                                    | **Baja (40%)**      | **Muy Alto (100%)** | **🟠 ALTO**     | **TRANSFERIR** | **Prevención:** Consulta expertos criptografía (8h consultoría), documentar estándares FIPS 140-2, validación externa con especialista<br>**Contingencia:** Implementar cifrado HSM tradicional AWS KMS, esquema dual en lugar de tripartito, mantiene seguridad pero reduce complejidad                                                                                                                                           |
| **R07** | **Integración**   | **Interfaces entre componentes mal definidas**       | Riesgo de que las especificaciones de APIs, contratos de datos y protocolos de comunicación entre portal, backend y datalake no sean completamente compatibles                                  | **Media (60%)**     | **Alto (80%)**      | **🟠 ALTO**     | **MITIGAR**    | **Prevención:** Contratos OpenAPI 3.0 obligatorios, reuniones sync bi-semanales martes/viernes, diagramas de secuencia por flujo<br>**Contingencia:** Workshop alineación 4h si incompatibilidades detectadas, rediseño contratos en 2 días, validación cruzada inmediata                                                                                                                                                          |
| **R08** | **Escalabilidad** | **Arquitectura no preparada para la carga esperada** | El diseño puede no contemplar adecuadamente el manejo de millones de registros, miles de usuarios concurrentes y procesamiento de grandes volúmenes de datos                                    | **Baja (40%)**      | **Medio (60%)**     | **🟡 MODERADO** | **MITIGAR**    | **Prevención:** Definir límites técnicos concretos por componente (Bio Registro: 100 req/min, La Bóveda: 10GB/día), especificar patrones de escalabilidad (load balancers, auto-scaling), calcular capacidad mínima requerida<br>**Contingencia:** Rediseñar arquitectura con clustering activo/pasivo, implementar sharding en diseño de BD, especificar CDN y caching layers, definir estrategia de particionamiento horizontal  |
| **R09** | **Recursos**      | **Disponibilidad limitada del Product Owner**        | El Product Owner puede no estar disponible para validar decisiones arquitectónicas críticas o para resolver ambigüedades en los requerimientos técnicos                                         | **Media (60%)**     | **Bajo (40%)**      | **🟡 MODERADO** | **ACEPTAR**    | **Prevención:** Agenda fija martes/viernes, decisiones escritas en Slack, timeboxing 24h para respuestas<br>**Contingencia:** Escalación a stakeholders si > 48h sin respuesta, decisiones técnicas por equipo con validación posterior, documentar en GitHub para trazabilidad                                                                                                                                                    |
| **R10** | **Coordinación**  | **Diseños de componentes desconectados**             | Los diferentes integrantes del equipo pueden diseñar sus componentes sin suficiente coordinación, resultando en interfaces incompatibles o duplicación de funcionalidades                       | **Media (60%)**     | **Medio (60%)**     | **🟡 MODERADO** | **MITIGAR**    | **Prevención:** Sincronización semanal viernes 1h, documentación centralizada GitHub, daily stand-ups 15min<br>**Contingencia:** Workshop alineación medio día si interfaces incompatibles, rediseño coordinado 3 días máximo, matriz de dependencias actualizada                                                                                                                                                                  |

### 1.8 Definición de KPIs

#### KPIs por Hito del Proyecto

##### Hito 1: Planeamiento del Proyecto

**Período**: 18-22 Mayo 2025 (Semana W20)

| KPI                              | Métrica                            | Objetivo | Método de Recolección                              |
| -------------------------------- | ---------------------------------- | -------- | -------------------------------------------------- |
| **Cumplimiento de cronograma**   | % de tareas completadas a tiempo   | 100%     | ClickUp - estado de tareas vs. fechas planificadas |
| **Completitud de documentación** | % de entregables documentados      | 100%     | Revisión de README y archivos en GitHub            |
| **Participación del equipo**     | % de integrantes activos en tareas | 100%     | ClickUp - asignación y progreso de tareas          |
| **Validación del Product Owner** | % de entregables aprobados         | 100%     | Estado "Aprobado" en ClickUp                       |

##### Hito 2: Supuestos del Proyecto

**Período**: 25-31 Mayo 2025 (Semana W21)

| KPI                            | Métrica                              | Objetivo | Método de Recolección                            |
| ------------------------------ | ------------------------------------ | -------- | ------------------------------------------------ |
| **Cumplimiento de cronograma** | % de tareas completadas a tiempo     | 100%     | ClickUp - comparación fecha planificada vs. real |
| **Calidad de supuestos**       | Número de supuestos validados con PO | 100%     | Documentación de validaciones en Slack/GitHub    |
| **Identificación de riesgos**  | Número de riesgos documentados       | ≥10      | Matriz de riesgos actualizada                    |

##### Hito 3: Stack Tecnológico

**Período**: 1-7 Junio 2025 (Semana W22)

| KPI                               | Métrica                                       | Objetivo | Método de Recolección                        |
| --------------------------------- | --------------------------------------------- | -------- | -------------------------------------------- |
| **Cumplimiento de cronograma**    | % de tareas completadas a tiempo              | 100%     | ClickUp - estado vs. cronograma              |
| **Decisiones tecnológicas**       | % de tecnologías seleccionadas y justificadas | 100%     | Documentación técnica en GitHub              |
| **Factibilidad técnica**          | Prototipos de concepto funcionando            | ≥2       | Repositorio con ejemplos funcionales         |
| **Compatibilidad con requisitos** | % de requisitos cubiertos por stack           | 100%     | Matriz de trazabilidad requisitos-tecnología |

##### Hito 4: Diseño de los Componentes

**Período**: 8-14 Junio 2025 (Semana W23)

| KPI                               | Métrica                                   | Objetivo | Método de Recolección                 |
| --------------------------------- | ----------------------------------------- | -------- | ------------------------------------- |
| **Cumplimiento de cronograma**    | % de tareas completadas a tiempo          | 100%     | ClickUp - seguimiento diario          |
| **Cobertura de componentes**      | % de componentes diseñados vs. requeridos | 100%     | Documentación de arquitectura         |
| **Calidad del diseño**            | Revisiones aprobadas por PO               | 100%     | Estados de aprobación en ClickUp      |
| **Integración entre componentes** | % de interfaces definidas                 | 100%     | Diagramas de integración documentados |

##### Hito 5: Validación de los Requerimientos

**Período**: 15-21 Junio 2025 (Semana W24)

| KPI                            | Métrica                           | Objetivo | Método de Recolección             |
| ------------------------------ | --------------------------------- | -------- | --------------------------------- |
| **Cumplimiento de cronograma** | Entrega a tiempo                  | 100%     | Fecha de entrega final            |
| **Cobertura de requisitos**    | % de requisitos validados         | 100%     | Matriz de trazabilidad completa   |
| **Calidad de documentación**   | Checklist de atributos completado | 100%     | Revisión contra checklist oficial |
| **Aprobación final**           | Validación del Product Owner      | 100%     | Confirmación formal de aceptación |

#### KPIs Transversales del Proyecto

##### Gestión y Comunicación

| KPI                         | Métrica                        | Objetivo | Frecuencia de Medición |
| --------------------------- | ------------------------------ | -------- | ---------------------- |
| **Comunicación efectiva**   | Respuestas en Slack < 24h      | 90%      | Semanal                |
| **Reuniones semanales**     | Asistencia a reuniones         | 100%     | Semanal                |
| **Actualización de tareas** | Tareas actualizadas en ClickUp | Diario   | Diario                 |
| **Resolución de bloqueos**  | Tiempo promedio de resolución  | <48h     | Semanal                |

##### Calidad y Riesgos

| KPI                        | Métrica                             | Objetivo | Frecuencia de Medición |
| -------------------------- | ----------------------------------- | -------- | ---------------------- |
| **Gestión de riesgos**     | % de riesgos con plan de mitigación | 100%     | Semanal                |
| **Incidencias críticas**   | Número de riesgos materializados    | 0        | Semanal                |
| **Calidad de entregables** | % de entregables sin retrabajos     | 90%      | Por hito               |

#### Mecanismos de Recolección y Cálculo

##### Herramientas de Monitoreo

1. **ClickUp**: Seguimiento automático de tareas, tiempos y estados
2. **Slack**: Métricas de comunicación y tiempo de respuesta
3. **GitHub**: Commits, documentación y versiones
4. **Reuniones semanales**: Revisión manual de KPIs y ajustes


## 2. Supuestos del proyecto

### 2.1 Estándares y Regulaciones

Para el proyecto "Data Pura Vida", la revisión de estándares y regulaciones nacionales e internacionales es crucial para garantizar la legalidad, seguridad, privacidad y gobernanza de los datos. A continuación, se detalla la relevancia de cada una de las normativas mencionadas y cómo se aplican a los requerimientos de la plataforma:

#### 1. Ley 8968 (Costa Rica) - Ley de Protección de la Persona frente al Tratamiento de sus Datos Personales

Esta es la normativa nacional fundamental que rige la protección de datos personales en Costa Rica. "Data Pura Vida" debe cumplir íntegramente con sus disposiciones, dado que el sistema manejará una gran cantidad de datos personales de personas físicas y jurídicas.

##### Aplicación a los Requerimientos de la Plataforma:

##### Bioregistro:

##### ARTÍCULO 5.- Principio de consentimiento informado:\*\*REST, GraphQL,

El principio del consentimiento de información se regie por dos puntos importantes, a continuación, se mencionan los dos puntos y su aplicación dentro de la plataforma:

**Punto 1 - Obligación de informar**
Durante el proceso de registro en **Bio Registro Verde**, el sistema debe presentar de forma destacada y fácil de entender la siguiente información:

- La existencia de la base de datos **Data Pura Vida**.

- La finalidad clara de la recolección de datos (ej. validar identidad para operar en el ecosistema, permitir compartir/consumir datos, etc.).

- Los destinatarios de los datos (ej. otros usuarios del ecosistema con los que el usuario decida compartir, la administración de "Data Pura Vida").

- La obligatoriedad de ciertos datos (ej. cédula, información tributaria) y las consecuencias de no proporcionarlos (ej. imposibilidad de completar el registro o acceder a ciertas funcionalidades).

- Los derechos ARCO (Acceso, Rectificación, Cancelación y Oposición) y cómo ejercerlos dentro del portal. Esta información debe estar disponible antes de que el usuario envíe sus datos.

  **Punto 2 - Otorgamiento del consentimiento**
  El consentimiento para el tratamiento de datos debe ser expreso. "Bio Registro Verde" debe implementar un mecanismo de aceptación clara y explícita, como:

- Un checkbox de "Acepto los Términos y Condiciones y la Política de Privacidad" que el usuario debe marcar activamente.

- La documentación de este consentimiento debe almacenarse de forma segura, vinculada al registro del usuario.

- La autenticación avanzada (identidad digital, biometría, prueba de vida, MFA) y la validación documental automatizada por IA refuerzan la seguridad del proceso de consentimiento, asegurando que la persona que da el consentimiento es quien dice ser.

##### ARTÍCULOS 6 y 7 - Principio de calidad de la información; y Derechos que le asisten a la persona( Derechos ARCO ):

Estos principios garantizan que los datos sean apropiados y que los usuarios mantengan el control sobre su información.

**Aplicación a la Plataforma:**

Los datos solicitados (información personal, societaria, legal y tributaria) deben ser estrictamente necesarios y pertinentes para la creación y operación de una cuenta dentro del ecosistema **Data Pura Vida**.

La implementación de IA para verificar la completitud y validez de los documentos subidos (cédulas, actas, registros tributarios) es clave para asegurar la veracidad y exactitud de los datos, cumpliendo con el Artículo 6 (Principio de Calidad de la Información). Esto también ayuda a evitar la recolección de datos fraudulentos.

El portal debe ofrecer mecanismos claros y accesibles para que los usuarios puedan acceder, rectificar o solicitar la eliminación de sus datos personales, directamente desde su perfil o mediante un proceso de solicitud documentado, en cumplimiento con el Artículo 7 (Derechos ARCO). Esto incluye la posibilidad de actualizar información o cerrar cuentas.

##### ARTÍCULO 9 - Categorías particulares de los datos:

Aunque los requerimientos actuales del "Bio Registro Verde" no mencionan explícitamente la recolección de "datos sensibles" (como salud, origen racial, etc.), si el alcance de la plataforma evolucionara para incluirlos, "Data Pura Vida" deberá implementar garantías adicionales y obtener un consentimiento aún más explícito y específico para el tratamiento de estas categorías, según lo exige el Artículo 9 (Datos Sensibles).

##### ARTÍCULO 10 - Seguridad de los Datos:

Este artículo impone la obligación de proteger los datos de carácter personal y evitar su alteración, destrucción accidental o ilícita, pérdida, tratamiento o acceso no autorizado, así como cualquier otra acción contraria a esta ley al responsable de la base de datos.

Los requerimientos de seguridad del **Bioregistro** son una respuesta directa al Artículo 10 ( Seguridad de los datos):

- El uso de autenticación avanzada (identidad digital, biometría, prueba de vida, MFA) son medidas de seguridad lógicas para controlar el acceso.

- La asignación y protección de llaves de seguridad criptográficas (simétricas y asimétricas), incluyendo el sistema de llave tripartita, son medidas de seguridad lógicas esenciales para proteger la integridad y confidencialidad de la identidad y datos asociados.

- La restricción de acceso al portal solo desde direcciones IP ubicadas en Costa Rica, o mediante listas blancas de IPs institucionales, es una medida de seguridad lógica que limita el acceso geográfico y fortalece la protección contra accesos no autorizados.

- El cifrado de datos en reposo y en tránsito y el control de acceso estricto para ingenieros (para evitar acceso a datos en claro) son vitales para cumplir con el deber de confidencialidad y proteger la información sensible.

##### Feliz Compartiendo Datos:

##### ARTÍCULO 4.- Autodeterminación informativa:

La capacidad de los usuarios para gestionar sus datasets es central para este principio.

La sección **Feliz Compartiendo Datos** encarna el Artículo 4 (Autodeterminación Informativa) al permitir a los usuarios:

- Decidir qué datos compartir dentro del ecosistema
- Configurar la visibilidad del dataset (público o privado).
- Definir el modelo de acceso (gratuito o pagado).
- Establecer control granular sobre el acceso por institución, persona o grupo de actores.

Estas funcionalidades garantizan que el titular mantenga el control sobre el uso y la difusión de su información.

##### ARTÍCULO 6 - Principio de calidad de la información:

La Ley 8968 exige que la recolección y uso de datos sea proporcional a la finalidad.

Los requerimientos de **Feliz Compartiendo Datos** se alinean con el Artículo 6 (Principio de Calidad de la Información) al promover la minimización y el propósito limitado:

- La opción de seleccionar campos específicos a cifrar dentro del dataset permite a los usuarios proteger solo la información sensible, sin necesidad de cifrar todo, lo que se alinea con la minimización del tratamiento de datos sensibles.

- La capacidad de restringir acceso a datos por límites de tiempo, volumen o frecuencia de consulta asegura que el acceso y uso de los datos se realice únicamente para la finalidad acordada y bajo las condiciones definidas por el titular.

##### ARTÍCULO 14 - Transferencia de datos personales, regla general:

Si bien la "comercialización" dentro del ecosistema se enfoca en el acceso y consumo interno, el Artículo 20 es una consideración preventiva. Si la plataforma habilitara en el futuro transferencias a entidades o servicios fuera de Costa Rica (por ejemplo, para alimentar modelos de IA en la nube en otros países), se deberían cumplir las condiciones establecidas por este artículo, que incluyen el consentimiento del titular y garantías de seguridad adecuadas para los datos transferidos.

##### Descubriendo Costa Rica:

##### ARTÍCULOS 4 y 10 - Autodeterminación informativa; Seguridad de los datos:

La protección de la autodeterminación informativa y la seguridad son cruciales en la visualización.

La sección **Descubriendo Costa Rica** refuerza el Artículo 4 (Autodeterminación Informativa) y el Artículo 11 (Seguridad de los datos) al:

- Impedir la descarga directa de datos en cualquier momento y bloquear exportaciones de gráficos y contenidos. Esta medida es fundamental para mantener el control del titular sobre la información y prevenir usos no autorizados fuera del entorno seguro de la plataforma.

- Al obligar a la visualización exclusivamente dentro del portal, "Data Pura Vida" implementa una medida de seguridad lógica que reduce el riesgo de fugas de datos y asegura que el uso de la información esté bajo la gobernanza y protección de la Ley 8968. Esto también apoya el principio de limitación de la finalidad.

##### Backend API y Datalake: Aplicación de la Ley 8968 (Costa Rica)

##### Artículo 10 y 30 - Seguridad de los datos; Faltas graves:

Estos son el muy importantes para la infraestructura de seguridad.

Los requerimientos del Backend API y el Datalake son directamente aplicables al Artículo 10 (Seguridad de los datos) y al Artículo 30 (Faltas Graves):

La exigencia de que "Data Pura Vida" implemente medidas técnicas y organizativas para asegurar la protección de los datos se refleja en:

- La protección de la API mediante whitelist de IPs, validación de tokens y MFA.

- Los módulos separados para gestión de credenciales, firmas y cifrado de datos.

- La trazabilidad, cumplimiento legal y control de cada transacción, lo que demuestra un enfoque proactivo en la gestión de la seguridad.

- La implementación de RBAC (Role-Based Access Control) y RLS (Row-Level Security) en el Datalake, junto con el cifrado de datos sensibles en reposo y en tránsito, son medidas de seguridad robustas para proteger la confidencialidad e integridad de la información, previniendo accesos indebidos.

- La prohibición explícita de que ingenieros o personal técnico accedan a los datos en claro o sin autorización refuerza el principio de "conocimiento necesario" y el deber de confidencialidad del Artículo 10.

La auditoría detallada de todas las operaciones realizadas en el sistema (por usuario, acción, fecha y efecto) y el historial de consumo de datos son esenciales para:

- Demostrar el cumplimiento con la Ley 8968 ante la PRODHAB o en caso de una auditoría.

- Permitir la trazabilidad necesaria para la rendición de cuentas y la identificación de cualquier actividad irregular, ayudando a prevenir faltas graves como el tratamiento no autorizado de datos.

- Facilitar la extracción de evidencias para procesos legales o regulatorios.

#### 2. GDPR (General Data Protection Regulation)

Aunque es una regulación de la Unión Europea, el GDPR tiene un alcance extraterritorial. Si "Data Pura Vida" procesa datos de ciudadanos o residentes de la UE, o si ofrece bienes y servicios a ellos, entonces el GDPR es aplicable, independientemente de dónde se encuentre el servidor o la empresa. Dado que Costa Rica es un destino turístico y centro de negocios internacional, es muy probable que haya interacción con datos de la UE. Además, el GDPR ha influenciado muchas leyes de privacidad a nivel mundial, por lo que su cumplimiento a menudo supera los requisitos de otras normativas locales.

##### Aplicación a los Requerimientos de la Plataforma:

##### Bio Registro Verde:

**Bases Legales para el Tratamiento:** El registro debe establecer claramente la base legal para el procesamiento de cada tipo de dato (consentimiento, obligación legal, interés legítimo, etc.) según lo establece el GDPR (artículos 6 y 7). El consentimiento debe ser libre, específico, informado e inequívoco, y fácilmente revocable.

**Privacy by Design and by Default:** El diseño del sistema debe integrar la privacidad desde el inicio (por ejemplo, el cifrado de datos, el control granular de acceso, la minimización de datos por defecto), como exige el artículo 25 del GDPR.

**Derechos de los Interesados:** El GDPR otorga derechos robustos a los interesados (data subjects):

- **Derecho a la Información:** Transparencia sobre el procesamiento de datos (artículos 13 y 14 del GDPR).

- **Derecho de Acceso:** Los usuarios deben poder acceder a sus datos personales (Artículo 15).

- **Derecho de Rectificación:** Corrección de datos inexactos (Artículo 16).

- **Derecho de Supresión ("Derecho al Olvido"):** Eliminación de datos bajo ciertas condiciones (Artículo 17).

- **Derecho a la Limitación del Tratamiento:** Restringir el procesamiento de datos (Artículo 18).

- **Derecho a la portabilidad de los Datos:** Permite a los usuarios r recibir y transmitir sus datos en un formato estructurado (artículo 20).

- **Derecho de Oposición:** Oponerse al tratamiento de sus datos (Artículo 21).

- **Derechos en relación con Decisiones Automatizadas y Perfilado:** El uso de IA debe considerar el derecho a no ser objeto de decisiones basadas únicamente en procesamiento automatizado (artículo 22).

##### Feliz Compartiendo Datos:

**Transferencias Internacionales de Datos:** Si los datos pudieran ser accedidos o transferidos fuera del Espacio Económico Europeo, deben cumplirse los requisitos del Capítulo V del GDPR (artículos 44 al 50), incluyendo garantías como cláusulas tipo o reglas corporativas vinculantes.

**Evaluación de Impacto de Protección de Datos (DPIA):** Para el procesamiento de datos de alto riesgo (como la combinación de grandes volúmenes de datos sensibles, uso de IA para perfilado), una DPIA sería obligatoria bajo el GDPR (Artículo 35).

##### Backend API y Datalake:

**Oficial de Protección de Datos (DPO):** Si se cumple con los criterios (ej. procesamiento a gran escala de categorías especiales de datos o monitoreo sistemático de interesados), Data Pura Vida debería designar un Oficial de Protección de Datos (DPO) (Artículo 37).

**Notificación de Violaciones de Seguridad:** En caso de una brecha de seguridad que afecte datos personales, el GDPR exige la notificación a la autoridad de control en un plazo de 72 horas y, en ciertos casos, también a los interesados (Artículos 33 y 34). Esto implica un robusto sistema de monitoreo y respuesta a incidentes.

#### 3. ISO/IEC 27001 - Sistemas de Gestión de la Seguridad de la Información (SGSI)

Relevancia para **Data Pura Vida**: Aunque no es una ley obligatoria, la ISO/IEC 27001 es un estándar internacional que proporciona un marco para establecer, implementar, mantener y mejorar continuamente un Sistema de Gestión de la Seguridad de la Información (SGSI). Obtener la certificación ISO 27001 demostraría un compromiso serio con la seguridad de la información y la protección de activos, generando confianza en un ecosistema de datos.

##### Aplicación a los Requerimientos de la Plataforma:

La ISO 27001 se basa en la identificación y gestión de riesgos de seguridad de la información. Esto es fundamental para "Data Pura Vida", dada la sensibilidad y el volumen de los datos. Se debe realizar una evaluación de riesgos exhaustiva para determinar las medidas de seguridad necesarias.

Estan los controles de seguidad ubicadas en el anexo A de ISO 27001/ISO 27002 en la cual se ubican el estándar para un conjunto de controles que son relevantes para todos los requerimientos de la plataforma:

- **A.5 Políticas de seguridad de la información:** Definir políticas claras para el uso y acceso de datos.
- **A.6 Organización de la seguridad de la información:** Definir roles y responsabilidades (ej. PM, roles del Backoffice).
- **A.6.2.3 Tratamiento de la seguridad en contratos con terceras personas:** Gestión de la seguridad con terceros si se utilizan servicios externos.
- **A.7 Gestión de activos:** Clasificación de la información (público/privado, gratuito/pagado), y protección de activos.
- **A.8 Seguridad de los recursos humanos:** Seguridad antes, durante y después del empleo (fundamental para el personal de Data Pura Vida, incluyendo ingenieros y personal de backoffice).
- **A.10.6 Gestión de seguridad de redes:** Protección de la información en redes.
- **A.10.10 Monitoreo:** Gestión de logs (auditoría), monitoreo de sistemas, gestión de vulnerabilidades.
- **A.11 Control de acceso:** Implementación de RBAC, RLS, MFA, validación de tokens, whitelists de IPs, y la asignación/revocación de llaves de seguridad. La "llave tripartita" es un control de seguridad avanzado.
- **A.12.3 Controles criptográficos:** El uso de cifrado para datos en reposo y en tránsito, y el cifrado de campos específicos, son controles clave.
- **A.13 Gestión de incidentes de seguridad de la información:** Proceso para detectar, reportar, responder y aprender de los incidentes (crucial para notificar brechas como exige GDPR).
- **A.14.1 Aspectos de seguridad de la información de la gestión de la continuidad del negocio:** Planes de respaldo y recuperación.
- **A.15 Cumplimiento:** Identificación y cumplimiento de requisitos legales y contractuales.

**Mejora Continua (Ciclo PDCA):** ISO 27001 promueve un ciclo de Planificar-Hacer-Verificar-Actuar (PDCA), lo que se alinea con la necesidad de monitoreo continuo de métricas, auditorías y revisión de la dirección para garantizar la mejora continua de la seguridad y el cumplimiento normativo.

#### 4. OECD Data Governance

La OCDE establece principios fundamentales de gobernanza de datos que sirven como referencia para proyectos como Data Pura Vida, orientados a maximizar el uso y la compartición responsable de datos, mientras se protege la privacidad y se fortalece la confianza.

##### Principios Fundamentales de la OCDE

##### Enfoque Integral (Whole-of-Government)

- Promueve la participación de todos los actores (públicos y privados) y la coherencia entre sectores y niveles de gobierno.

##### Equilibrio de Beneficios y Riesgos

- Reconoce la necesidad de equilibrar los beneficios del acceso y uso de datos con los riesgos asociados (privacidad, seguridad, propiedad intelectual).

##### Diversidad de Datos y Respeto a Derechos

- Reconoce distintos niveles de sensibilidad y riesgo de los datos, y garantiza derechos como el acceso, la rectificación y la autodeterminación informativa.

##### Fortalecimiento de Capacidades y Confianza

- Fomenta la cultura de datos, el desarrollo de infraestructura y el establecimiento de relaciones de confianza entre actores.

##### Recomendaciones de la OCDE Aplicables

La OCDE ha emitido siete recomendaciones que sirven como marco para la gobernanza de datos y que deben integrarse a Data Pura Vida:

- Acceso a datos de investigación financiados públicamente (2006).
- Acceso y uso de información del sector público (2008).
- Protección de privacidad y flujos transfronterizos de datos (2013).
- Gobernanza de datos de salud (2016).
- Estrategias de gobierno digital (2014).

##### Aplicación a los Requerimientos de la Plataforma

##### Bio Registro Verde

Aplica el enfoque integral al registrar a todos los actores relevantes con autenticación avanzada (MFA, biometría, prueba de vida).

Implementa controles criptográficos (llaves simétricas y asimétricas) y segmentación de acceso por roles, siguiendo los estándares de confianza y seguridad.

##### Feliz Compartiendo Datos

Permite la clasificación de datasets (públicos, privados, gratuitos o pagados) y la definición de controles de acceso granular, balanceando beneficios de compartición con protección de derechos.

Soporta múltiples formatos de carga y mecanismos de conexión, fomentando la interoperabilidad.

##### Descubriendo Costa Rica

Limita la descarga directa y exportación de datos, asegurando que el acceso a datos se haga solo en entornos seguros y controlados.

Construcción de dashboards personalizables con visibilidad granular, respetando la autonomía de los usuarios y el principio de minimización.

##### Backend API y Datalake

Implementación de MFA, whitelists de IPs y control de acceso estricto para proteger la confidencialidad y cumplir con las recomendaciones de seguridad de la OCDE.

Uso de IA para normalización, relación de datos y detección de duplicidades, reforzando la calidad y eficiencia de la gobernanza de datos.

La implementación de **Data Pura Vida** no solo debe enfocarse en la funcionalidad, sino que debe tener la privacidad y seguridad integradas desde el diseño. El cumplimiento de la Ley 8968 es mandatorio para operar en Costa Rica. La incorporación de principios del GDPR y ISO 27001 garantizará un nivel de protección de datos de clase mundial y facilitará la confianza, mientras que las directrices de la OCDE proporcionarán la base para una gobernanza de datos efectiva y una promoción responsable del intercambio y uso de la información.

#### 5. Checklist para el Equipo de Desarrollo de "Data Pura Vida"

Este checklist tiene como objetivo presentar los requisitos legales y de seguridad de **Data Pura Vida** en acciones concretas para el equipo de desarrollo, asegurando el cumplimiento con la Ley 8968, GDPR, ISO/IEC 27001 y los principios de la OCDE.

##### Datalake

###### Cifrado de Datos:

- [ ] Implementar cifrado en reposo para todos los datos sensibles en el Datalake.
- [ ] Implementar cifrado en tránsito para todas las comunicaciones hacia y desde el Datalake.
- [ ] Asegurar que los campos específicos marcados como sensibles puedan ser cifrados a nivel de campo.

###### Control de Acceso:

- [ ] Configurar RBAC (Role-Based Access Control) para todos los usuarios y servicios que interactúan con el Datalake, otorgando el mínimo privilegio necesario.
- [ ] Implementar RLS (Row-Level Security) para asegurar que los usuarios solo puedan ver las filas de datos a las que tienen autorización explícita.
- [ ] Asegurar que ningún ingeniero o personal técnico pueda acceder a los datos en claro sin autorización.

###### Calidad y Gobernanza de Datos:

- [ ] Implementar mecanismos de validación de datos en el punto de entrada para asegurar la calidad y exactitud.
- [ ] Desarrollar y aplicar algoritmos de IA para normalización, relación de datos y detección de duplicidades.

###### Auditoría y Trazabilidad:

- [ ] Implementar auditoría detallada de todas las operaciones de CRUD (Crear, Leer, Actualizar, Borrar) en el Datalake, registrando usuario, acción, fecha, hora y efecto.
- [ ] Mantener un historial de consumo de datos por parte de los usuarios y servicios.

##### Backend API

###### Seguridad de la API:

- [ ] Proteger la API con whitelist de IPs (si aplica, para IPs institucionales o de Costa Rica).
- [ ] Implementar un robusto sistema de validación de tokens (ej. JWT) para todas las solicitudes.
- [ ] Exigir Multi-Factor Authentication (MFA) para el acceso a la API para usuarios administrativos o con privilegios elevados.

###### Gestión de Credenciales y Criptografía:

- [ ] Desarrollar módulos separados para la gestión de credenciales, firmas y cifrado de datos.
- [ ] Implementar el sistema de llave tripartita para la protección de identidades y datos asociados.

###### Registro y Monitoreo:

- [ ] Asegurar la trazabilidad y registro de cada transacción que pase por la API.
- [ ] Implementar monitoreo continuo de la API para detectar actividades anómalas o intentos de acceso no autorizado.

###### Transferencia de Datos:

- [ ] Si hay transferencia de datos fuera de Costa Rica, asegurar que se cumplen las garantías de seguridad.

##### Interfaz de Usuario (UI) - Bio Registro Verde

###### Consentimiento Informado (Ley 8968 Artículo. 5, GDPR Artículos. 6 y 7):

- [ ] Diseñar una sección clara y destacada en el registro para informar sobre:

  - La existencia de "Data Pura Vida" y su finalidad.
  - Los destinatarios de los datos.
  - La obligatoriedad de ciertos datos y sus consecuencias.
  - Los derechos ARCO y cómo ejercerlos.

- [ ] Implementar un checkbox explícito de "Acepto los Términos y Condiciones y la Política de Privacidad" que el usuario debe marcar activamente.
- [ ] Almacenar de forma segura la documentación del consentimiento vinculada al registro del usuario.

###### Autenticación y Validación:

- [ ] Integrar identidad digital, biometría o prueba de vida en el proceso de autenticación inicial.
- [ ] Implementar MFA para el acceso de los usuarios a sus cuentas.
- [ ] Integrar validación documental automatizada por IA para verificar la completitud y validez de documentos (ej. cédulas, etc.).

###### Derechos ARCO (Acceso, Rectificación, Cancelación y Oposición) (Ley 8968 Artículo. 7, GDPR Artículos. 15-21):

- [ ] Proporcionar un mecanismo claro y accesible en el perfil del usuario para:

  - Acceder a sus datos personales.
  - Rectificar datos inexactos.
  - Solicitar la eliminación de datos (Derecho al Olvido), con la lógica de negocio asociada.

- [ ] Si aplica, ofrecer opciones para limitar el tratamiento y ejercer la portabilidad de datos.
- [ ] Considerar el derecho a oponerse a decisiones basadas únicamente en procesamiento automatizado si la IA afecta decisiones legales significativas sobre el usuario.

###### Privacidad de Datos (Ley 8968 Artículo. 6, GDPR Artículo. 25):

- [ ] Asegurar que sistema integre la privacidad desde el inicio (ej. el cifrado de datos, el control granular de acceso, la minimización de datos por defecto).

##### Interfaz de Usuario (UI) - Feliz Compartiendo Datos

###### Autodeterminación Informativa (Ley 8968 Artículo. 4):

- [ ] Desarrollar funcionalidades para que el usuario pueda:
      Decidir qué datasets compartir.

  - Configurar la visibilidad del dataset (público/privado).
  - Definir el modelo de acceso (gratuito/pagado).
  - Establecer control granular sobre el acceso por institución, persona o grupo de actores.

- [ ] Permitir la selección de campos específicos a cifrar dentro del dataset compartido.

- [ ] Habilitar la capacidad de restringir el acceso a datos por límites de tiempo, volumen o frecuencia de consulta.

###### Interoperabilidad (Principios OCDE):

- [ ] Soportar múltiples formatos de carga y mecanismos de conexión para datasets.

##### Interfaz de Usuario (UI) - Descubriendo Costa Rica

###### Seguridad en Visualización (Ley 8968 Artículo. 10):

- [ ] Bloquear la descarga directa de datos desde los dashboards o visualizaciones.
- [ ] Impedir la exportación de gráficos y contenidos a formatos externos.
- [ ] Asegurar que la visualización de datos solo sea posible dentro del entorno seguro del portal.

###### Control Granular y Personalización:

- [ ] Permitir la construcción de dashboards personalizables por los usuarios.
- [ ] Asegurar que la visibilidad granular aplicada en "Feliz Compartiendo Datos" se refleje correctamente en las visualizaciones.

##### Seguridad General y Operaciones

###### Políticas y Procedimientos (ISO 27001 A.5, A.6, A.8):

- [ ] Colaborar con el equipo de PM/Seguridad para la implementación de las políticas de seguridad de la información.
- [ ] Asegurar que el personal de desarrollo (ingenieros, backoffice) cumpla con los controles de seguridad antes, durante y después del empleo.

###### Controles de Acceso Lógico (ISO 27001 A.11):

- [ ] Restringir el acceso al portal solo desde direcciones IP ubicadas en Costa Rica o a través de listas blancas de IPs institucionales.

###### Monitoreo y Gestión de Incidentes (ISO 27001 A.10.10, A.13, GDPR Artículos. 33 y 34):

- [ ] Implementar monitoreo de sistemas y gestión de logs para todas las plataformas.
- [ ] Desarrollar un proceso claro y automatizado para la detección, reporte y respuesta a incidentes de seguridad.
- [ ] Preparar la capacidad técnica para notificar brechas de seguridad a la autoridad de control (PRODHAB, DPA de la UE) y a los interesados dentro de los plazos establecidos (ej. 72 horas para GDPR).

##### Cifrado General (ISO 27001 A.12.3):

- [ ] Asegurar el uso de cifrado para todos los datos en reposo y en tránsito a través de la plataforma.

###### Pruebas de Seguridad:

- [ ] Realizar pruebas de penetración y escaneos de vulnerabilidades de forma regular.
- [ ] Incluir pruebas de seguridad en el ciclo de vida de desarrollo de software.

###### Continuidad del Negocio (ISO 27001 A.14.1):

- [ ] Implementar planes de respaldo y recuperación para todos los componentes críticos del sistema.

##### Gobernanza de Datos y Cumplimiento

###### Auditoría Interna y Externa:

- [ ] Estar preparado para auditorías internas y externas para demostrar el cumplimiento con la Ley 8968, GDPR e ISO 27001.
- [ ] Asegurar la disponibilidad de evidencias (logs, configuraciones, políticas) para procesos legales o regulatorios.

###### Documentación:

- [ ] Mantener una documentación actualizada de la arquitectura de seguridad, controles implementados y flujos de datos.

### 2.2 Prácticas de Manejo de Código

Para garantizar que el código fuente de Data Pura Vida sea seguro, mantenible y escalable, se adoptan tres marcos principales de buenas prácticas:

#### 1. OWASP Secure Coding Practices

Basados en los estándares de OWASP Top 10 y OWASP ASVS:

- Validación de entradas:

  - Se realiza con el objetivo de que solo los datos parametrizados correctamente entren al workflow de Data Pura Vida.
  - Se evita que malformaciones de datos entren en las bases de datos y realicen un efecto en cadena de malfuncionamientos.

- Control de acceso y privilegios mínimos:

  - El objetivo es asegurar que cada usuario solo tenga acceso a los recursos estrictamente necesarios para cumplir su función.
  - Se evitará la acumulación de privilegios innecesarios a lo largo del tiempo mediante revisiones periódicas.
  - Todas las solicitudes serán validadas en el backend, independientemente de su origen.
  - En lugar de depender exclusivamente de roles (RBAC) también se hara el uso de ABAC (Attribute-Based Access Control).

- Almacenamiento y transmisión segura:
  - Todos los datos sensibles serán cifrados en tránsito mediante TLS 1.3 y en reposo mediante AES-256.
  - **TLS 1.3 (Transport Layer Security):** protocolo criptográfico utilizado para proteger los datos en tránsito entre el cliente y el servidor. Asegura la confidencialidad e integridad de la información, evitando ataques de MITM(Man in the middle). - **AES-256 (Advanced Encryption Standard):** algoritmo de cifrado simétrico que se usa para proteger los datos almacenados en el sistema. Utiliza una clave de 256 bits, lo que lo hace extremadamente resistente a ataques de fuerza bruta. Es uno de los estándares más seguros y reconocidos a nivel mundial.
    - El sistema implementará gestión segura de llaves y almacenamiento segmentado para evitar accesos no autorizados, incluso desde el personal técnico.
- Manejo seguro de errores:

  - Los mensajes de error visibles para el usuario serán genéricos, evitando revelar información del sistema.
  - Los errores serán registrados en logs internos enmascarados, permitiendo análisis posterior sin comprometer datos sensibles.

- Protección ante dependencias vulnerables:

  - Se integrará un escaneo automatizado de dependencias y librerías de terceros en el pipeline de CI/CD.
  - Las versiones serán actualizadas de forma periódica y se restringirá el uso de paquetes sin mantenimiento o con vulnerabilidades conocidas.

- Autenticación robusta:
  - El sistema implementará OAuth2 para autorización y JWT como mecanismo de sesión segura.
    - **OAuth2 (Open Authorization 2.0):** es un protocolo de autorización que permite a una aplicación acceder a recursos en nombre del usuario sin necesidad de compartir sus credenciales.
    - **JWT (JSON Web Token):** es un formato compacto y seguro para transmitir información entre partes como un objeto JSON firmado. Se usa para manejar sesiones de forma segura, ya que contiene los datos del usuario y sus permisos codificados y firmados digitalmente, lo que permite validar su autenticidad sin necesidad de consultar una base de datos en cada petición.
  - Además, toda cuenta que acceda a áreas críticas deberá utilizar autenticación multifactor (MFA), y se exigirá prueba de vida y biometría en el registro de representantes legales.

#### 2. Clean code

El proyecto aplicará los principios fundamentales de Clean Code propuestos por Robert C. Martin y enriquecidos con buenas prácticas reconocidas de la industria, con el objetivo de asegurar un código legible, mantenible y confiable.

**Principios clave aplicados:**

- **Funciones pequeñas y específicas:** Cada función debe realizar una sola tarea de forma clara.

- **Nombres claros y semánticos:** Variables, funciones y clases deben ser autodescriptivas.

- **Evitar código innecesario:** Se eliminará código muerto o comentarios obvios.

- **Regla del Boy Scout:** Dejar el código más limpio de como se encontró.

- **Manejo explícito de errores:** Nunca se deben silenciar excepciones.

- **Evitar condicionales complejos:** Preferir polimorfismo sobre if o switch.

- **Separación vertical:** Agrupar código relacionado en bloques visuales cercanos.

- **Ley de Demeter:** Cada clase solo debe conocer sus dependencias directas.

**Implementación concreta en el proyecto:**

- **Uso de linters y formatters:** Se utilizaran para validar estilo de código en cada lenguaje usado (ESLint, SonarQube, entre otros).

- **Refactorización continua:** Esta práctica será integrada como una actividad habitual dentro del flujo de trabajo del equipo.

- **Validaciones reutilizables:** Se implementarán middlewares específicos para validar tokens, estructura de datos y permisos, evitando duplicación de lógica (principio DRY: Don’t Repeat Yourself).

- **Inyección de dependencias:** Los servicios críticos como cifrado, autenticación y conexión a base de datos se gestionarán por inyección de dependencias, lo que facilita el testing y desacopla las capas del sistema.

- **Controladores REST claros:** Los endpoints de la API seguirán convenciones semánticas (`GET /datasets`, `POST /register`, etc.) y estarán separados en archivos por entidad, facilitando su lectura y mantenimiento.

- **Nombres de funciones como verbos y de clases como sustantivos:**
  Por ejemplo: `validateInput()`, `encryptDataset()`, `DatasetUploader`, `IbanVerifier`.

- **Uso de constantes centralizadas:** Valores como `MAX_UPLOAD_SIZE_MB`, `SUPPORTED_FORMATS`, `DEFAULT_LANGUAGE` estarán definidos en archivos de configuración o constantes globales.

- **Errores bien definidos y gestionados:** Todos los errores tendrán estructuras estandarizadas `({code, message, details})` y serán manejados con `try/catch` en backend, registrando trazas seguras en logs sin exponer detalles internos al usuario.

Estas prácticas no solo mejoran la calidad del software, sino que también reducen los costos de mantenimiento, facilitan las auditorías de seguridad y mejoran la experiencia del equipo de desarrollo durante todo el ciclo de vida del sistema.

#### 3. The Twelve-Factor App

El desarrollo de Data Pura Vida también se alinea con los principios del manifiesto Twelve-Factor App, con el objetivo de garantizar una arquitectura moderna, portable, escalable y apta para despliegues en la nube o entornos híbridos. A continuación se detallan los factores aplicados:

1. **Código base:** El código está centralizado en un único repositorio de GitHub con control de versiones. Cada microservicio o módulo mantiene su propio namespace lógico.

2. **Dependencias explícitas:** Se utiliza un package manager en cada stack (como npm, pip, o cargo) y un archivo de lock (package-lock.json, Pipfile.lock, etc.) para gestionar y auditar todas las dependencias.

3. **Configuración separada:** Variables sensibles como claves de API, cadenas de conexión y llaves criptográficas se mantienen fuera del código, gestionadas mediante variables de entorno y servicios seguros de secretos (como AWS Secrets Manager o .env en desarrollo).

4. **Servicios externos como recursos:** Todas las bases de datos, colas, y almacenamiento externo se consideran recursos gestionados a través de URLs o credenciales inyectadas dinámicamente, lo que permite su intercambio sin afectar el código.

5. **Construcción, ejecución y publicación desacopladas:** Se definen pipelines de CI/CD que separan claramente la fase de build (npm run build), la fase de ejecución (node app.js) y el entorno de despliegue (Docker/OCI).

6. **Procesos sin estado:** El backend es stateless. Toda la sesión del usuario se gestiona mediante JWT y los archivos temporales se almacenan en servicios externos como S3, no en disco local.

7. **Vinculación de puertos:** Cada componente expone sus servicios por medio de puertos estándar (PORT=3000) facilitando integración y despliegue en contenedores.

8. **Concurrencia:** Se utilizan workers y multiprocesamiento para escalar horizontalmente los módulos de procesamiento intensivo, como el motor de validación ETDL y el generador de dashboards.

9. **Descarte rápido:** Las apps manejan señales del sistema operativo (SIGTERM, SIGINT) y liberan recursos como conexiones o archivos abiertos. Esto permite ciclos de despliegue seguros y rápidos.

10. **Entornos de desarrollo y producción iguales:** Se utilizan contenedores (Docker) para asegurar que el código se ejecute de forma idéntica en desarrollo, staging y producción.

11. **Logs como streams:** Los logs no se almacenan en archivos, sino que se emiten a stdout/stderr y se redirigen a herramientas de agregación como Elastic Stack o Grafana Loki.

12. **Procesos administrativos como tareas one-off:** Scripts de migración, pruebas y carga inicial de datos se ejecutan como procesos independientes (npm run seed, python manage.py migrate), no embebidos en el ciclo de vida principal de la app.

#### Buenas Prácticas Complementarias de Codificación Segura

| Objetivo                      | Práctica                                       | Aplicación                                                                       |
| ----------------------------- | ---------------------------------------------- | -------------------------------------------------------------------------------- |
| **Visibilidad y detección**   | Logs + monitoreo en tiempo real                | Uso de Prometheus y Alertmanager para monitoreo                                  |
| **Seguridad en dependencias** | Escaneo continuo y alertas automáticas         | GitHub Dependabot activado                                                       |
| **Gestión de secretos**       | Manejo seguro de claves, tokens y credenciales | Uso de servicios como AWS Secrets Manager o archivos .env con acceso restringido |
| **Protección de endpoints**   | CORS y rate-limiting                           | Configuración estricta de origen cruzado (CORS) y límites de solicitudes por IP  |

#### Validación automatizada de código

Con el fin de reforzar las prácticas de codificación segura, mantenible y coherente, el proyecto Data Pura Vida adoptará una estrategia de validación automatizada. Esta estrategia abarcará tanto el estilo y la calidad del código como la seguridad y el cumplimiento de reglas internas de desarrollo.

**1. Linter personalizado y estilización de código:**

- Se usará `ESLint` como base para código en Node.js, incorporando lo siguiente:

  - Principios de Clean Code.

  - Recomendaciones OWASP para codificación segura.

  - Reglas adicionales generadas con ayuda de una IA especializada en refactorización.

- Además, se incluirá `Prettier` para formateo del código. Las reglas podrán ser vistas en archivos con los siguientes formatos:

  - `/.config/lint/eslintrc.js`

  - `/docs/estandares-codigo.md`

- A continuación, un ejemplo de un archivo `.eslintrc.js` que funciona para un proyecto Node.js:

```js
module.exports = {
  root: true,
  env: {
    node: true,
    es2021: true,
  },
  extends: [
    "eslint:recommended",
    "plugin:security/recommended", // OWASP rules
    "airbnb-base", // Airbnb style guide
    "plugin:prettier/recommended",
  ],
  plugins: ["security", "prettier"],
  parserOptions: {
    ecmaVersion: 12,
    sourceType: "module",
  },
  rules: {
    // --- Clean Code ---
    "no-unused-vars": ["warn", { argsIgnorePattern: "^_" }],
    "no-console": "warn",
    "prefer-const": "error",
    "no-magic-numbers": [
      "warn",
      { ignore: [0, 1, -1], enforceConst: true, detectObjects: false },
    ],
    "consistent-return": "error",
    "no-else-return": "error",

    // --- Seguridad (OWASP & buenas prácticas) ---
    "security/detect-object-injection": "warn",
    "security/detect-non-literal-fs-filename": "warn",
    "security/detect-eval-with-expression": "error",
    "security/detect-buffer-noassert": "error",

    // --- Legibilidad y mantenibilidad ---
    "max-lines": [
      "warn",
      { max: 300, skipBlankLines: true, skipComments: true },
    ],
    "max-depth": ["warn", 4],
    complexity: ["warn", 10],
    camelcase: "error",
    "newline-before-return": "warn",

    // --- Estilo general (Airbnb + Prettier) ---
    "prettier/prettier": [
      "error",
      {
        printWidth: 100,
        semi: true,
        singleQuote: true,
        trailingComma: "es5",
        arrowParens: "always",
      },
    ],

    // --- Reglas adaptadas al proyecto Data Pura Vida ---
    "no-param-reassign": ["error", { props: true }],
    "import/order": [
      "warn",
      {
        groups: [
          ["builtin", "external"],
          "internal",
          "parent",
          "sibling",
          "index",
        ],
        "newlines-between": "always",
      },
    ],
  },
  overrides: [
    {
      files: ["*.test.js", "*.spec.js"],
      env: {
        jest: true,
      },
    },
  ],
};
```

**2. Análisis de calidad y seguridad del código:**

- Se integrará `SonarQube` para análisis estático continuo del código.
- Su uso será para detectar usos inseguros de variables de entorno, errores de autenticación, entre otros.

**3. Validación de dependencias:**

- Se hará uso de `Dependabot` para revisar librerías vulnerables.
- En estas validaciones se revisan versiones desactualizadas o inseguras de paquetes, licencias incompatibles con el proyecto, paquetes abandonados, entre otros.

### 2.3 Sistema de Versionamiento

Para el versionamiento de los distintos componentes de Data Pura Vida manejaremos un solo repositorio en GitHub, utilizando un enfoque inspirado en Git Flow, adaptado para flujos modernos con automatización CI/CD, de la siguiente forma:

- main: rama estable lista para production.

- dev: rama de integración en ella se corren los tests

- feature/\*: son ramas efímeras en las que se desarrolla una característica en específico

- fix/\*: son ramas efímeras en las que se solventan hotfixes o bugs.

Todo cambio realizado en las ramas de feature y hotfix, una vez estén listos, se deben fusionar a la rama dev, donde se ejecutarán las pruebas correspondientes. Luego, cuando todo esté aprobado, se harán merge a la rama main para que se realice el despliegue a producción.

#### Versionado

Se seguirá un esquema de versionado semántico usando la notación MAJOR.MINOR.PATCH, por ejemplo: 2.3.1. Esto permitirá comunicar de forma clara el tipo de cambios introducidos:

MAJOR: Se incrementa cuando hay cambios incompatibles con versiones anteriores.

MINOR: Se incrementa al agregar funcionalidades nuevas que mantienen compatibilidad.

PATCH: Se incrementa al aplicar correcciones de errores menores o mejoras no disruptivas.

Ejemplos:

Cambiar la estructura del modelo de datos → 2.0.0

Agregar una nueva funcionalidad al generador de dashboards → 2.1.0

Corregir un bug en la visualización de gráficos → 2.1.1

#### Estructura del repositorio

A continuación, esta será la estructura del repositorio:

```bash
/data-pura-vida/
├── components/
│   ├── bioregistro-verde/
│   ├── la-boveda/
│   ├── ingestor/
│   ├── motor-de-transformacion/
│   ├── centro-de-visualizacion-y-consumo/
│   │   ├── generador-de-dashboards/
│   │   ├── consumo-para-ia/
│   │   └── visualización-consumo/
│   ├── marketplace/
│   └── backoffice/
├── shared/
│   ├── utils/
│   └── auth/
├── infra/
│   └── terraform/
├── .github/
│   └── workflows/
└── docker-compose.yml
```

- En la carpeta de components estarán albergados todos los componentes del sistema, junto con sus subcomponentes.

- El el directorio de shared se encontrarán librerias y herramientas comunes a todos los componentes.

- En terraform/ estará la estructura para el despliegue en AWS, todo cambio al app para poder verse reflejado en el cloud provider debe pasar por acá.

ejemplos de archivos en terraform son:

```hcl

# provider.tf, para poner la metada del cloud provider
provider "aws" {
  region = "us-east-1"
}

# s3.tf, para crear un bucket de S3
resource "aws_s3_bucket" "react_app_bucket" {
  bucket = "mi-bucket-react-app-unique-1234"
  acl    = "public-read"
}

# eks.tf, para crear un cluster de EKS
module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = "mi-cluster-eks"
  cluster_version = "1.27"

  subnets         = ["subnet-12345", "subnet-67890"] # las subnets donde va el cluster
  vpc_id          = "vpc-abcde123"

  node_groups = {
    default = {
      desired_capacity = 2
      max_capacity     = 3
      min_capacity     = 1

      instance_type = "t3.medium"
    }
  }
}

```

- En .github/ estarán ubicados los pipelines de GitHub Actions. Definirá las reglas de despliegue del app, por ejmplo, cuando se haga un push a main de cierto componente, se encargará de prepararlo y hacer su deploy al cloud provider. A continuación un ejemplo de un pipeline que monta un microservicio en EKS:

```yaml
name: Deploy-Microservice

on:
  push:
    branches:
      - main

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up AWS CLI
        uses: aws-actions/configure-aws-credentials@v2
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1

      - name: Terraform Init and Apply
        working-directory: ./terraform/bioregistro-verde
        run: |
          terraform init
          terraform apply -auto-approve

      - name: Build Docker image
        run: |
          docker build -t ${{ secrets.ECR_REPO_URI }}/bioregistro-verde:latest .
          aws ecr get-login-password | docker login --username AWS --password-stdin ${{ secrets.ECR_REPO_URI }}
          docker push ${{ secrets.ECR_REPO_URI }}/bioregistro-verde:latest

      - name: Deploy to EKS
        run: |
          helm upgrade --install bioregistro-verde ./charts/bioregistro-verde \
          --set image.repository=${{ secrets.ECR_REPO_URI }}/bioregistro-verde \
          --set image.tag=latest
```

### 2.4 Sistemas de Terceros

Durante el desarrollo e integración de la plataforma Data Pura Vida, se contempla el uso de múltiples sistemas de terceros que habilitan funciones clave como autenticación, verificación de identidad, procesamiento inteligente y orquestación de datos. A continuación, se describen los principales:

#### Protocolos de Autenticación

- OAuth2: Protocolo estándar utilizado para autorización segura entre frontend, backend y terceros que acceden a APIs protegidas.
- JWT (JSON Web Token): Para transmisión segura de credenciales y validación de sesiones, especialmente en dashboards y servicios personalizados.
- MFA: Autenticación multifactor implementada mediante servicios externos como Google Authenticator o Auth0, fortaleciendo el inicio de sesión y la gestión de cuentas.

#### Verificación de Identidad y Seguridad

- SumSub: Plataforma externa para verificación de identidad (KYC), validación documental automática y prueba de vida para personas físicas o representantes institucionales.

#### Proveedor de Nube

- AWS: Plataforma seleccionada para el despliegue de componentes, incluyendo servicios de hosting, bases de datos, colas de eventos, control de accesos, API Gateway, y otros servicios específicos como S3, Lambda, DynamoDB, etc.

#### Inteligencia Artificial y Recomendaciones

- Hugging Face / GPT Recommender: Integraciones exploradas para generar recomendaciones de datasets mediante modelos preentrenados de lenguaje natural.

#### Orquestación y Flujos de Datos

- Google Cloud Workflows y BigQuery: Se valorará el uso de servicios de Google para tareas específicas de integración de datos y análisis en el datalake, incluyendo procesamiento por lotes, consultas distribuidas y automatización de flujos de datos complejos.

### 2.5 Aspectos de Calidad/SLA

Para garantizar que **Data Pura Vida** funcione exitosamente como ecosistema nacional de datos de Costa Rica, se establecen cinco aspectos de calidad fundamentales con implementaciones técnicas específicas que guiarán el diseño y operación del sistema.


#### **2.5.1 Escalabilidad**

La escalabilidad es la capacidad del sistema para manejar un crecimiento progresivo de usuarios, datos y transacciones sin que se degrade el rendimiento o la calidad del servicio.

Data Pura Vida debe comenzar con las instituciones públicas principales y crecer gradualmente hasta servir a miles de usuarios simultáneos, incluyendo ciudadanos, empresas, organizaciones sociales y entidades gubernamentales. El sistema debe soportar desde datasets iniciales de unas pocas instituciones hasta volúmenes masivos de información nacional.

**Capacidades de crecimiento requeridas:**

- Soporte para miles de usuarios trabajando al mismo tiempo sin ralentización
- Almacenamiento que puede expandirse desde gigabytes hasta terabytes de información
- Procesamiento capaz de manejar cientos de datasets nuevos diariamente durante períodos de alta actividad
- Cobertura nacional con tiempos de respuesta rápidos desde cualquier provincia

**Configuraciones técnicas específicas para escalabilidad:**

**Balanceador de Carga y Gateway:**
El sistema utilizará un balanceador de carga configurado en la infraestructura cloud de AWS con parámetros específicos para garantizar distribución eficiente del tráfico:

- Configuración en 2 zonas de disponibilidad con verificaciones de salud cada 60 segundos
- Capacidad de 500 solicitudes por segundo por instancia con escalado automático hasta 6 instancias
- Tiempo límite de 30 segundos para solicitudes normales, 600 segundos para cargas de datasets grandes
- Terminación SSL con TLS 1.3 y certificados renovados cada 6 meses

**Gestión de Conexiones y Concurrencia:**
Para manejar múltiples usuarios simultáneos, se implementará un sistema de agrupación de conexiones a base de datos:

- Agrupación con mínimo 3 conexiones activas, máximo 12 conexiones por servicio
- Tiempo límite de conexión de 45 segundos, tiempo límite de adquisición de 90 segundos
- Tiempo límite inactivo de 60 segundos para liberar conexiones no utilizadas
- Tiempo límite de conexión de 10 segundos para establecimiento de nuevas conexiones

**Estrategia de Caché Multicapa:**
El almacenamiento temporal de datos frecuentemente accedidos mejorará el rendimiento mediante:

- **Nivel 1 - Caché de Aplicación**: Caché en memoria con tiempo de vida de 15 minutos
- **Nivel 2 - Caché Distribuido**: Tecnología de caché distribuido a definir en Stack Tecnológico
- **Nivel 3 - Caché de Base de Datos**: Optimización a nivel de base de datos
- Tiempo de vida específico por tipo de dato: usuarios (2 horas), metadatos de datasets (8 horas), validaciones (48 horas)

**Procesamiento de Datos con Inteligencia Artificial:**
Para el Motor ETDL (Extracción, Transformación y Carga) que utiliza inteligencia artificial, se configurarán colas de procesamiento:

- Cola tipo FIFO (Primero en Entrar, Primero en Salir) para garantizar orden en procesamiento
- Tiempo límite de visibilidad de 30 minutos (tiempo máximo de procesamiento por dataset)
- Retención de mensajes de 7 días para reintento de fallos
- Tamaño de lote de 5 mensajes por procesamiento para eficiencia
- Máximo 3 datasets procesándose simultáneamente para evitar sobrecarga

**Control de Concurrencia para Inteligencia Artificial:**
Dado que modificar el diseño de modelos concurrentemente es peligroso, se implementarán semáforos y procesamiento asíncrono:

- Semáforo único para modificaciones concurrentes del modelo de datos
- Solo 1 modificación de esquema simultánea permitida
- Tiempo límite de 60 minutos para operaciones de modificación de modelo
- Cola de espera para modificaciones pendientes con prioridad FIFO

**Mecanismos de escalabilidad:**

El sistema utilizará escalado automático, que significa que cuando detecta mayor actividad, automáticamente asigna más recursos computacionales (servidores adicionales) para mantener el rendimiento. Cada componente puede crecer independientemente según su demanda específica, y el sistema se optimiza continuamente basándose en los patrones de uso reales de los costarricenses.



#### **2.5.2 Mantenibilidad**

La mantenibilidad se refiere a la facilidad con que el sistema puede ser actualizado, corregido y mejorado a lo largo del tiempo sin interrumpir el servicio a los usuarios.

Un sistema nacional debe poder evolucionar constantemente. Las regulaciones cambian, las necesidades del país se transforman, y la tecnología avanza. Data Pura Vida debe adaptarse a estos cambios sin afectar su operación diaria.

**Compromisos de mantenibilidad:**

- Resolución de problemas críticos en máximo cuatro horas
- Implementación de mejoras sin interrumpir el servicio a usuarios
- Capacidad de revertir cambios problemáticos en menos de quince minutos
- Monitoreo proactivo que detecta problemas antes de que afecten a los usuarios

**Configuraciones técnicas específicas para mantenibilidad:**

**Sistema de Monitoreo Integrado:**
La observabilidad es la capacidad de entender el estado interno del sistema basándose en los datos que produce:

- **Métricas**: Retención de 15 días con resolución de 30 segundos para métricas críticas
- **Registros**: Retención de 30 días con compresión automática después de 3 días
- **Trazas**: Seguimiento de solicitudes entre componentes para depuración
- **Alertas**: 25 reglas configuradas para diferentes umbrales críticos del sistema
- **Herramientas**: Stack de monitoreo a definir en Stack Tecnológico

**Integración Continua y Despliegue Continuo:**
La práctica de integrar código frecuentemente y desplegarlo automáticamente incluye:

- **GitHub Actions**: Pipelines automatizados según la estructura definida en .github/workflows/
- **Terraform**: Infraestructura como código para despliegue en AWS según /infra/terraform/
- **Estrategia de Despliegue**: Estrategia de despliegue seguro a definir en Stack Tecnológico
- Pruebas automáticas con cobertura mínima del 70% antes de despliegue
- Construcción y empaquetado de aplicaciones con etiquetado por commit SHA
- Verificación de salud automática con tiempo límite de 5 minutos antes de activación

**Migraciones de Base de Datos:**
Los scripts que permiten evolucionar la estructura de la base de datos de forma controlada:

- Scripts de migración versionados con nomenclatura estándar
- Reversión automática si la migración falla
- Validación con verificación de suma de comprobación en cada despliegue
- Respaldo automático antes de cada migración crítica
- **Herramienta**: Sistema de migración a definir según tecnología de base de datos seleccionada

**Estrategia de Reversión:**

- Reversión automática a revisión anterior en caso de fallo
- Tiempo límite configurado a 10 minutos máximo para reversión completa
- Preservación de últimas 5 revisiones para reversión selectiva
- Scripts de reversión semiautomáticos para cambios de base de datos

**Estrategias de mantenimiento:**

El sistema utiliza una arquitectura modular, lo que significa que cada componente puede actualizarse independientemente sin afectar los demás. Los despliegues son automatizados con validación previa, y existe documentación que se actualiza automáticamente. El sistema incluye observabilidad completa, que es la capacidad de monitorear en tiempo real el rendimiento, errores y patrones de uso.

#### **2.5.3 Reutilización**

La reutilización maximiza el aprovechamiento de cada funcionalidad desarrollada, permitiendo que sea utilizada en múltiples componentes del sistema para optimizar recursos y garantizar consistencia.

Con recursos públicos limitados, cada desarrollo debe aprovecharse al máximo. Cuando se crea una funcionalidad para validar documentos costarricenses, esta debe servir para todo el sistema, no solo para una parte específica.

**Componentes reutilizables principales:**

- Sistema de autenticación unificado que permite un solo acceso para toda la plataforma
- Validadores específicos para documentos costarricenses (cédulas, IBAN, registros tributarios)
- Biblioteca de componentes visuales que garantiza interfaces consistentes
- Herramientas de cifrado estandarizadas para protección de datos
- APIs (interfaces de programación) comunes para integraciones con sistemas externos

**Configuraciones técnicas específicas para reutilización:**

**Librerías Compartidas según estructura del repositorio:**
Basándose en el directorio /shared/ definido en el README:

- **shared/utils/**: Utilidades comunes para todos los componentes
- **shared/auth/**: Sistema de autenticación unificado usando OAuth2 y JWT

**OAuth2 (Autorización Abierta 2.0) y JWT (Token Web JSON):**
OAuth2 es un protocolo de autorización que permite a aplicaciones obtener acceso limitado a cuentas de usuario:

- Configuración con proveedores Google y Microsoft según requerimientos
- Alcances: 'openid', 'profile', 'email' para información básica del usuario
- URI de redirección configurado según ambiente de despliegue

JWT es un estándar para transmitir información de forma segura entre partes como un objeto JSON firmado:

- Expiración de 8 horas con renovación automática si el usuario está activo
- Emisor específico 'data-pura-vida' con audiencia configurada para 'web', 'mobile', 'api'
- Algoritmo de firma RS256 para validación de integridad con rotación de claves mensual

**Autenticación Multifactor (MFA):**
Método de autenticación que requiere múltiples formas de verificación de identidad:

- **TOTP (Contraseña de Un Solo Uso Basada en Tiempo)**: Ventana de 3 períodos (90 segundos) para flexibilidad
- **Integración con SumSub**: Según sistemas de terceros definidos para KYC (Conoce a Tu Cliente)
- **Biometría**: Integración para prueba de vida en representantes legales
- 8 códigos de respaldo generados automáticamente con posibilidad de regeneración
- Códigos QR de 256x256 píxeles para mejor compatibilidad con dispositivos móviles

**Plantillas de Infraestructura con Terraform:**
Según directorio /infra/terraform/:

- Módulos reutilizables para cada componente en /components/
- Variables configurables para nombre, imagen, CPU y memoria
- 2 réplicas por defecto con escalado automático configurado hasta 6 réplicas
- Solicitudes de recursos de 250m CPU y 256Mi memoria por defecto
- Límites de recursos de 1 CPU y 1Gi memoria máximo
- Verificaciones de salud automáticas en endpoint /health con tiempo límite de 10 segundos

**Beneficios de la reutilización:**

- Desarrollo significativamente más rápido al aprovechar funcionalidades ya construidas y probadas
- Experiencia de usuario consistente en todos los componentes
- Mantenimiento simplificado donde un cambio se propaga automáticamente
- Mejora continua de la calidad a medida que los componentes se refinan con el uso

#### **2.5.4 Eficiencia**

La eficiencia busca optimizar el uso de recursos computacionales y financieros para ofrecer el mejor rendimiento posible con el menor costo operativo, utilizando responsablemente los recursos públicos.

El sistema debe proporcionar respuestas rápidas y una experiencia fluida mientras utiliza los recursos de manera inteligente, evitando desperdicios y optimizando costos.

**Objetivos de eficiencia:**

- Tiempos de respuesta que los usuarios perciban como instantáneos para operaciones comunes
- Uso óptimo de la capacidad de los servidores, manteniendo un balance eficiente
- Almacenamiento inteligente con compresión automática para reducir costos
- Escalado dinámico que ajusta recursos según la demanda real

**Configuraciones técnicas específicas para eficiencia:**

**Optimización de Consultas de Base de Datos:**
Optimización específica para La Bóveda, que debe almacenar datos en formato unificado independientemente del origen (relacional, documental, CSV, Excel):

- **Particionado automático**: Organización por fecha para datasets históricos
- **Índices optimizados**: Para búsquedas de texto completo en español (Costa Rica)
- **Relaciones entre datasets**: Índices para columnas que relacionan datasets del ecosistema
- **Trazabilidad completa**: Índices para auditoría de datos usados, no usados y descartados

**Estrategia de Almacenamiento AWS:**
Según proveedor cloud definido (AWS), se utilizarán servicios específicos de almacenamiento:

- **Almacenamiento activo**: Para datos activos frecuentemente accedidos
- **Almacenamiento tibio**: Para datos de acceso ocasional
- **Almacenamiento frío**: Para archivo a largo plazo
- **Almacenamiento de archivo**: Para archivo permanente
- **Políticas de ciclo de vida**: Migración automática según antigüedad y patrones de acceso

**Estrategia de Compresión específica para datasets:**

- **LZ4**: Compresión rápida para datasets recientes (< 7 días) con proporción 2:1
- **ZSTD**: Compresión alta para datasets archivados (> 30 días) con proporción 5:1
- **BZIP2**: Máxima compresión para almacenamiento frío (> 1 año) con proporción 8:1
- Migración automática según políticas de ciclo de vida de AWS

**Gestión de Recursos:**
Orquestación de contenedores según arquitectura seleccionada:

- **Núcleos de CPU**: 12 en solicitudes totales, 24 núcleos de CPU en límites
- **Memoria**: 24Gi en solicitudes totales, 48Gi memoria en límites
- **Escalado automático**: Configurado por componente según tecnología seleccionada
- **Disparadores de escalado**: CPU mayor a 75% o Memoria mayor a 85%
- **Comportamiento de escalado**: Máximo 1 instancia por escalado hacia arriba cada 2 minutos, máximo 1 por escalado hacia abajo cada 5 minutos

**Estrategias de optimización:**

El sistema implementa caché multicapa, que mantiene los datos más consultados en memoria de acceso rápido para respuestas inmediatas. Utiliza consultas optimizadas diseñadas para ser eficientes incluso con millones de registros, y compresión automática que reduce el espacio de almacenamiento sin pérdida de información. Incluye balanceo de carga inteligente que distribuye las consultas entre múltiples servidores para evitar sobrecargas.

#### **2.5.5 Claridad y Gestión de Complejidad**

La claridad asegura que un sistema técnicamente sofisticado sea comprensible y fácil de usar tanto para usuarios finales como para desarrolladores que lo mantienen.

Data Pura Vida debe ocultar su complejidad técnica detrás de interfaces simples e intuitivas. Los usuarios no deben necesitar conocimiento técnico para aprovechar sus capacidades.

**Principios de claridad:**

- Interfaces consistentes con navegación predecible y uniforme en toda la plataforma
- Mensajes comprensibles que explican claramente qué está ocurriendo, especialmente en casos de error
- Documentación automática que se mantiene actualizada sin intervención manual
- Configuración organizada de forma lógica y comprensible

**Configuraciones técnicas específicas para claridad:**

**Diseño de APIs (Interfaces de Programación):**
API RESTful (Transferencia de Estado Representacional) es un estilo arquitectónico para diseñar interfaces web que permite la comunicación entre sistemas de forma sencilla:

- **Endpoints semánticos**: /api/v1/datasets, /api/v1/users, /api/v1/dashboards
- **Métodos HTTP**: GET (consultar), POST (crear), PUT (actualizar completo), PATCH (actualizar parcial), DELETE (eliminar)
- **Códigos de Estado**: 200 (OK), 201 (Creado), 400 (Solicitud Incorrecta), 401 (No Autorizado), 404 (No Encontrado)
- **Tipo de Contenido**: application/json para intercambio de datos
- **Versionado**: /api/v1/ como prefijo para mantener compatibilidad hacia atrás

**Manejo de Errores Estructurado:**

- **Código semántico**: DATASET_NOT_FOUND, INVALID_CEDULA_FORMAT, UNAUTHORIZED_ACCESS
- **Mensaje descriptivo**: En español para usuarios finales costarricenses
- **Detalles técnicos**: Campo específico con error y valor esperado
- **ID de Correlación**: Para seguimiento y depuración entre componentes
- **Marca de Tiempo**: Formato ISO 8601 para consistencia internacional

**Categorías de Error específicas para Costa Rica:**

- **Errores de validación**: Formato de cédula costarricense, IBAN nacional, RTN
- **Errores de autenticación**: MFA, biometría, prueba de vida
- **Errores de autorización**: Permisos RBAC (Control de Acceso Basado en Roles), acceso por IP costarricense
- **Errores de lógica de negocio**: Reglas específicas del ecosistema nacional de datos

**Organización del Código:**
Según estructura del repositorio definida:

```
/data-pura-vida/
├── components/               # Cada componente independiente
│   ├── bioregistro-verde/   # Máximo 200 líneas por archivo
│   ├── la-boveda/           # Separación clara de responsabilidades
│   ├── motor-de-transformacion/ # Funciones específicas para ETDL
│   └── centro-de-visualizacion-y-consumo/
├── shared/                  # Código reutilizable
│   ├── utils/              # Utilidades comunes
│   └── auth/               # Autenticación centralizada
```

**Estándares de Código Limpio:**

- **Funciones**: Máximo 50 líneas, una responsabilidad específica
- **Clases**: Principio de responsabilidad única, máximo 300 líneas
- **Variables**: Nombres autodescriptivos en español/inglés según contexto
- **Complejidad ciclomática**: Máximo 15 por función (moderadamente complejo)
- **Documentación**: JSDoc para funciones públicas, comentarios en español para lógica compleja

**Gestión de Configuración:**
Configuración específica por ambiente:

- **Desarrollo**: Configuración local con bases de datos de prueba
- **Pruebas**: Ambiente de pruebas en AWS con datos simulados
- **Producción**: Ambiente productivo con datos reales costarricenses
- **Gestión de secretos**: Servicios AWS para credenciales sensibles
- **Variables de ambiente**: Configuración específica por ambiente sin valores fijos en código

**Gestión de complejidad:**

El sistema utiliza separación de responsabilidades, donde cada componente tiene una función específica y bien definida. Implementa abstracciones útiles que ocultan la complejidad técnica detrás de interfaces simples, y aplica patrones reconocibles con soluciones consistentes para problemas similares. Incluye escalamiento gradual que presenta funcionalidades básicas primero y avanzadas después.

**Implementación práctica:**

Las APIs (interfaces de programación) utilizan nomenclatura semánticamente clara que explica exactamente qué hacen. El manejo de errores es estructurado, proporcionando mensajes que incluyen qué ocurrió y cómo solucionarlo. La arquitectura se organiza en capas claras que separan presentación, lógica de negocio y datos.

#### **2.5.6 Métricas y SLAs Específicos**

**Métricas de Rendimiento alineadas con requerimientos**

**SLAs de Tiempo de Respuesta:**

- **Endpoints de API**: 95% de operaciones completadas en menos de 800ms
- **Generación de Tableros**: Menos de 5 segundos para gráficos simples
- **Carga de Datasets**: Máximo 30 minutos para procesamiento ETDL
- **Operaciones de Búsqueda**: Menos de 3 segundos para búsquedas en español

**Tiempos de Procesamiento ETDL específicos:**

- **Datasets pequeños** (menor a 1MB): máximo 10 minutos de procesamiento
- **Datasets medianos** (1-10MB): máximo 30 minutos
- **Datasets grandes** (10-100MB): máximo 2 horas
- **Datasets extra-grandes** (mayor a 100MB): máximo 8 horas con procesamiento por lotes

**SLAs de Disponibilidad para ecosistema nacional**

**Disponibilidad del Sistema:**

- **Sistema general**: 99.5% tiempo activo anual (máximo 43.8 horas inactivo/año)
- **Bio Registro Verde**: 99.7% tiempo activo (componente crítico para acceso)
- **La Bóveda**: 99.6% tiempo activo (almacenamiento central de datos)
- **Centro Visualización**: 99.0% tiempo activo (menor criticidad, más tolerante a fallas)
- **Ventana de mantenimiento**: Domingos 02:00-06:00 GMT-6 (horario costarricense)

**Planificación de Capacidad específico para Costa Rica**

**Proyecciones de Crecimiento basadas en adopción nacional:**

**Año 1 (Instituciones públicas principales):**

- 25,000 usuarios registrados (funcionarios públicos y ciudadanos early adopters)
- 5,000 datasets (datos de ministerios principales, TSE, BCCR)
- 2TB almacenamiento (documentos básicos, bases de datos institucionales core)
- 5M llamadas de API mensuales

**Año 3 (Sector privado integrado):**

- 100,000 usuarios (empresas medianas, algunas cámaras, organizaciones)
- 25,000 datasets (expansión gradual con datos comerciales selectos)
- 12TB almacenamiento (crecimiento orgánico con sector privado)
- 25M llamadas de API mensuales

**Año 5 (Ecosistema en maduración):**

- 250,000 usuarios (adopción amplia pero no total)
- 75,000 datasets (ecosistema robusto pero en crecimiento)
- 50TB almacenamiento (volumen significativo de datos históricos)
- 100M llamadas de API mensuales

#### **Aseguramiento de Calidad específica para Costa Rica**

**Puertas de Calidad de Código:**

- **Cobertura mínima**: 70% para código nuevo, 75% objetivo general
- **Validaciones nacionales**: 85% cobertura para validadores de cédula, IBAN, RTN
- **Cumplimiento de seguridad**: Cumplimiento básico Ley 8968, consideración GDPR e ISO 27001
- **Internacionalización**: Soporte principal para español costarricense

**Pruebas de Rendimiento específico:**

- **Pruebas de carga**: 500 usuarios concurrentes (estimación conservadora)
- **Pruebas de restricción geográfica**: Validación de acceso preferencial desde IPs costarricenses
- **Recuperación ante desastres**: Tiempo de recuperación máximo 8 horas
- **Integridad de datos**: 98% integridad en transferencias entre componentes (tolerancia a errores menores)

## 3. Stack Tecnológico

En cada una documentar versiones de frameworks, SDKs, lenguajes y herramientas utilizadas, así como sus restricciones y licencias

### Frontend

- **React.js**: Un framework de javascript especializado en web apps
- **Vite**: Empaquetador de react.
- **Tailwind CSS**: Librería para acelerar la creación de estilos mediante utilidades predefinidas.
- **Axios**: Libreria de javascript que permite hacer llamadas a rest APIs.
- **Formik + Yup**: Dos librerías de Javascript que harán la escritura de formularios más simple. Formik para la estructura de formularios, Yup para validación
- **Cognito**: Servicio de AWS que será usado para el registro de personas.
- **Plotly**: Librería para gráficos interactivos y avanzados con soporte para fuentes dinámicas y control total. Presione [aquí](https://www.chartjs.org/docs/latest/samples/information.html) para ver los gráficos que ofrecen.
- **AWS S3:** Servicio de almacenamiento escalable donde se alojan los archivos estáticos de la aplicación React (HTML, CSS, JS, imágenes, etc.).
- **AWS Cloudfront:** Red de distribución de contenido (CDN) que entrega los archivos desde S3 con baja latencia y alta velocidad, mejorando el rendimiento y la disponibilidad global.

### Backend

- **Python**: Lenguaje de programación versatil, con variedad de librerías y frameworks especializados en ETL e IA.
- **FastAPI**: Framework asíncrono en Python ideal para construir APIs rápidas y escalables.
- **RabbitMQ**: Broker de mensajería para comunicación asíncrona entre módulos backend.
- **EKS**: Servicio de Kubernetes gestionado por AWS para despliegue escalable y seguro del backend.
- **Apache Spark**: Framework especializado en procesamiento distribuido para ETL, validación y transformación de datos (usando PySpark).
- **Apache Airflow**:Orquestador de workflows para automatizar y monitorear procesos ETL con Spark, asegurando orden, trazabilidad y escalabilidad.
- **Helm**: Herramienta para gestionar despliegues Kubernetes mediante plantillas dinámicas.
- **Docker**: Será usado para crear imágenes de los distintos módulos del backend.

### Data

- **PostgreSQL:** Almacenamiento relacional de datos estructurados, ideal para usuarios y clientes.
- **DynamoDB:** Base de datos NoSQL para gestionar metadatos dinámicos y de alto rendimiento.
- **Redis:** Base de datos Clave Valor que sirve para caching o guardar información con TTL.
- **AWS S3:** Almacenamiento de objetos escalable y seguro para grandes volúmenes de datos no estructurados, como archivos.
- **Opensearch**: Elasticsearch gestionado por AWS que permite tener bases de datos time series altamente escalables.
- **AWS Glue:** Servicio ETL gestionado para la transformación y preparación de datos en flujos automatizados.\*tentativo, puede que prefiramos implementar nuestro propio cluster de spark en EKS organizado con airflow.
- **AWS RDS**: Es el servicio que AMazon ofrece para poder albergar bases de datos de PostgreSQL o MYSQL
- **AWS SageMaker:** Plataforma integral para crear, entrenar y desplegar modelos de machine learning de forma segura y escalable.
- **AWS KMS (Key Management Service):** Servicio de administración de claves criptográficas para cifrar y proteger datos sensibles en todos los servicios de AWS.

### AI

- **Hugging Face Transformers:** Uso de modelos preentrenados (ej. all-mpnet-base-v2) para generar embeddings semánticos de texto.
- **LangChain:** Orquestación de agentes inteligentes y manejo de flujos de lenguaje natural.
- **OpenAI (GPT-4):** Procesamiento de lenguaje natural, generación de texto y clasificación semántica.
- **Amazon SageMaker**: Entrenamiento, ajuste fino y despliegue de modelos personalizados de machine learning.
- **Hugging face**: para modelos ya entrenados que nos puedan servir (all-mpnet-base-v2 genera embeddings que podría servir para entrenar IA)


### Sistemas de Terceros

- **SumSub:** Sistema para poder realizar las comprobaciones KYC, AML y sdk para realizar pruebas de vida.
- **AWS:** Será nuestro cloud provider, y usaremos distintos servicios como S3, Glue, Cognito, etc.
- **Stripe:** Sistema que permite manejar los pagos dentro de nuestro sitio web.
- **Hugging Face:** Fuente para usar módelos de IA ya entrenados.

### Cloud

#### **Proveedor Principal**

- **Amazon Web Services (AWS)**: Plataforma de computación en la nube para toda la infraestructura de Data Pura Vida.

#### Servicios de Computación

- **Amazon EKS:** Kubernetes gestionado para contenedores del backend
- **AWS Lambda:** Funciones serverless para procesos específicos

#### **Servicios de Red**

- **AWS Application Load Balancer:** Balanceador de carga
- **Amazon CloudFront:** CDN para contenido estático
- **AWS VPC:** Red privada virtual para aislar recursos

#### **Servicios de Gestión**

- **AWS IAM:** Gestión de identidades y permisos
- **AWS CloudWatch:** Monitoreo y métricas (ya definido en DevOps)
- **AWS CloudTrail:** Auditoría de acciones

#### **Servicios Adiocionales**

- **Amazon SES:** Una opción gestionada por AWS para poder hacer envío de correos electrónico.

### DevOps y Testing

#### Infraestructura como Código (IaC)

- **AWS CloudFormation:** plantilla oficial de AWS para definir infraestructura como código.

- **Terraform:** herramienta para definir y aprovisionar la infraestructura en AWS mediante archivos .tf, asegurando consistencia entre ambientes y facilitando el versionamiento y rollback de cambios.

- **Helm:** gestor de paquetes para Kubernetes que permite definir despliegues mediante chart templates reutilizables, simplificando el despliegue de servicios backend.

#### Integración y Despliegue Continuo (CI/CD)

- **Github:** Para guardar codigo y control de versiones.

- **AWS CodePipeline:** herramienta nativa de AWS para construir pipelines de integración y despliegue continuo.

- **GitHub Actions:** seguirá siendo utilizado como integrador externo, especialmente para validar PRs, ejecutar linters, y disparar eventos hacia CodePipeline mediante webhooks.

#### Observabilidad y Monitoreo

- **AWS CloudWatch:** permite monitorear y supervisar toda la infraestructura desplegada en AWS, como RDS, DynamoDB y S3. Dado que todo el alojamiento en la nube se realizará en AWS, no es necesario utilizar otras herramientas externas como DataDog o Prometheus.

- **Grafana + CloudWatch + Prometheus:** para dashboards visuales personalizados directamente desde CloudWatch Metrics para los servicios de AWS, y Prometheus para los microservicios en EKS.

#### Pruebas Automatizadas

- **Pytest:** framework de pruebas para Python usado en pruebas unitarias para el backend.

- **Jest :** para pruebas unitarias de componentes React en el frontend.

- **Gatling:** para hacer pruebas de carga en la aplicación antes de poder pasarla a producción.

- **Postman + Newman:** se usarán para pruebas manuales y automáticas de la API REST. Newman permite integrar las colecciones en el CI.

#### Validación de Código y Estilo

- **ESLint:** verificación automática de estilo y seguridad en el frontend, con reglas personalizadas ancladas en el repositorio (.eslintrc.js).

- **Amazon CodeGuru Reviewer:** analiza código Python, detectando problemas de rendimiento y vulnerabilidades usando machine learning.

- **SonarQube:** se usará para realizar análisis estático del código backend y frontend, identificando automáticamente bugs, vulnerabilidades y malas prácticas. Estará integrado al pipeline de CI/CD para bloquear pull requests con problemas críticos y generar reportes de calidad y seguridad.

#### Seguridad

- **AWS Secrets Manager:** gestión segura de claves API, credenciales y tokens con rotación automática y control de acceso granular.

- **Dependabot:** para monitoreo de paquetes vulnerables desde GitHub. Se integra con CodePipeline para ejecutar pruebas de validación al actualizar dependencias.

## 4. Diseño de los componentes

En esta sección se detallará el diseño de los componentes previamente definidos en la sección de planeamiento. A cada uno se le aplicará un análisis de frontend, backend y datos, según corresponda. Además, existe la posibilidad de incluir prototipos en forma de pruebas de concepto. También se especificará cómo se llevará a cabo el proceso de pruebas e integración, despliegue y mantenimiento.

Antes de comenzar cabe por dejar en claro algunas especificaciones generales que se verán a lo largo de todo el diseño de los componentes:

- Todos los microservicios del backend estarán desplegados en un cluster de EKS.

- Se tendrá un API general para todo el backend, para poder acceder a las funcionalidades de todos los microservicios se debde consultar a dicha API (será RESTful). Además, estará construida en FastAPI, para favorecernos de sus características asincrónicas que la hacen sumamente rápida y apta para manejar carga pesada. Estará desplegada en el cluster de EKS, como un deployment con N replicas (Antes de pasar a producción se le realizarán pruebas de carga con Gatling, para poder determinar exactamente cuantas replicas ocupará).

### 4.1. Bioregistro

Este componente es el punto de entrada al sistema, tiene como propósito registrar distintos tipos de usuarios y adaptarse dinámicamente a sus requerimientos de autenticación.

Los tipos de usuarios que se podrán registrar en la plataforma son los siguientes :

- **Usuarios con Cédula Física**: Esto incluye a cualquier persona física que tenga cédula costarricense.

- **Usuarios con Cédula Jurídica**: Esta capa incluye una amplia variedad de colectivos que pueden aportar datasets de valor.
  - **Empresas privadas**: Incluye PYMES y Sociedades Anónimas (S.A).
  - **Empresas públicas y entes estatales**: Abarca instituciones autónomas, empresas estatales, empresas municipales, y Ministerios.
  - **Cámaras y gremios**: Incluye cámaras empresariales y gremios profesionales o técnicos.
  - **Universidades y centros académicos**: Comprende universidades públicas y privadas, así como sus escuelas, facultades y centros de investigación.

Asimismo, se adjunta una descripción de que es cada uno de los colectivos listados junto con que aporte pueden dar a Data Pura Vida,que información se les va a solicitar para poder garantizar que son empresas verdaderas y solicitadas por sus representantes reales (Cabe aclarar que todo documento PDF debe venir con firma digital):

#### **Empresas privadas**

Organizaciones con fines de lucro que operan en sectores diversos. Se dividen principalmente en:

**PYMES (Pequeñas y Medianas Empresas)**:
Empresas de menor escala que operan en comercio, manufactura ligera, servicios digitales, turismo, entre otros. Dentro de ellas pueden haber subdivisiones.

- **Actividad diaria**: ventas, atención al cliente, manejo de inventario, facturación, pagos, operaciones locales.
- **Datos potenciales**: consumo local, comportamiento de clientes, tiempos de entrega, cadenas de distribución.
- **Documentos necesarios para Identificarla**:
  - Certificación de personería jurídica: Contiene la información de la empresa como su nombre, cédula jurídica, tipo de sociedad, nombre del representante.
  - Cédula del representante legal: Debe coincidir con el de la certificación de personería jurídica.
  - Nombre y Apellido del representante.
  - Cédula jurídica: Debe coincidir con la certificación de personería jurídica.
  - Correo Institucional: correo electrónico del encargado de la institución.
  - Acta Constitutiva y Estatutos: Es un acta que establece la existencia legal de la empresa.
  - Constancia de incripción en el PYME: Demuestra que está registrada en el MEIC y cumple los requisitos para ser PYME.
  - Departamento a Registrar: Se debe registrar a que departamento de la empresa pertenece el registro.



**Sociedades Anónimas (S.A.)**
Empresas grandes con estructura formal, juntas directivas y accionistas. Comunes en construcción, industria, finanzas o tecnología.
- **Actividad diaria**: operación por departamentos, contratación de proveedores, desarrollo de productos, comercio exterior.
- **Datos potenciales**: operaciones financieras, productividad, logística, desempeño empresarial.
- **Documentos necesarios para Identificarla**:
  - Certificación de personería jurídica: Contiene la información de la empresa como su nombre, cédula jurídica, tipo de sociedad, nombre del representante.
  - Cédula jurídica: Debe coincidir con la certificación de personería jurídica.
  - Cédula del representante legal: Debe coincidir con el de la certificación de personería jurídica.
  - Nombre y Apellido del representante.
  - Correo Institucional: correo electrónico del encargado de la institución.
  - Estatutos sociales: Documento que establece la organización, funcionamiento, objeto social, entre otra información valiosa sobre la empresa.
  - Certificado de Registro Mercantil: Documento que certifica la inscripción de la empresa en el Registro Mercantil.
  - Certificado de Existencia: Documento legal que certifica la existencia de la empresa.
  - Departamento a Registrar: Se debe registrar a que departamento de la empresa pertenece el registro.


#### **Empresas públicas y entes estatales**

Entidades que operan con fondos públicos y ofrecen servicios esenciales.

**Instituciones autónomas**

Ejemplos: CCSS, ICE, INS, TSE.
- **Actividad diaria**: prestación de servicios de salud, energía, seguros, agua, telecomunicaciones.
- **Datos potenciales**: cobertura geográfica, consumo, atención médica, reclamos ciudadanos.
- **Documentos necesarios para Identificarla**:
  - Cédula Jurídica: adjuntar la cédula jurídica con el formato "4-000-NNNNNN"
  - Nota oficial con membrete institucional: Nombre completo de la persona que actuará como representante de la institución, con firma digital de un funcionario autorizado.
  - Cédula del representante legal: Debe coincidir con el de la certificación de personería jurídica.
  - Nombre y Apellido del representante.
  - Correo Institucional: correo electrónico del encargado de la institución.
  - Acta de Resolución Interna: Un acta firmada que describa la resolución dada internamente en el ente estatal.
  - Departamento a Registrar: Se debe registrar a que departamento de la empresa pertenece el registro.

**Empresas estatales**
Ejemplos: RECOPE, RACSA.
- **Actividad diaria**: importación, distribución de bienes estratégicos, operación con entes reguladores.
- **Datos potenciales**: consumo nacional, logística, demanda energética.
- **Documentos necesarios para Identificarla**:
  - Cédula Jurídica: adjuntar la cédula jurídica con el formato "3-NNN-NNNN"
  - Certificación de personería jurídica: Contiene la información de la empresa como su nombre, cédula jurídica, nombre del representante.
  - Nota oficial con membrete institucional: Nombre completo de la persona que actuará como representante de la institución, con firma digital de un funcionario autorizado.
  - Cédula del representante legal: Debe coincidir con el de la certificación de personería jurídica.
  - Nombre y Apellido del representante del órgano.
  - Correo Institucional: correo electrónico del encargado de la institución.
  - Acta de Resolución Interna: Un acta firmada que describa la resolución dada internamente en el ente estatal.
  - Departamento a Registrar: Se debe registrar a que departamento de la empresa pertenece el registro.

**Empresas municipales**
Entidades creadas por municipalidades para servicios locales, un ejemplo es la ESPH (Empresa de Servicios Públicos de Heredia).
- **Actividad diaria**: recolección de residuos, parqueo, mantenimiento urbano, servicios culturales.
- **Datos potenciales**: desarrollo cantonal, planificación urbana, gestión ambiental.
- **Documentos necesarios para Identificarla**:
  - Cédula Jurídica: adjuntar la cédula jurídica.
  - Certificación de personería jurídica: Contiene la información de la empresa como su nombre, cédula jurídica, nombre del representante.
  - Nota oficial con membrete institucional: Nombre completo de la persona que actuará como representante de la institución, con firma digital de un funcionario autorizado.
  - Cédula del representante legal: Debe coincidir con el de la certificación de personería jurídica.
  - Nombre y Apellido del representante.
  - Correo Institucional: correo electrónico del encargado de la institución.
  - Acuerdo Municipal: Un acta firmada que describa la resolución dada internamente en el ente municipal.


#### **Órganos del Poder Ejecutivo**
Ejemplos: MEP, MINAE, MOPT
- **Actividad diaria**: Formulación e implementación de políticas públicas, ejecución de programas nacionales, regulación sectorial, gestión presupuestaria y administrativa.
- **Datos potenciales**: Indicadores educativos, ambientales, de infraestructura y transporte; estadísticas de cobertura, acceso y calidad de servicios; y datos geoespaciales y sectoriales según competencia del ministerio.
- **Documentos necesarios para Identificarla**:
  - Oficio firmado por jefatura autorizada: Documento firmado por la jefatura con la autorización.
  - Cédula del representante legal: Cédula del representante del órgano.
  - Correo Institucional: correo electrónico del encargado de la institución.
  - Nombre y Apellido del representante del órgano.


#### **Cámaras y gremios**

Organizaciones que agrupan empresas o profesionales.

**Cámaras empresariales**
Ejemplos: Cámara de la Construcción, Cámara de Tecnologías de Información, Cámara de Exportadores de Flores.
- **Actividad diaria**: representación del sector, capacitaciones, generación de estudios y estadísticas.
- **Datos potenciales**: empleo, productividad, retos sectoriales, inversión.
- **Documentos necesarios para Identificarla**:
  - Certificación de personería jurídica: Contiene la información de la empresa como su nombre, cédula jurídica, nombre del representante.
  - Cédula Jurídica: adjuntar la cédula jurídica, que coincida con la de la certificación de personería jurídica.
  - Carta firmada por el comité o jefatura: Oficio que demuestre autorización de la cámara empresarial.
  - Cédula del representante legal: Debe coincidir con el de la certificación de personería jurídica.
  - Nombre y Apellido del representante.
  - Correo Institucional: correo electrónico del encargado de la institución.

**Gremios profesionales o técnicos**
Ejemplos: colegios de médicos, ingenieros, abogados.
- **Actividad diaria**: certificación profesional, formación continua, vigilancia del ejercicio profesional.
- **Datos potenciales**: matrícula, servicios ofrecidos, formación, cobertura geográfica.
- **Documentos necesarios para Identificarla**:
  - Certificación de personería jurídica: Contiene la información de la empresa como su nombre, cédula jurídica, nombre del representante.
  - Cédula Jurídica: adjuntar la cédula jurídica, que coincida con la de la certificación de personería jurídica.
  - Acta de asamblea constitutiva: Oficio que demuestre autorización de la cámara empresarial.
  - Cédula del representante legal: Debe coincidir con el de la certificación de personería jurídica.
  - Nombre y Apellido del representante.
  - Correo Institucional: correo electrónico del encargado de la institución.

#### **Universidades y centros académicos**

Instituciones de educación superior, tanto públicas como privadas, dedicadas a la formación profesional, la investigación científica y la extensión social. Dentro de estas operan subdivisiones como facultades, escuelas y centros de investigación (CI).

**Universidades públicas y privadas**
- **Actividad diaria**: matrícula, gestión de carreras, proyectos de investigación y extensión.
- **Datos potenciales**: rendimiento académico, estadísticas de graduación, impacto social.
- **Documentos necesarios para Identificarla**:
  - Cédula Jurídica: adjuntar la cédula jurídica, que coincida con la de la certificación de personería jurídica.
  - Nombramiento Interno: Carta que oficializa el encargado de hacer el registro en la plataforma.
  - Carta de la Unidad Interna: Oficio que da la autorización del unidad interna de la universidad:
  - Unidad Interna: Escuela, Facultad, Centro de Investigación.
  - Nombre de la unidad: Ingresar nombre específico.
  - Cédula del representante legal: Debe coincidir con el de la certificación de personería jurídica.
  - Nombre y Apellido del representante.
  - Correo Institucional: correo electrónico del encargado de la institución.


#### Llaves Tripartita

Una parte fundamental del sistema es la gestión tripartita de llaves. Se adoptó un esquema de tres claves: una asignada al representante designado por la empresa para su registro, otra para cada usuario secundario de la empresa, y una tercera bajo control de Data Pura Vida.
El mecanismo se basa en la comparación de una Data Encryption Key (DEK), la cual es cifrada con una Key Encryption Key (KEK) específica para cada parte involucrada.
Los detalles sobre cuándo, dónde y cómo se utiliza este esquema se ampliarán en la sección de definición del backend, pero por ahora esta descripción representa la visión de alto nivel.

#### Diseño del Frontend

##### Plataforma de Autenticación

Primero se describirá cómo se realizará en el frontend el proceso de registro e inicio de sesión para personas físicas, ya que los conjuntos no tienen un inicio de sesión propio, sino que solo cuentan con creación de cuenta, la cual es manejada posteriormente por personas físicas que la agregan a su cuenta personal.

Dado que la plataforma será alojada en AWS, usaremos AWS Cognito para el registro y posterior inicio de sesión de las personas en la plataforma. Del servicio se utilizarán las siguientes características:

- Uso de JWT Tokens para autorizar el acceso a las APIs en EKS.
- Uso de Cognito User Pools que registren email, teléfono, cédula, nombre y apellidos.
- Uso de choice-based authentication para que los usuarios elijan cómo iniciar sesión (contraseña, Email OTP o SMS OTP).
- Uso del AuthFlow de USER_PASSWORD_AUTH, que incluirá un MFA obligatorio con Email OTP o SMS OTP.
- Uso del SDK de Cognito para agilizar este proceso. Sin embargo, el formulario de registro será manejado programáticamente por nosotros, ya que el estándar que ofrece Cognito no se adapta a nuestro caso de uso.

No hay que dejar de lado que un paso muy importante en nuestro sistema es la captura de imagen de la cédula y la prueba de vida, para comprobar que la persona que solicita la cuenta sea real. Por lo tanto, en el flujo de registro de una persona física, este paso se realizará antes de autorizar el registro en el sistema por medio de cognito.

Para implementar esta lógica se usará el sistema de terceros SumSub, ya que provee herramientas para:

- Verificación de ID (cédula en nuestro caso).
- Prueba de vida y detección de deepfake.
- Prueba de dirección, para verificar que la dirección física del usuario sea real.
- Revisión de AML.
- Revisión de KYC.

Para realizar todas estas tareas en nuestro frontend se utilizará el WebSDK que SumSub provee para React, que cuenta con todas las herramientas necesarias para implementar las opciones mencionadas.

El proceso de registro de las empresas será distinto, ya que requiere realizar tres tareas principales:

- Validación y completitud de los datos.
- Validación de personas asignadas.
- Asignación de llaves tripartitas.

Por ello no se usará Cognito para las empresas. Sin embargo, para la validación SumSub ofrece una solución de KYB (Know Your Business), que permite:

- Revisar el registro nacional para seleccionar la empresa.
- Verificar al encargado del registro mediante prueba de vida y verificación de cédula.
- Generar cuestionarios personalizados donde se pueden adjuntar documentos legales que SumSub aprobará.

Por lo tanto, la validación de empresas también será implementada con SumSub. El almacenamiento de información y la delegación de llaves tripartitas serán discutidos más adelante en la sección del backend.

Por otro lado, cabe aclarar que para poder llevar a cabo las validaciones con SumSub es necesario dirigirse a la página de SumSub y ahí generar flows. Los desarrolladores tendrán que crear estos flows con base en las especificaciones dadas sobre que información se le debe solicitar a cada tipo de usuario (los distintos tipos de jurídico y el físico)  que fue especificada previamente en este subcapítulo.

##### Arquitectura de Cliente

Nuestra arquitectura de cliente consistirá en Client Side Rendering con rendering estático, con una única capa dedicada a la web. Esta decisión se toma porque los bundles de React generados en el build de cada proyecto serán almacenados en un bucket de S3, el cual será servido a los clientes mediante el CDN provisto por CloudFront.

Por otro lado, uno de los requerimientos de este módulo es que solo puede ser accedido con IPs Costarricenses (El registro), por lo que cuando se desee acceder a la página de registro Cloudfront ejecutará un Lambda@Edge Function que revisará la IP del usuario y en caso de no ser de Costa Rica, no servirá dicha ruta del App.

Además, para acceder al backend se utilizará una única API, desarrollada en FastAPI. Se entrará en más detalles de dicha API más adelante.


##### Patrones de Diseño de Objetos

A Continuación el diagrama de clases del frontend del Bioregistro:

![Patrones de Diseño de Objetos](img/FrontBioregistro.png)

- **Caja Verde**: La caja verde representa el patrón de Chain of Responsability. Está asociado a los distintos tipos de forms que existen en el sistema, y gracias a la naturaleza del CoR, permite declararlos dinámicamente. Inclusive, permite que si en un futuro se desea agregar otra capa, sea sumamente sencillo.
- **Cajas Celeste**: Las cajas celestes representan el strategy pattern, ya que por medio de herencia se aisla los distintos tipos de forms para colectivos, y de colectivos.
- **Caja Roja**: Esta caja roja cumple dos funciones, de Singleton y de Facade. De singleton porque de esta manera solo existe una instancia que se conecta al API en todo momento. Además funciona como Facade ya que aisla toda la lógica de conexión con el API del backend en una sola clase.


##### Componentes Visuales

**Patrones y Principios**

- **Responsive Design**: Aunque el enfoque principal de nuestro sistema está en el uso desde web desktop, es importante implementar un diseño responsivo para que los usuarios puedan realizar el registro, prueba de vida y verificación de cédula de forma cómoda desde la cámara de sus celulares. Este diseño responsivo se logrará aprovechando las opciones que ofrece Tailwind CSS para distintos tamaños de pantalla, utilizando prefijos como sm:, md:, lg:, y xl:, que permiten adaptar los estilos según el dispositivo.

- **SOLID**:
  - Single Responsibility: Cada componente en el bioregistro solo tendrá una responsabilidad. Por ejemplo, el formulario que detecta si es persona física o un conjunto solo emplea esa tarea, o los componentes de verificación de SumSub son distintos y cada uno hace su propia tarea: uno para la prueba de vida, otro para la verificación de id, y así para todo componente.
  - Open Closed Principle: Los componentes de registro son dinámicos y están separados, gracias a esto, si en un futuro se desea agregar otro tipo de organización, tan solo se debe desarrollar dicho componente y de ahí la conexión con el resto del flujo será directa.
  - Liskov Substitution Principle: La herencia debe ser utilizada solo cuando es necesaria. Por ejemplo, para los formularios de documentos para empresas si es valioso usar una superclase, pero no tiene sentido agruparlos en una clase madre con el formulario de prueba de vida.
  - Interface Segregation Principle: No usaremos una interfáz enorme para agrupar a todo tipo de formulario, solo si es necesario se definirán, y cuando se haga se haŕan lo más específicas posibles. Por ejemplo, una interfáz madre para los procesos de SumSub que ocupen uso de camara.
  - Dependency Inversion Principle: Las clases nunca deben depender de implementaciones, deben usar las intefaces. Por ejemplo, la clase que agrupe los formularios para registro de organizaciones debe poder permitir cualquier tipo de cuestionario de documentos, independientemente de con que colectivo se este trabajando.

- **Dry principle**: En la medida de lo posible se usará la menor cantidad de código repetido. Dos ejemplos de esto son: gracias a que usaremos atomic design, componentes como botones o labels serán reutilizado no solo en el bioregistro, pero en todo el sistema; y otro ejemplo es que tanto en el registro de colectivos como de personas se pide prueba de vida, entonces se utilizará la misma clase para manejar ambas tareas.

- **Separation of Concern**: Se cumple este principio ya que las distintas capas del frontend estarán bien definidas. En la capa de datos solo se gestionarán los objetos como personas y colectivos. Luego por medio de CustomHooks se gestionará la lógica del ViewModel, por ejemplo, las funciones como GetLivenessCheck o AttachPDF. Y Finalmente la capa de Vista se dedicará a tan solo eso, hacer el render de los componentes.

- **Atomic Design**: Este es un patrón muy común en React, y se verá reflejado porque los componentes serán creados empezando por átomos, como bótones e inputs; Luego con moléculas, que por ejemplo podría ser un item de formulario que tenga un label, botón e input; Para después crear Organismos como los Formularios Completo; Para que después se junten todos en una página que será la que finalmente renderize todo.

- **MVVM**: Estamos usando React, así que MVC no era una opción, y el flujo que tenemos planeado de comunicación entre hooks y componentes se adapta a un MVVM. Se aplicará de la siguiente forma:
  - Model: Lo implementaremos en la conexión con la API (serán funciones), y también en los objetos que luego se insertarán en la base de datos (no vamos a poner la lógica de negocio acá, como recomiendan empresas como Microsoft, para que nuestra app no viole el principio de responsabilidad única ni la separación de responsabilidades) como los distintos tipos de organización, o las personas físicos.
  - View: Será toda la parte visual de los componentes, que van a seguir atomic design.
  - ViewModel: Se implementará en los custom hooks reutilizables que gestionan la lógica de negocio.


**Toolkits y Standards**:

- **Vite**: Se usará como servidor local para el desarrollo, y también para hacer el bundle de la aplicación.
- **React Router**: Herramienta que permite manejar un app de react por medio de rutas.
- **ESlint**: Se usará para mantener un estándar de código y evitar errores comunes.


##### Estructura de Carpetas

``` bash
frontend/
├── public/                   #Assets como imagenes
├── src/
│   ├── api/                  #Acá estarán las funciones del API
│   ├── model/                #Acá se almacenarán las clases del modelo
│   │   ├── Person
│   │   └── Collective
│   ├── components/           #Atomic Design
│   │   ├── atoms/            #Componentes más básicos
│   │   │   ├── Button.jsx
│   │   │   └── Icon.jsx
│   │   │
│   │   ├── molecules/
│   │   │   └── FormItem.jsx
│   │   │
│   │   ├── organisms/
│   │   │   ├── PersonalInfoForm.jsx
│   │   │   └── ProofOfAddressForm.jsx
│   │   │
│   │   └── templates/
│   │       ├── CollectiveForm.jsx
│   │       └── PersonForm.jsx
│   │
│   ├── hooks/                 #ViewModel
│   │   ├── useLivenessCheck.jsx
│   │   └── useIdVerification.jsx
│   │
│   ├── contexts/              #Contexto del form, que datos han sido registrados
│   │   └── FormContext.jsx
│   │
│   ├── pages/                 #Uso de las templates lista para formar una página completqa
│   │   ├── MainRegister.jsx
│   │   └── VerifyEmail.jsx
│   │
│   ├── styles/               #Tailwind
│   │   └──globals.css        #Configuración de Tailwind
│   │
│   ├── utils/                #Funciones DRY
│   │
│   └── App.tsx               #Punto de Entrada
│
│
└── tests/
    ├── unit/
    └── integration/
```

##### Diagrama del Front
A continuación se presenta el diagrama del frontend de Bioregistro. En él se muestra cómo el contenido estático generado por React se almacena en un bucket de S3, donde residen todos los componentes visuales, su ViewModel a través de funciones y custom hooks, y las clases modelo como Person y Collective.

También se indica que los componentes visuales están estilizados con Tailwind CSS. La interacción con el backend se realiza mediante el módulo apiConnector.

Finalmente, se incluye una Lambda@Edge function que, antes de que CloudFront entregue el HTML, verifica si la IP de acceso corresponde a Costa Rica, como parte de un filtro geográfico.


![image](img/DiagramaFrontRegistro.png)

#### Diseño del backend


##### Microservicios

A continuación se dará una explicación de todos los microservicios correspondientes al Bioregistro.


**1. identity-verification-service**

Este servicio se encarga de gestionar todo el flujo de autenticación a través de la plataforma SumSub.

Para personas físicas, realiza los siguientes procesos:

- Verificación de cédula.
- Prueba de vida y detección de deepfakes.
- Verificación de dirección física.

Para colectivos, se utilizará la funcionalidad Full KYB 2.0 de SumSub que es una verificación por IA y por personas física que incluye:

- Consulta al Registro Nacional para identificar el colectivo.
- Revisión de documentos legales según el tipo de entidad.
- Revisión de que representantes trabajen en dicha empresa.

Ahora bien dentro de él existirán los siguientes componentes:

- SumSubController: Expone los endpoints del servicio para que el API General pueda acceder a él, estos serán:
  - /sumsub/person/token: Para mandar al crear el Applicant Id en SumSub.
  - /sumsub/person/webhook: Para recibir aprobaciones de personas desde SumSub.
  - /sumsub/collective/token: Para mandar al crear el Applicant Id en SumSub.
  - /sumsub/collective/check-documents/collective-type : Manda los documentos legales de SumSub a Auto-KYB para verificarlos. Existe un endpoint por cada tipo de colectivo.
  - /sumsub/collective/manual-verification: Para que los colectivos tengan la opción de solicitar una verificación manual.
  - /sumsub/collective/webhook: Para recibir aprobaciones de colectivos desde SumSub.
- CollectiveService: Se encarga de abstraer las llamadas a los workflows de SumSub según el tipo de colectivo, y hacer el registro del applicant.
- PersonService:	Se encarga de registrar las personas en SumSub y generar UUIDs para los usuarios.
- WebHookProcessor:	Se encarga de procesar los resultados de las respuestas de SumSub.
- CollectiveVerificationRouter: Middleware que se encarga de ver si se hace verifación manual o por medio de SumSub a los colectivos.


A continuación se muestra el flujo completo de interacción entre frontend y este componente para verificar una persona física:

1. La persona inicia el proceso de verificación:
- Frontend llama a: POST /sumsub/person/token:
  ```json
  {
    "email": "email de la persona",
    "Nombre": "nombre de la persona",
    "Apellido1": "Primer apeliido de la persona",
    "Apellido2": "Segundo apellido de la persona",
    "Telefono": "telefono de la persona",
    "direccion": "dirección donde vive la persona"
  }
  ```
- El SumSubController dirige la carga al PersonService que se encargará de registrar el Applicant en SumSub y enviarle un UUID interno. Obtendrá de respuesta el Id interno de SumSub que se usará para realizar la verificación.
  - También en la tabla de SumSubApplicants se registrará el UUID interno, una fila llamada Approved en False, y todas las credenciales dadas. Esto permitirá que cuando las personas traten de registrarse solo puedan una ves este flag sea cambiado a True (Más detalles sobre el registro serán explicados en el registration-service).

- Se retorna al frontend:
  ```json
  {
    "SumSubId": "id-de-sumsub",
    "InternalId": "uuid-del-sistema"
  }
  ```
2. El sdk de SumSub realiza la prueba de vida, la verificación de id, y la prueba de dirección física:

- En este punto el proceso puede durar desde minutos a horas, por lo que se detiene el proceso.

3. Llamada al Webhook desde SumSub:
- Una vez SumSub haya finalizado el proceso de verificación procedera a llamar al endpoint (En el dashboard de SumSub se puede configurar una uri hacia donde mandar las verificaciones) del webhook por medio de una solicitud POST a /sumsub/person/webhook con la siguiente información:

  ```json
  {
    "event": "applicantApproved",
    "applicantId": "sumsub-uuid",
    "externalUserId": "uuid-interno-del-sistema",
    "timestamp": "2025-06-06T15:00:00Z"
  }
  ```
- Se envía dicha información a WebHookProcessor para que empiece el proceso de aprobación:
  - Se pone el estado en SumSubApplicants como approved en True.
  - Se genera un token UUID, el cual será guardado en Redis junto al UUID del usuario en SumSubApplicants, de la siguiente forma:

    ``` python
    import redis
    import uuid

    r = redis.Redis(host='localhost', port=6379, db=0)

    token = str(uuid.uuid4())
    sumsub_id = "abc123" #Este id viene desde el webhook

    r.setex(f"registration_token:{token}", 86400, sumsub_id) #Para que persista por 24 horas
    ```

  - Ya que se tiene el token se envía un mensaje por medio de RabbitMQ al Notification Service para que envíe un correo con un link al registro, que lleve de query parameter el token:
    ``` txt
    https://data-pura-vida.com/register/person?token=<token_uuid>
    ```
  - Más adelante, en el registration-service se dirá como se manejará el registro con base en dicho token de redis.

4. El proceso de verificación fue exitoso, se continua a registro.

Ahora, se muestra el flujo completo de interacción entre frontend y este componente para verificar un colectivo:

1. La persona representante del colectivo inicia el proceso de verificación:
- Frontend llama a: POST /sumsub/collective/token:
  ```json
  {
    "email": "persona@ejemplo.com"
  }
  ```
- El SumSubController dirige la carga al CollectiveService que se encargará de registrar el Applicant en SumSub y enviarle un UUID interno. Obtendrá de respuesta el Id interno de SumSub que se usará para realizar la verificación.

- Se retorna al frontend:
  ```json
  {
    "SumSubId": "id-de-sumsub",
    "InternalId": "uuid-del-sistema"
  }
  ```
2. El sdk de SumSub realiza la búsqueda de Colectivo en el registro nacional

3. El usuario adjunta al formulario los documentos legales según el tipo de colectivo, y los representantes que ya deben de estar previamente registrados en el sistema (Cabe aclarar que el administrador de la empresa que está haciendo la gestión del registro también debe de estar registrado en el sistema de Data Pura Vida)

- El frontend lo envía por medio de /sumsub/collective/check-documents/collective-type

  ```json
  {
    "applicantId": "sumsub-uuid",
    "Representatives": "[Lista de objetos de tipo PersonaFísica]",
    "Admin": "{Objeto de tipo PersonaFisica correspondiente al que está gestionando el registro del colectivo}",
    "Documents": "[Los documentos legales según el tipo de colectivo]"
  }
  ```

- El SumSubController dirige la ejecución al CollectiveService.

- Primero se revisará que ya el colectivo no haya sido registrado en el sistema.

- Despues se checkeará si los usuarios insertados en Representatives y Admin efectivamente existen en la base de datos de RDS. En dado caso se insertan registros a SumSubCollectiveApplicant, la cúal guardará el UUID del sistema, el Id del administrador, y el estado de aprobación del colectivo. Y también se guardarán en SumSubCollective un FK a los representantes en Representatives y al registro en SumSubCollectiveApplicant.

- Luego se encargará de enviar a los WorkFlows de SumSub la información de las empresas.

- También se encarga de subir los documentos legales a un S3 Bucket bajo un directorio que tenga como nombre el UUID. Dicha interacción se hace por medio del uso de Boto3 en python.

- En este punto el proceso puede durar desde minutos a horas, por lo que se detiene el registro de empresa en el frontend.

4. Llamada al Webhook desde SumSub:
- Una vez SumSub haya finalizado el proceso de verificación procederá a llamar al endpoint del webhook por medio de una solicitud POST a /sumsub/collective/webhook con la siguiente información:

  ```json
  {
    "event": "applicantApproved",
    "applicantId": "sumsub-uuid",
    "externalUserId": "uuid-interno-del-sistema",
    "timestamp": "2025-06-06T15:00:00Z"
  }
  ```

- Se envía dicha información a WebHookProcessor para que empiece el proceso de aprobación:
  - Se pone el estado en SumSubCollectiveApplicant como approved en True.
  - Se genera un token UUID, el cual será guardado en Redis junto al UUID del colectivo en SumSubCollectiveApplicant, de la siguiente forma:

    ``` python
    import redis
    import uuid

    r = redis.Redis(host='localhost', port=6379, db=0)

    token = str(uuid.uuid4())
    sumsub_id = "abc123" #Este id viene desde el webhook

    r.setex(f"collective-register:{token}", 86400, sumsub_id) #Para que persista por 24 horas
    ```

- Ya que se tiene el token se envía un mensaje por medio de RabbitMQ al Notification Service para que envíe un correo con un link a la creación de llaves tripartitas, que lleve de query parameter el token:

  ``` txt
  https://data-pura-vida.com/collective-register?token=<token_uuid>
  ```
  - Más adelante, en el  registration-service se dirá como se manejará el registro con base en dicho token de redis.

4. El proceso de verificación fue exitoso, se continua a creación de las llaves tripartita.

Ahora bien, en el caso de colectivos, puede suceder que SumSub no encuentre al colectivo en sus bases de datos. Si esto ocurre, se habilita una opción de revisión manual, la cual envía un mensaje al notification-service a través de RabbitMQ. Este servicio notificará a los administradores, quienes podrán completar la verificación manual desde el portal web del backoffice.

Previamente fue mencionado, pero a modo de aclaración cabe decir que los templates de revisión serán creados desde el SumSub Dashboard. con base en la información listada al inicio del capítulo. Posteriormente en el código podrán ser llamados de esta forma por medio de un request al API similar a este:

``` python
import requests
import time
import hmac
import hashlib
import base64

flow_name = "kyb_legal_doc_flow"

ts = str(int(time.time()))
sig_data = ts + 'POST' + '/resources/applicants?levelName=' + flow_name
signature = base64.b64encode(
    hmac.new(SECRET_KEY.encode(), sig_data.encode(), digestmod=hashlib.sha256).digest()
).decode()

headers = {
    "X-App-Token": APP_TOKEN,
    "X-App-Access-Sig": signature,
    "X-App-Access-Ts": ts,
    "Content-Type": "application/json"
}

data = {
    "externalUserId": external_user_id,
    "info": {
        "companyName": "Colectivo Pura Vida S.A.",
        "registrationNumber": "CR-123456789",
        "country": "CR",
        "email": "legal@colectivopv.cr"
    }
}
response = requests.post(
    f"https://api.sumsub.com/resources/applicants?levelName={flow_name}",
    headers=headers,
    json=data
)
```

**2. auth-service**

Este servicio es un facade de autenticación sobre Cognito, por el cuál los usuarios deberán pasar siempre antes de iniciar sesión. En el habrán los siguientes componentes:

- AuthController: Expone los endpoints del servicio para que el API General pueda acceder a él, estos serán:
  - /auth/login: Para realizar el login por medio de contraseña
  - /auth/login/otp: Para realizar el login por medio de OTP
  - /auth/login/mfa: Para realizar el login por medio de MFA
  - /auth/login/mfa/resend Para poder reenviar los tokens MFA en caso de ser necesario
  - /auth/login/verify-mfa Para poder revisar que el MFA sea satisfactorio
  - /auth/logout: Para la gestión del Logout de la aplicación
- CognitoService: Se encarga de abstraer las llamadas de signup, login, challenge y refresh.
- MFAService:	Lógica para MFA (enviar y validar OTP por SMS/email).
- AuthChoiceHandler:	Implementa lógica de choice-based auth (elegir entre OTP o pass).

A continuación se muestra el flujo completo de inicio de sesión con MFA en la arquitectura:

1. El usuario inicia sesión:
- Frontend llama a: POST /auth/login:

  ```json
  {
    "identifier": "santi@gmail.com",
    "authMethod": "password", // o "otp"
    "password": "****" // solo si es método "password"
  }
  ```
- AuthController recibe el request y llama a AuthChoiceHandler para enrutar según authMethod.

2. Verificación de credenciales (si es con contraseña)
- Si authMethod es "password":
  - AuthChoiceHandler llama a CognitoService.initiateAuth()
  - Cognito verifica credenciales.
    - Si están bien pero MFA está activado, responde con un Session y un ChallengeName: SMS_MFA o similar.
    - Si el usuario no tiene MFA activado, responde con el JWT Token directamente.

3. El frontend reacciona a la respuesta
- Si recibe ChallengeName y Session, el frontend muestra pantalla MFA.
- Luego procede a enviar una llamada a /auth/login/mfa para que el MFAService envié un mensaje por medio de rabbitMQ al notification-service. Para que así se envíe un correo electrónico con el pin.

4. Usuario envía su código MFA
- Frontend llama a: POST /auth/login/veriyf-mfa con:

  ```json
  {
    "code": "123456",
    "session": "eyJraWQiOi...",
    "identifier": "santi@gmail.com",
    "deliveryMethod": "email"
  }
  ```
- AuthController pasa a MFAService.verifyCode()
  - Llama a CognitoService.respondToAuthChallenge()
  - Si todo bien, devuelve los JWT tokens (ID, access, refresh).

5. Tokens son devueltos al frontend
- Frontend los guarda y los manda en cada request siguiente al backend.


Ahora bien, en caso de que el usuario decida iniciar sesión por medio de OTP el proceso es similar lo que cambia es que el primer request pide "OTP", y el sistema va a generar uno que se enviará por medio de SMS al usuario para que posteriormente pueda iniciar sesión.

Cabe aclarar que las interacciones entre los componentes de este microservicio se realizarán por medio de REST APIs. Por lo que cada uno de ellos estará escritos en FastAPI y recibirá las solicitudes por medio de dicha interfáz. Para cada componente se tendrá un archivo con los endpoints y la lógica del api, y otros con la lógica de negocio de cada uno.


**3. registration-service**

Ahora bien, el registration-service es el encargado de registrar tanto personas como colectivos en el sistema.

Con respecto al registro de personas se encarga de cargarlas a Cognito y también en la base de datos del bioregistro en RDS, mientras que con colectivos solo se registra en RDS, y los documentos legales que se habían guardado previamente en un S3 Bucket, se pasan al bucket oficial de documentos legales llamado "collective_data".

En el habrán los siguientes componentes:

- RegistrationController: Expone los endpoints del servicio para que el API General pueda acceder a él, estos serán:
 - /register/person: Registro de una persona física.
 - /register/collective: Registro de una organización/colectivo.
 - /register/collective/key-generation: Endpoint para llamar al KeyGenerationHandler.
 - /register/check-token: Revisa el token UUID generado por el identity-verification-service.
 - /register/person/generate-token: Genera un nuevo token UUID para poder registrar al usuario en el sistema.
 - /register/collective/generate-token: Genera un nuevo token UUID para poder registrar al colectivo en el sistema.
- TokenManager: Este componente se encargará de operar con los tokens.
- PersonRegistrationService: Este componente se encargará del crear el usuario en cognito y rds.
- CollectiveRegistrationService: Este componente se encargará del crear el usuario en rds, dynamo y cargar documentos al bucket adecuado.
- KeyGenerationHandler: Este componentes se encarga de comunicarse con el microservicio de key-management-service para crear las llaves tripartita

A continuación se presenta el flujo de registro de una persona física:

1. Verificación de token UUID:
- Apenas el usuario entra al sitio web de registro (Si lo hace de forma correcta fue siguiendo el link que se envió a su correo en el identity-verification-service)

- Se hace un POST con /register/check-token, y se pasa el control a TokenManager para que se verifica si el query parameter de token: registration_token:<TOKEN_UUID> existe.

- En dado caso se usa como clave en redis con el prefijo de registration_token, y si retorna un UUID de la tabla de SumSubApplicant signfica que ya el usuario fue aprobado. Si no retorna nada significa que o bien el UUID Token cumplió su TTL de 24 horas, o que se está intentando ingresar al registro de manera no oficial.

- Se retorna al frontend:

  ```json
  {
    "status": "approved"
  }
  ```

2. El usuario registra su contraseña en el frontend

- Hace un POST a /register/person:

  ```json
  {
    "token": "El mismo Token UUID de redis",
    "Password": "Contraseña del usuario"
  }
  ```

- Solo se solicita el password porque las credenciales ya habían sido obtenidas por medio del identity-verification-service. Si se volvieran a pedir, estariamos arriesgando que un usuario use credenciales reales en el identity-verification-service, pero en este servicio invente información.

- Primero se hace el registro del usuario en la cognito pool, y se extrae el UUID usado en dicha pool, para usarlo también en RDS, de esta forma se guarda simetría entre ambos sistemas. Se hace de la siguiente forma:

  ``` Python
  import boto3

  client = boto3.client('cognito-idp', region_name='us-east-1')

  #Se crea el usuario en cognito
  response = client.admin_create_user(
      UserPoolId='user-pool-id',
      Username='correo@ejemplo.com',
      UserAttributes=[
          {'Name': 'email', 'Value': 'correo@ejemplo.com'},
          {'Name': 'email_verified', 'Value': 'true'},
      ],
      MessageAction='SUPPRESS'
  )

  #Se registra su contraseña
  client.admin_set_user_password(
      UserPoolId='user-pool-id',
      Username='correo@ejemplo.com',
      Password='LaContraseniaQuePidioElUsuario123',
      Permanent=True
  )

  # Se extrae el UUID generado por Cognito
  sub = next(attr['Value'] for attr in response['User']['Attributes'] if attr['Name'] == 'sub')
  ```

3. Registro en el Sistema

- Una vez se obtiene el UUID de Cognito, también se obtiene el UUID de la tabla de SumSubApplicant volviendo a sacarlo de redis con el token por medio del TokenManager.

- Ahora con la información de SumSubApplicant y el UUID de Cognito se registra el usuario en la tabla de PersonaFisica.

4. Proceso de registro de persona física exitoso.


Otro proceso posible es el de creación de un nuevo token en caso de que el TTL haya muerto (el proceso de solicitar un nuevo token como colectivo es el mismo, solo cambia el path):

1. Desde el Frontend el usuario hace:
- POST /register/person/generate-token

  ```json
  {
    "email": "correo con el que se gestionó la verificación"
  }
  ```

- Esto lo enruta al TokenManager.

2. Verificación de Aprobación

- Con base en el correo que se envió desde el frontend se revisa la tabla de SumSubApplicant, para ver si en verdad existe un registro con dicha información, y en todo caso que realmente esté Aprobado.

- En caso de estar aprobado el TokenManager crea otro token en redis y se conecta al notification-service por medio de RabbitMQ y solicita el envío de un nuevo correo.

3. Ya el usuario puede volver a intentar con el nuevo correo.

Finalmente se presenta el flujo de registro de un Colectivo:

1. Verificación de token UUID:
- Apenas el usuario administrador del colectivo entra al sitio web de registro (Si lo hace de forma correcta fue siguiendo el link que se envió a su correo en el identity-verification-service)

- Se hace un POST con /register/check-token, y se pasa el control a TokenManager para que verifice si el query parameter de token: collective-register:<TOKEN_UUID> existe.

- En dado caso puede ser usado como clave en redis con el prefijo de registration_token, y si retorna un UUID de la tabla de SumSubApplicant signfica que ya el usuario fue aprobado. Si no retorna nada significa que o bien el UUID Token cumplió su TTL de 24 horas, o que se está intentando ingresar al registro de manera no oficial.

- Se retorna al frontend:

  ```json
  {
    "status": "approved"
  }
  ```

2. Se llama a la creación de KEKs (Key Encryption Key) y DEKs parciales
- Hace un POST a /register/collective/key-generation

  ```json
  {
    "token": "El mismo Token UUID de redis"
  }
  ```

- Se enruta al KeyGenerationHandler que llamará por medio de su REST API al key-management-service. Se le enviará el token UUID de redis para que haga la gestión de llaves tripartita.

- Se espera como valor de retorno:

  ```json
  {
    "admin_dek": "La DEK asignada al administrador del colectivo",
    "dpv_dek": "La DEK asignada a data pura vida",
    "representatives_dek": "[IdDelRepresentate : DEK del representante]"
  }
  ```
- Cabe aclarar que cada DEK es un dictionary (en el key-management-service se muestra de que consiste), que debe ser guardado en postgres como JSONB.

3. Registro de información:
Desde el frontend se hace

- POST /register/collective


- Se procede a hacer el registro de toda la información correspondiente al colectivo.

- Se crean los registros correspondientes a los representantes en la tabla de Representantes, en ella se guardan sus respectivas DEKs.

- Se crea el registro del colectivo en la tabla de Colectivo con su respectiva DEK.

- Se crea el registro en DEKDataPuraVida con la DEK del sistema y una referencia al colectivo que le corresponde.

- Se pasan todos los documentos del S3 Bucket temporal (Se conoce el directorio ya que es el mismo UUID de la tabla SumSubCollectiveApplicant) a "collective_data". Además se guarda referencia a dicha información en DynamoDB, y se usa el mismo Id que el usado en RDS para guardar el Colectivo para mantener simetría.

- Se crea un rol de IAM para que el colectivo pueda acceder a los datasets que suba, más explicación sobre como sirve esto se verá en el componente de la bóveda:
  - Se crea el json sobre el rol:
    ``` json
    {
      "RoleName": "DPV_DataAccess_Colectivo1234",
      "AssumeRolePolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
          {
            "Effect": "Allow", # esta política significa que es un rol de permisión
            "Principal": {
              "Federated": "cognito-identity.amazonaws.com" # El rol se asgina a suarios federados que vienen de cognito
            },
            "Action": "sts:AssumeRoleWithWebIdentity", # Es para que un usuario obtenga dicho rol temporalmente mediante su JWT Token de sts con duración limitada
            "Condition": {
              "StringEquals": {
                "cognito-identity.amazonaws.com:aud": "REGION:IDENTITY_POOL_ID" # Solo se puede usar el token si viene de ese cognito pool
              }
            }
          }
        ]
      },
      "Description": "Rol para acceder al dataset de Empresas 2024 en DPV"
    }
    ```

  - Se crea el rol en IAM de aws:

    ``` python
    import boto3
    import json

    iam = boto3.client('iam')

    role_name = 'DPV_DataAccess_Colectivo1234'

    policy_document = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "redshift-data:ExecuteStatement",         # Ejecutar SELECTs y otros SQL
                    "lakeformation:GetDataAccess",            # Permiso de LakeFormation para consultar datos
                ],
                "Resource": "*"
            }
        ]
    }
    response = iam.create_role(
        RoleName=role_name,
        AssumeRolePolicyDocument=json.dumps(assume_role_policy),
        Description="Rol para acceder a dataset Empresas 2024"
    )

    print("Rol creado:", response['Role']['Arn'])
    ```

Esos fueron los flujos principales del microservicio de registration-service

Cabe aclarar que las interacciones entre los componentes de este microservicio se realizarán por medio de REST APIs. Por lo que cada uno de ellos estará escritos en FastAPI y recibirá las solicitudes por medio de dicha interfáz. Para cada componente se tendrá un archivo con los endpoints y la lógica del api, y otros con la lógica de negocio de cada uno.

**4. key-management-service**

El key-management-service es un componente clave del bioregistro, ya que se encarga de la creación y distribución de las llaves en el esquema tripartito.

Durante el registro de una empresa, el servicio genera una Key Encryption Key (KEK) para cada parte involucrada: una para los representantes, otra para el administrador de la empresa, y una tercera para Data Pura Vida.

Estas KEKs se envían directamente a los usuarios y no se almacenan en la base de datos del sistema, lo cual desacopla el proceso de encriptación del acceso a los datasets de la empresa, permitiendo así client-side encryption.

En el habrán los siguientes componentes:

- KeyManagementController: Expone los endpoints del servicio para que el API General y otros microservicios puedan acceder a él, estos serán:
 - /encrypt/collective: Recibe el Token UUID desde el registration-service.
 - /encrypt/verify/user: Por medio de este endpoint el usuario representante manda su kek para su aprobación.
 - /encrypt/verify/admin: Por medio de este endpoint el usuario administrador manda su kek para aprobar a un representante.
- EncryptionManager: Este componente se encarga del proceso de encripción.
- DecryptionManager: Este componente se encarga del proceso de desencriptado.
- Generator: Este componente se encarga de generar las DEKs y KEKs.
  - Verificator: Se encarga de verificar a un representante.

A continuación algunos flujos del microservicio que muestrán cuando y donde se usa. Primeramente, el proceso de generación de KEKs y DEKs.

1. Llega el request a creación desde el registration-service:
- Por medio de POST /encrypt/collective

  ```json
  {
    "token": "El mismo Token UUID de redis"
  }
  ```
- el KeyManagementController pasa el control al Generator.

- Con dicho token se saca el UUID que se encuentra en redis por medio de: collective-register:<TOKEN_UUID>.

2. El UUID es obtenido exitosamente

- Ya con dicho UUID, se busca en la tabla de SumSubCollectiveApplicant para poder encontrar cual es la empresa y cual es el usuario administrador. De ahí también se revisa en SumSubCollective para verificar cuales son los usuarios representantes a los que se les desea asignar una KEK.

- Se obtienen los Ids de los usuarios representantes en la tabla de PersonaFísica, y el del administrador de la empresa.

3. Creación de keys
- El Generator llama al EncryptionManager por medio del API de FastAPI que posee y le envía los representantes para que sepa cuantas KEKs/DEKs debe generar:
  ```json
  {
    "representatives": "[Los ids en la base de datos de dichos usuarios]"
  }
  ```

- Cabe aclarar que el proceso de encripción a utilizar es un AES-GCM, que posee la robustes de AES y además da un tag que dice la validez de la encripción, para evitar que se hagan modificaciones (es como un checksum)

  ```Python
  from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
  from cryptography.hazmat.backends import default_backend
  import os
  import base64

  # Función para cifrar la DEK con un KEK usando AES-GCM
  def encrypt_dek_with_kek(dek: bytes, kek: bytes):
      iv = os.urandom(12)  # de 96 bits
      encryptor = Cipher(
          algorithms.AES(kek),
          modes.GCM(iv),
          backend=default_backend()
      ).encryptor()

      ciphertext = encryptor.update(dek) + encryptor.finalize()

      return { # se pasan a base64 para poder ser transmitidos en htttp
          'iv': base64.b64encode(iv).decode(),
          'ciphertext': base64.b64encode(ciphertext).decode(),
          'tag': base64.b64encode(encryptor.tag).decode()
      }

  def generar_tripleta_deks(representatives):

      # 1. Generación de clave maestra
      dek = os.urandom(32)  # se usan 256 bits

      # 2. Se crean KEKs para la empresa y data pura vida
      kek_empresa = os.urandom(32)
      kek_dpv = os.urandom(32)

      # 3. Cifrar la DEK con cada KEK
      data_empresa = {
          "dek": encrypt_dek_with_kek(dek, kek_empresa),
          "kek": kek_empresa
      }

      data_dpv = {
          "dek": encrypt_dek_with_kek(dek, kek_dpv),
          "kek": kek_dpv
      }

      # 4. Se crean las distintas keks y deks para los representantes
      data_representatives = []
      for elem in representatives:
          kek = os.urandom(32)
          data_representatives = {
              "id" = elem,
              "kek" = kek,
              "dek" = encrypt_dek_with_kek(dek, kek)
          }

      # 5. Se retorna los resultados
      return {
          'representantes': data_representatives,
          'empresa': data_empresa,
          'dpv': data_dpv,
      }
  ```

- Esta return lo obtiene el controller del EncryptionManager y genera un jsondump al cual le aplica codificación en base64 para que pueda ser pasado por medio de http.

4. Distribución y Guardado:

- Ya con el resultado del EncryptionManager el Generator se encarga de generar un mensaje por medio de RabbitMQ al notification-service para que envie por correo a los usuarios tanto representantes como el admin su kek.

- Ya que se distribuyeron las KEKs se devuelven los DEKs al registration service para que así pueda terminar el registro.

5. finalizó el proceso de creación de llaves tripartitas

Ahora, el otro punto importante en el key-management-service es el proceso de verificación de KEKs para poder aprobar un usuario representante.

1. Interacción del usuario representante:
- Desde el frontend hace un POST /encrypt/verify/user

  ```json
  {
    "user_kek": "kek del usuario en base64"
  }
  ```

- Luego de esto el KeyManagementController enruta al Verificator para que se encargue de primero que todo obtener el id del usuario de la tabla de Representantes, y crea una entrada en redis (del mismo modo que con los tokens UUID en el registration-service) con un TTL de 48 horas:

  ``` redis
    check_kek:<TOKEN_UUID> : [<ID_DEL_USUARIO>, <KEK_DEL_USUARIO>]
  ```

- Posteriormente se envía un mensaje por RabbitMQ al notification-service para que envíe un mensaje "push" a las notificaciones dentro del portal web al administrador de la empresa que diga "El usuario <USUARIO> está esperando su aprobación>", además en dicho mensaje se adjunta el TOKEN_UUID, para que posteriormente se vuelva enviar desde el frontend.

2. Interacción del administrador

- Desde el frontend hace un POST /encrypt/verify/user

  ```json
  {
    "admin_kek": "kek del usuario en base64",
    "token": "token uuid en redis"
  }
  ```

- Luego de esto el KeyManagementController enruta al Verificator para que se encargue de obtener todo de redis por medio del token.

- Una vez se obtiene la kek del usuario representante se saca la kek de Data pura vida desde DEKDataPuraVida para así empezar el proceso de validación de keks.

  ``` python
  from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
  from cryptography.hazmat.backends import default_backend
  import base64

  def decrypt_dek_with_kek(encrypted_data: dict, kek: bytes):

      iv = base64.b64decode(encrypted_data['iv'])
      ciphertext = base64.b64decode(encrypted_data['ciphertext'])
      tag = base64.b64decode(encrypted_data['tag'])

      decryptor = Cipher(
          algorithms.AES(kek),
          modes.GCM(iv, tag),
          backend=default_backend()
      ).decryptor()

      return decryptor.update(ciphertext) + decryptor.finalize()}



  def verify_keks(kek_user, kek_admin, kek_dpv, dek_user, dek_admin, dek_dpv ):

      dek1 = decrypt_dek_with_kek(dek_user, base64.b64decode(kek_user))
      dek2 = decrypt_dek_with_kek(dek_admin, base64.b64decode(kek_admin))
      dek3 = decrypt_dek_with_kek(dek_dpv, base64.b64decode(kek_dpv))

      if dek1 == dek2 == dek3:
          print("Aprobado test tripartita")
      else:
          print("Falló el test tripartita")
  ```

3. En caso de que las tres llaves coincidan entonces se aprueba la validación y se actualiza el estado del representante en Postgres a Aprobado. Además se comunica con rabbitMQ y el notification-service para que envie un correo al usuario para que sepa que su kek fue aprobado.


Esos fueron los flujos principales del microservicio de key-management-service.

Cabe aclarar que las interacciones entre los componentes de este microservicio, cuando no se hizo explicita en la explicación, es porque se realizarán por medio de REST APIs. Por lo que cada uno de ellos estará escrito en FastAPI y recibirá las solicitudes por medio de dicha interfáz. Para cada componente se tendrá un archivo con los endpoints y la lógica del api, y otros con la lógica de negocio de cada uno.


**5. notification-service**

Este componente es el encargado de desacoplar la lógica de notificación a usuarios, ya sea por medio de correos electrónicos o notificaciones internas de la aplicación, del resto del microservicio.

No expone ninguna interfaz HTTP para comunicarse con otros microservicios; todo su tráfico se gestiona exclusivamente a través de colas en RabbitMQ. Las colas que utilizará son las siguientes:

- manual-verification: Por acá se reciben mensajes para poder notificar al backoffice que deben aprobar manualmente una empresa.
- register: Para enviar correos con el link al registro una vez identity-verification-service haya terminado la validación de usuarios.
- mfa-mail: Por esta cola se reciben solicitudes de generar correos con el pin para MFA.
- send-token: Para poder reenviar un token_uuid del identity-verification-service.
- send-kek: Para enviar por correo las keks.
- verify-kek: Para enviar una notificación a traves de las notificaciones dentro de la página, para que un administrador apruebe un usuario.
- approve-dek: Para notificarle al key-management-service que apruebe el estado del usuario en Representantes a Approve.

Cabe aclarar que los componentes del bioregistro no publicarán mensajes directamente en las cola, se usará una estructura de exchange como la siguiente:

![image](img/bioexchange.png)

De esta forma se desacopla aún más la comunicación entre los otros componentes y notification-service, para que así en caso de ser necesarias modificaciones a la aquitectura en un futuro, el proceso sea más flexible.

Ahora bien, para realizar el envío de correos electrónicos se usará AWS SES, y se habilitará en us-east-1 y se le configurará un dominio especial del equipo de soporte de data pura vida.

Una vez configurado AWS SES desde la consola de aws se tendrán que definir plantillas en html para los distintos tipos de correo. A continuación de la estructura para un correo de register:

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Confirmación de Registro</title>
  </head>
  <body style="font-family: Arial, sans-serif;">
    <h2>¡Bienvenido/a a Data Pura Vida!</h2>
    <p>Hola {{ nombre }},</p>
    <p>Tu proceso de verificación ha sido aprobado exitosamente.</p>
    <p>Podés ingresar al sistema usando el siguiente enlace:</p>
    <p><a href="{{ link }}" style="padding: 10px 15px; background-color: #008f39; color: white; text-decoration: none;">Acceder a la plataforma</a></p>
    <p>Gracias por confiar en nosotros.</p>
    <p>— El equipo de Data Pura Vida</p>
  </body>
</html>
```

Luego, una vez seleccionada la plantilla html se enviará el correo de la siguiente manera:

```python
import boto3
from botocore.exceptions import ClientError

def render_verification_email(nombre, link):
    template = env.get_template("verification_approved.html")
    return template.render(nombre=nombre, link=link)

def send_email(to_address, subject, body_html, body_text):
    client = boto3.client('ses', region_name='us-east-1')
    try:
        response = client.send_email(
            Source='supporteam@datapuravida.com',
            Destination={'ToAddresses': [to_address]},
            Message={
                'Subject': {'Data': subject},
                'Body': {
                    'Text': {'Data': body_text},
                    'Html': {'Data': body_html}
                }
            }
        )
        print("Correo enviado:", response['MessageId'])
        return response
    except ClientError as e:
        print("Error al enviar correo:", e.response['Error']['Message'])
        raise
```

En cuanto al manejo de notificaciones dentro de la aplicación web, el flujo en el notification-service será el siguiente:

1. Cuando llega un mensaje a las colas manual-verification o verify-kek:

- Existe un webhook en la API de FastAPI que a su vez consume mensajes de esas colas.

- Si el usuario está activo (conectado vía WebSocket), el webhook envía la notificación directamente a través de la conexión abierta.

- Si el usuario no está activo, el webhook no puede enviar la notificación en tiempo real, por lo que guarda el mensaje en una tabla DynamoDB llamada "Notifications".

- Cuando el usuario se conecta, el webhook consulta la tabla "Notifications" para verificar si hay notificaciones pendientes para ese usuario.

- En caso de encontrar notificaciones, las recupera, las envía al usuario y luego las elimina de DynamoDB. Si no hay notificaciones, no se realiza ninguna acción adicional.


##### Diagramas de Clases

En esta sección se presentarán los distintos diagramas de clase correspondientes a cada microservicio descrito en la sección anterior. Para cada uno se explicará además cuales patrones de diseño fueron implementados. Además, cabe aclarar que en algunos microservicios aparecerán clases que ya se habían utilizado en otros. A nivel del diagrama, estas clases se muestran duplicadas para mayor claridad, pero en el código serán reutilizadas.

**1. identity-verification-service**

Primeramente, los patrones de diseño orientados a objetos utilizados son los siguientes:

- Morado: Representa un facade.
- Amarillo: Representa un observer.
- Naranja: Representa un dependency injection.
- Verde: Representa un strategy.
- Celeste: Muestra un factory.
- Café: Representa un singleton.

Ahora bien, las clases están organizadas de la siguiente manera:

El punto de entrada es el SumSubController, que actúa como facade para que otros microservicios y el API general del backend se comuniquen con este microservicio. Este controlador delega las llamadas a un observer mediante el EventManager, encargado de notificar a la lógica de negocio correspondiente según el tipo de llamada realizada al SumSubController.

Dentro de esa lógica se encuentran el WebHookProcessor, PersonService y CollectiveService, que reciben como dependencias los servicios de la segunda capa de facade.

En esta segunda capa se encuentran:

- RabbitMQMessager: abstrae el envío de mensajes al exchange del bioregistro.
- SumSubService: encapsula toda la comunicación con el sistema externo de SumSub.
- ApplicantService: se encarga de las operaciones sobre los aplicantes en RDS.
- TokenManager: gestiona la generación de tokens y su almacenamiento en Redis.
- DocumentManager: cambia dinámicamente entre S3Factory y DynamoFactory para guardar documentos.

Finalmente, existe una capa de repositorios gestionada mediante el patrón Factory. Además, cada conexión se maneja utilizando el patrón Singleton.

![identity clases](img/ClasesBioregistro1.png)

**2. auth-service**

Primeramente, los patrones de diseño orientados a objetos utilizados son los siguientes:

- Morado: Representa un facade.
- Amarillo: Representa un observer.
- Naranja: Representa un dependency injection.
- Verde: Representa un strategy.


Ahora bien, las clases tienen un funcionamiento muy simple, el punto de entrada es AuthController, que actúa como facade para que el API general pueda acceder al microservicio. Luego el EventManager se encarga de distribuir según lo que se pidio al AuthController. En este caso es el AuthChoiceHandler el que escucha, y decide cual es el tipo de login que se solicitó. Luego están las clases de MFAService y CognitoService  que se encargan de comunicarse con Cognito

![identity clases](img/ClasesBioregistro2.png)

**3. registration-service**

Primeramente, los patrones de diseño orientados a objetos utilizados son los siguientes:

- Morado: Representa un facade.
- Amarillo: Representa un observer.
- Naranja: Representa un dependency injection.
- Verde: Representa un strategy.
- Celeste: Muestra un factory.
- Café: Representa un singleton.

Ahora bien, las clases están organizadas de la siguiente manera:

El punto de entrada es el RegistrationController, que actúa como facade para que otros microservicios y el API general del backend se comuniquen con este microservicio. Este controlador delega las llamadas a un observer mediante el EventManager, encargado de notificar a la lógica de negocio correspondiente según el tipo de llamada realizada al RegistrationController.

Dentro de esa lógica se encuentran el TokenManager, PersonRegistrationService y CollectiveRegistrationService, que reciben como dependencias los servicios de la segunda capa de facade.

En esta segunda capa se encuentran:

- RabbitMQMessager: abstrae el envío de mensajes al exchange del bioregistro.
- Cognito: encapsula toda la comunicación con Cognito.
- RegApplicantService: se encarga de las operaciones sobre los aplicantes en RDS.
- TokenCoordinator: gestiona la generación de tokens y su almacenamiento en Redis.
- DocumentManager: cambia dinámicamente entre S3Factory y DynamoFactory para guardar y traer documentos.

Finalmente, existe una capa de repositorios gestionada mediante el patrón Factory. Además, cada conexión se maneja utilizando el patrón Singleton.

![identity clases](img/ClasesBioregistro3.png)


**4. key-management-service**

Primeramente, los patrones de diseño orientados a objetos utilizados son los siguientes:

- Morado: Representa un facade.
- Amarillo: Representa un observer.
- Naranja: Representa un dependency injection.
- Celeste: Muestra un factory.
- Café: Representa un singleton.

Ahora bien, las clases están organizadas de la siguiente manera:

El punto de entrada es el KeyManagementController, que actúa como facade para que otros microservicios y el API general del backend se comuniquen con este microservicio. Este controlador delega las llamadas a un observer mediante el EventManager, encargado de notificar a la lógica de negocio correspondiente según el tipo de llamada realizada al KeyManagementController.

Dentro de esa lógica se encuentran el Generator y Verificator, que reciben como dependencias los servicios de la segunda capa de facade.

En esta segunda capa se encuentran:

- RabbitMQMessager: abstrae el envío de mensajes al exchange del bioregistro.
- SumSubPersonService: encapsula las llamadas a las tablas de personas en RDS.
- EncryptionManager: se encarga de las operaciones de encripcion de DEkS y creacion de KEKs.
- DecryptionManager: se encarga de las operaciones Desencripcion de DEKs.
- DekService: gestiona el acceso a DEKs parciales en RDS.
- RedisController: Controla las operaciones de extraccion de UUIDs, guardado y salvado de KEKs.

Finalmente, existe una capa de repositorios gestionada mediante el patrón Factory. Además, cada conexión se maneja utilizando el patrón Singleton.

![identity clases](img/ClasesBioregistro4.png)


**5. notification-service**

Primeramente, los patrones de diseño orientados a objetos utilizados son los siguientes:

- Morado: Representa un facade.
- Celeste: Muestra un factory.
- Verde: Representa un strategy.

Ahora bien, las clases están organizadas de la siguiente manera:

Se cuenta con una clase abstracta QueueListener que provee la lógica y conexión a RabbitMQ. Esta clase es reutilizada por dos componentes principales:

- EmailSender: escucha mensajes destinados a ser reenviados por correo electrónico a través de AWS SES utilizando el SESService.
- NotificationConsumer: detecta la llegada de nuevas notificaciones que deben mostrarse dentro de la aplicación.

Además, existe una capa encargada de escuchar conexiones de usuarios al frontend para enviar notificaciones en tiempo real mediante el WebSocketController. En segundo plano, el NotificationConsumer verifica si llegan nuevas notificaciones. Si el usuario está conectado, se le muestran inmediatamente; de lo contrario, se almacenan en DynamoDB a través del NotificationManager, para que en la próxima conexión el WebSocketController se las muestre.

Finalmente, existe una capa de repositorios gestionada mediante el patrón Factory. Cada conexión es manejada utilizando el patrón Singleton.

![identity clases](img/ClasesBioregistro5.png)


##### Servicios en AWS

A continuación se presentan todos los servicios AWS con los que se operará en los microservicios del Bioregistro, además se listarán las configuraciones de hardware para cada uno

**EKS**
Será el lugar donde estarán contenerizados los distintos microservicios.

- **Configuración de Hardware:**
  - **Versión de Kubernetes:** 1.29 (o la más reciente compatible).
  - **Tipo de nodo:** Amazon EC2.
  - **Tipo de instancia:** t3.medium (2 vCPU, 4 GB RAM) o superior.


**RDS**
Base de datos relacional para almacenar datos estructurados de la aplicación. Se entrará en más detalle en el diseño de los datos.

- **Configuración de Hardware:**
  - **Motor:** PostgreSQL (o MySQL, MariaDB según necesidad).
  - **Versión:** PostgreSQL 15 (o la más reciente estable compatible).
  - **Tipo de instancia:** db.t3.medium (2 vCPU, 4 GB RAM) o superior.
  - **Almacenamiento:** General Purpose SSD (gp3) con tamaño escalable según la carga.
  - **Multi-AZ:** Activado para alta disponibilidad.

**DynamoDB**
Base de datos NoSQL escalable para almacenamiento de datos con acceso rápido y flexible. Se entrará en más detalle en el diseño de los datos.

- **Configuración:**
  - **Modo de capacidad:** On-Demand.
  - **Streams:** Habilitados para replicación o integración con otros servicios.


**S3**
Almacenamiento de objetos para archivos, backups y datos estáticos.

- **Configuración:**
  - **Versionado:** Activado para control de versiones y recuperación de datos.
  - **Lifecycle policies:** Para transición a almacenamiento más barato (Glacier) o eliminación automática.


**AWS SES**
Servicio para envío de correos electrónicos confiables y escalables.

- **Configuración:**
  - **Región:** us-east-1.
  - **Identidad verificada:** Dominios y correos electrónicos verificados.
  - **Políticas de envío:** Limitaciones y tasas configuradas para evitar bloqueos.
  - **Autenticación:** SPF, DKIM y DMARC configurados para mejorar entregabilidad.


**Amazon ElastiCache (Redis)**
Se usará para albergar el servicio de redis. Se entrará en más detalle en el diseño de los datos.

- **Configuración de Hardware:**
  - **Modo de cluster:** Cluster mode enabled para sharding o disabled para despliegues pequeños.
  - **Versión:** Redis 7.x o la más reciente estable compatible.
  - **Tipo de instancia:** cache.t3.medium (2 vCPU, 4 GB RAM) o superior.
  - **Multi-AZ:** Activado para alta disponibilidad (opcional).
  - **Seguridad:** VPC privada, grupos de seguridad restrictivos y cifrado en tránsito y en reposo activados.


##### Sistema de Monitoreo
El monitoreo del componente Bioregistro se implementará siguiendo una estrategia de observabilidad integral que permita supervisar en tiempo real el comportamiento, rendimiento y seguridad del microservicio. Esta estrategia se alinea con las tecnologías definidas en el stack tecnológico del proyecto.

**Arquitectura de Observabilidad**
El sistema de monitoreo se estructurará en tres pilares fundamentales que trabajarán de manera coordinada para proporcionar visibilidad completa del componente:

**1. Métricas y Rendimiento**
AWS CloudWatch será el servicio central para recopilar y almacenar métricas operacionales del Bioregistro. Se monitorizarán aspectos críticos como:

- **Métricas de negocio:** Cantidad de registros procesados por tipo de entidad (personas físicas vs jurídicas), tasa de éxito en validaciones documentales, tiempo promedio del proceso completo de registro, y cantidad de llaves tripartitas generadas diariamente.
- **Métricas de infraestructura:** Utilización de recursos del pod en EKS (CPU, memoria, red), latencia de las conexiones a bases de datos PostgreSQL y DynamoDB, y throughput de solicitudes HTTP procesadas.
- **Métricas de integración:** Disponibilidad y tiempo de respuesta de servicios externos como SumSub y Cognito, tasa de fallos en llamadas a APIs externas, y volumen de datos intercambiados con sistemas de terceros.

**Prometheus** complementará a **CloudWatch** recopilando métricas específicas del microservicio a través de un endpoint dedicado. Esto permitirá obtener métricas más granulares sobre el comportamiento interno de la aplicación, como contadores de operaciones específicas, histogramas de distribución de tiempos, y gauges para valores instantáneos.

**2. Visualización y Dashboards**
**Grafana** se utilizará como plataforma principal de visualización, integrándose tanto con CloudWatch como con Prometheus para crear dashboards interactivos que permitan:

- **Dashboard operacional:** Vista en tiempo real del estado general del Bioregistro, mostrando registros activos, distribución geográfica de solicitudes (verificando cumplimiento de restricción de IPs costarricenses), y estado de salud de todos los componentes.
- **Dashboard de validaciones:** Monitoreo específico del proceso de validación documental, incluyendo éxito/fallo de verificaciones con SumSub, tiempos de procesamiento de IA para validación de documentos, y distribución de tipos de documentos procesados.
- **Dashboard de seguridad:** Seguimiento de eventos relacionados con seguridad como intentos de acceso no autorizados, generación y uso de llaves criptográficas, y auditoría de accesos a datos sensibles según requerimientos de la Ley 8968.

**3. Logs y Trazabilidad**
El sistema de logging aprovechará **CloudWatch Logs** para centralizar todos los registros generados por el Bioregistro. Se implementará un esquema de logging estructurado que facilite:

- **Trazabilidad completa:** Cada transacción tendrá un identificador único de correlación que permitirá seguir su flujo desde el inicio del registro hasta la emisión de credenciales digitales.
- **Auditoría regulatoria:** Logs específicos para cumplimiento normativo, registrando accesos a datos personales, modificaciones de información sensible, y ejercicio de derechos ARCO por parte de los usuarios.
- **Diagnóstico de problemas:** Niveles de log diferenciados (INFO, WARN, ERROR) con contexto suficiente para identificar rápidamente la causa raíz de cualquier incidencia.

**Sistema de Alertas y Notificaciones**
Se configurará un sistema proactivo de alertas utilizando CloudWatch Alarms que notificará al equipo de operaciones cuando se detecten condiciones anómalas:
**Alertas críticas (respuesta inmediata requerida):**
- Fallo total del servicio o indisponibilidad del endpoint de health check
- Tasa de error superior al 20% en ventana de 5 minutos
- Fallo en la conexión con servicios críticos (Cognito, SumSub, bases de datos)
- Detección de múltiples intentos de acceso desde IPs no autorizadas

**Alertas de advertencia (revisión prioritaria):**
- Degradación del rendimiento con latencias superiores a 3 segundos
- Uso de recursos por encima del 80% de capacidad
- Incremento inusual en validaciones fallidas
- Acumulación de tareas en cola de procesamiento manual

**Alertas informativas (seguimiento regular):**
- Resumen diario de métricas operacionales
- Reporte semanal de tendencias y patrones
- Notificaciones de mantenimiento programado

**Monitoreo de Cumplimiento y Seguridad**
Dado el carácter sensible de los datos manejados por el Bioregistro, se implementarán controles específicos de monitoreo para garantizar el cumplimiento normativo:
- **Seguimiento de consentimientos:** Monitoreo del ciclo de vida de los consentimientos otorgados por usuarios, incluyendo fechas de otorgamiento, actualizaciones y revocaciones.
- **Auditoría de accesos:** Registro detallado de todos los accesos a datos personales, identificando quién accedió, cuándo, desde dónde y con qué propósito.
- **Monitoreo de retención de datos:** Seguimiento automatizado de los períodos de retención de datos según las políticas establecidas, con alertas para datos próximos a expirar.
- **Verificación de cifrado:** Monitoreo continuo del estado de cifrado de datos en tránsito y reposo, asegurando que no existan brechas de seguridad.

**Health Checks y Disponibilidad**
El microservicio implementará múltiples niveles de verificación de salud que serán monitoreados continuamente:

- **Liveness probe:** Verificación básica de que el servicio está activo y respondiendo, ejecutada cada 10 segundos por Kubernetes.
- **Readiness probe:** Verificación comprehensiva de que todas las dependencias están disponibles y el servicio puede procesar solicitudes, incluyendo conectividad con bases de datos, servicios externos y disponibilidad de recursos.
- **Deep health checks:** Verificaciones periódicas más exhaustivas que validan la integridad de configuraciones, certificados SSL, y correcta operación de funciones críticas.

**Análisis y Mejora Continua**
El sistema de monitoreo no solo detectará problemas, sino que proporcionará insights para la mejora continua:

- Análisis de tendencias: Identificación de patrones en el uso del sistema para optimizar recursos y predecir necesidades futuras.
- Detección de anomalías: Uso de las capacidades de CloudWatch para identificar comportamientos inusuales que podrían indicar problemas emergentes.
- Reportes de capacidad: Proyecciones basadas en datos históricos para planificar el crecimiento de la infraestructura.
- Optimización de costos: Análisis del uso de recursos para identificar oportunidades de optimización sin comprometer el rendimiento.

##### Modelo de seguridad detallado
El módulo de Bioregistro maneja información altamente sensible relacionada con personas naturales y jurídicas (incluyendo representantes legales, personas con poder legal, etc.). Su backend será asegurado mediante un conjunto de mecanismos orientados a prevenir accesos no autorizados, garantizar integridad, confidencialidad, trazabilidad y disponibilidad continua de los datos.

**1. Control de Acceso Granular**

**OAuth2 + JWT:** Toda operación sobre el bioregistro requerirá un token válido con permisos específicos. Estas herramientas serán implementado en el frontend por parte de AWS Cognito, pero su flujo de trabajo seguirá en el backend.

**RBAC (Role Based Access):** Se le otorgará permisos a los usuarios según el rol que desempeñen dentro del sistema; esto con el fin de limitar acceso a solo los recursos necesarios y evitar privilegios excesivos. Existiran 4 tipos de roles:

| Rol del Usuario                            | Descripción                          | Permisos sobre recursos del Bioregistro           |
| ------------------------------ | --------------------------------- | -------- |
| `bio:viewer` | Visualiza registros existentes                 | Lectura en PostgreSQL y DynamoDB    |
| `bio:editor `   | Crea y modifica registros, sin aprobarlos         | Lectura y escritura parcial     |
| `bio:approver`  | Aprueba, certifica o valida registros | Escritura total + validación cruzada     |
| `bio:admin`          | Gestión completa del módulo, incluyendo usuarios y configuración      | Acceso total y eliminación    |

- La equivalencia de estos roles en la base de datos se puede mapear de la siguiente manera:
  - Viewer: Son los usuarios en la tabla llamada AccesoDataset.
  - Editor: Esto hace referencia a los representantes de los colectivos, ubicados en la tabla de Representantes.
  - Approver: Hace referencia a los administradores del colectivo, se ubican en la tabla de cada colectivo.


**Asociacion de RBAC a las bases de datos del sistema:**
- **PostgreSQL:** Usado para almacenar entidades estructuradas.
  - Personas físicas/jurídicas, Certificados, Estados de validación, Trazas de auditoría
  - Se usan los roles exactamente como en la tabla anterior.
  - En la capa de acceso, se verifica el rol antes de ejecutar consultas SQL.

- **DynamoDB:** Usado para gestionar metadatos dinámicos y documentos JSON no estructurados.
  - Información adjunta, Historial de verificación, Pruebas de vida o firmas electrónicas.
  - En cada tabla DynamoDB, los accesos se segmentan con políticas AWS IAM condicionales según el rol (Condition: "bio:role" == "approver").

Ejemplo flujo autenticación:
```json
{
  "sub": "uuid",
  "email": "usuario@dominio.com",
  "custom:role": "bio:editor"
}
```

**AWS Identity and Access Management (IAM):** Permite definir de manera segura quién puede acceder a qué recursos y con qué nivel de permisos dentro del entorno en la nube. La implementación se hará con con políticas por rol, usando etiquetas.


| Caso de uso                            | Acción permitida                          | Servicio AWS           | Rol asociado
| ------------------------------ | --------------------------------- | -------- | ------------ |
| **Consulta de certificados validados** | `Vdynamodb:GetItem`, `Query`                 | DynamoDB    | `bio:viewer`, `bio:approver`   |
| **Carga de archivos adjuntos**   | `s3:PutObject`, `GetObject`         | Bucket S3     | `bio:editor`, `bio:approver` |
| **Lectura de llaves privadas**  | `secretsmanager:GetSecretValue` | Secrets Manager     | `bio:admin` |
| **Acceso a logs de auditoría**          | `logs:FilterLogEvents`     | CloudWatch Logs    | `bio:admin`, `bio:approver` |


Ejemplo politica por rol:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["dynamodb:PutItem", "dynamodb:GetItem"],
      "Resource": "arn:aws:dynamodb:::table/bioregistro_certificados"
    },
    {
      "Effect": "Allow",
      "Action": ["s3:PutObject"],
      "Resource": "arn:aws:s3:::bio-adjuntos/*"
    }
  ]
}
```
**3. Validación de entradas**

Para proteger el backend del Bioregistro, se implementarán validaciones estrictas de datos en todas las capas de entrada. Estas validaciones estarán directamente integradas en los endpoints de la API desarrollados con FastAPI, usando las capacidades de tipado y validación de Pydantic, reforzadas con validadores personalizados.

La aplicación de esto sucede en los siguientes eventos:
- En todos los endpoints RESTful del Bioregistro (registro, modificación, eliminación, consulta).
- En validaciones internas antes de realizar operaciones sobre la base de datos.

**Validaciones estructurales:**
- Uso de tipos estrictos: `str`, `int`, `EmailStr`, `UUID`, `datetime`.
- Validaciones de longitud y formato (Regex).

Ejemplo de validación estructural:
```python
from pydantic import BaseModel, Field, EmailStr
class RegistroResidente(BaseModel):
    cedula: str = Field(..., regex=r'^\d{9}$')
    nombre: str = Field(..., max_length=60)
    correo: EmailStr
    telefono: str = Field(..., regex=r'^\d{8}$')
    fechaNacimiento: str
```
**Prevención de Inyecciones:**
- **SQL Injection:** al usar ORMs o query builders con `SQLALCHEMY`, evitando la concatenación de strings en queries.
-**NoSQL Injection:** validación de claves primarias/secundarias con tipos y formatos válidos.


**Validadores personalizados:**
Se emplearán funciones decoradoras (@validator) para definir reglas de negocio complejas

ejemplo:
```python
from pydantic import validator
class Registro(BaseModel):
    fechaNacimiento: datetime
    fechaDefuncion: Optional[datetime]

    @validator("fechaDefuncion")
    def check_fechas(cls, v, values):
        if v and "fechaNacimiento" in values and v < values["fechaNacimiento"]:
            raise ValueError("La fecha de defunción no puede ser anterior a la fecha de nacimiento.")
        return v
```


**4. Auditoría y Registro de Actividades**
Se hará con el objetivo de monitorear en tiempo real y registrar de forma persistente todos los accesos, modificaciones y acciones críticas sobre los datos del Bioregistro, tanto por parte de usuarios humanos como de servicios automatizados.

**Acciones que se auditarán**

- Inicios y cierres de sesión con Cognito
- Accesos exitosos y fallidos a endpoints sensibles del backend
- Cambios de configuración y roles dentro del sistema
- Accesos o intentos de acceso a recursos restringidos
- Uso de claves KMS para cifrado/descifrado de datos sensibles
- Acciones administrativas sobre recursos de AWS vinculados al Bioregistro

**Implementación Técnica**

###### Middleware de FastAPI
Se desarrollará un middleware de auditoría personalizado que capture metadatos clave en cada interacción:

  - IP de origen
  - Usuario autenticado
  - Timestamp
  - Endpoint accedido
  - Método HTTP
  - Código de respuesta (status code)
  - Rol del usuario


Los registros se almacenarán en DynamoDB, aprovechando su alto rendimiento y consulta eficiente para logs estructurados.

Ejemplo:
```json
{
  "PK": "user#1234",
  "SK": "log#2025-06-05T17:42:13Z",
  "endpoint": "/residente/456",
  "action": "UPDATE",
  "statusCode": 403,
  "ip": "190.10.25.6",
  "role": "PersonalAutorizado"
}
```
###### AWS CloudWatch

Se tiene una visualización en tiempo real de los logs generados por el backend. Se realiza la creación de alarmas automatizadas para eventos sospechosos o violaciones de políticas como las siguientes:
- Más de 5 intentos fallidos de autenticación en 60 segundos.
- Acceso masivo a datos de residentes por un mismo usuario.
- Actividades fuera del horario laboral.

###### Integración con AWS CloudTrail

Para capturar eventos directamente desde el entorno AWS, se utilizará AWS CloudTrail como complemento de auditoría. Este registra todas las llamadas a la API de AWS, incluyendo:
- Uso de AWS KMS
- Acceso a buckets S3 con documentos biométricos
- Cambios a roles, políticas y grupos de IAM

Beneficios:

- Trazabilidad completa de acciones en servicios críticos del backend
- Integración con AWS KMS para detectar uso indebido de claves
- Compatible con otros servicios de AWS para ejecutar consultas avanzadas sobre logs


**5. Cifrado de Datos**
El módulo Bioregistro maneja información sensible relacionada con la identidad de los residentes, como números de identificación, datos biométricos y documentos oficiales. Por ello, se implementa lo siguiente:

| Tipo de Cifrado                            | Descripción                          | Aplicación en el Bioregistro           | Herramientas/Protocolos Usados | Caso de Uso |
| ------------------------------ | --------------------------------- | -------- | ------------ | -------------- |
| **Cifrado en Tránsito** | Protege los datos mientras se transmiten entre el cliente y el servidor. Evita intercepciones o manipulaciones.                 | Aplicado en todas las solicitudes HTTP entre frontend y backend, y entre backend y servicios como Amazon Cognito, PostgreSQL y RabbitMQ..    | TLS 1.3, HTTPS obligatorio con AWS Certificate Manager   |La adopción de HTTPS obligatorio será gestionada mediante certificados válidos y renovables (por ejemplo, con AWS Certificate Manager). |
| **Cifrado en Reposo**   | Protege los datos almacenados en bases de datos o archivos para evitar acceso no autorizado.         | Aplica al almacenamiento de cédulas, datos biométricos y documentos subidos a S3 o PostgreSQL.    | AES-256, PostgreSQL TDE, S3 + SSE-KMS |Para almacenamiento de documentos e imágenes biométricas en Amazon S3, se aplicará cifrado del lado del servidor (SSE) con claves gestionadas por AWS Key Management Service (KMS). |

**Uso de AWS KMS para Gestión de Claves**

AWS KMS permitirá la centralización del manejo de claves de cifrado, incluyendo:
- Rotación automática de claves
- Control de acceso por política granular
- Auditoría completa mediante integración con AWS CloudTrail
- Cada operación de cifrado y descifrado queda registrada, permitiendo trazabilidad sobre qué usuario accedió a qué recurso, cuándo y con qué clave.


**Protección Extendida**

Se combinará cifrado del lado del cliente con el cifrado del lado del servidor, especialmente en flujos sensibles como subida de documentos biométricos desde el frontend. Esto permite que los datos ya lleguen cifrados a S3, agregando una capa adicional de defensa en caso de vulneración de acceso al bucket.


**Verificación de Implementación**

Se integran pruebas automáticas en los pipelines de CI para asegurar que:

- Ninguna transmisión ocurra por HTTP.
- Los datos almacenados no estén en texto plano.
- Las operaciones de cifrado sean exitosas y rastreables en CloudWatch.

Estas medidas aseguran la confidencialidad de los datos personales y fortalecen la postura de cumplimiento del proyecto con respecto a normativas como la Ley 8968 de Protección de la Persona frente al tratamiento de sus datos personales y estándares como ISO/IEC 27001.

**6. Protección contra Abuso y Ataques**

| Categoría                           | Estrategia                          | Herramienta / Tecnología            | Caso de uso
| ------------------------------ | --------------------------------- | -------- | ------------ |
| **Limitación de tráfico** | 	Aplicar límites de solicitudes por IP por endpoint y método.                 | AWS API Gateway + FastAPI Middleware    | Evitar que un usuario o bot consulte masivamente los datos de residentes en un corto periodo.   |
| **Bloqueo por patrones**   | Identificación de IPs con comportamiento malicioso y bloqueo automático.         | AWS WAF     | Bloqueo de IPs que intenten manipular repetidamente URLs como `/residente/1234/edit` |
| **Protección contra bots**  | 	Detección de bots mediante análisis de headers y frecuencia. | Middleware personalizado + WAF     | Evita scraping automático de datos personales o intentos de acceso automatizado al registro. |
| **Protección DoS/Brute Force**          | Prevención de ataques de denegación de servicio o fuerza bruta en login.     | AWS Shield + CloudWatch    | Resguarda el endpoint de autenticación Cognito usado por el personal autorizado. |
| **Validación profunda de inputs**          | Inspección de JSON y parámetros de URL para detectar inyecciones     | Pydantic + validadores personalizados    | Prevenir que usuarios maliciosos inserten comandos o scripts en campos como nombre o dirección. |

**7. Gestión de Secretos con AWS Secrets Manager**

Se usará AWS Secrets Manager como proveedor principal para almacenar, cifrar y rotar automáticamente los secretos necesarios del backend. Este servicio permite:
- Cifrado automático con AWS KMS de los valores sensibles.
- Control de acceso detallado mediante políticas IAM por recurso.
- Auditoría completa con AWS CloudTrail.
- Integración directa desde FastAPI usando AWS SDK (boto3).

| Nombre del Secreto  |	Contenido     |	Servicio  |	Rotación Automática
| ---------- | --- | ---| --- |
| `bioregistro/db_credentials`	| Usuario y contraseña para acceder a PostgreSQL	| PostgreSQL	| Activada cada 30 días
| `bioregistro/jwt_signing_key`	| Llave privada para firmar JWT |	FastAPI auth middleware	|  Solo lectura
| `bioregistro/rabbitmq_credentials` |	Usuario y contraseña para conectarse a RabbitMQ	| RabbitMQ (eventos)|  |
| `bioregistro/s3_upload_token` |	Token temporal para subida de archivos desde frontend	| S3 + Cognito	|  12h de disponibilidad |

Ejemplo de acceso seguro desde FastAPI

```py
import boto3
import json

def get_secret(secret_name):
    client = boto3.client("secretsmanager", region_name="us-east-1")
    response = client.get_secret_value(SecretId=secret_name)
    return json.loads(response['SecretString'])

db_creds = get_secret("bioregistro/db_credentials")
DB_USER = db_creds["username"]
DB_PASS = db_creds["password"]
```

Ejemplo de politicas de secretos con AWS IAM
```json
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::123456789012:role/bioregistro-backend-role"
  },
  "Action": "secretsmanager:GetSecretValue",
  "Resource": "*"
}
```

**8. Procedimiento de Recuperación ante Incidente**
1. Detección del incidente mediante alertas de CloudWatch.
2. Validación del último snapshot válido en RDS o versión del objeto en S3.
3. Restauración automática desde consola de AWS Backup, RDS o S3.
4. Notificación y verificación de consistencia posterior al recovery.
5. Registro de incidente en CloudWatch Logs.

##### Elementos de alta disponibilidad

**1. Replicación y Multi-AZ en Bases de Datos**

Para asegurar la continuidad operativa del sistema en caso de fallos, se configuró una topología Master-Slave en Amazon RDS con PostgreSQL, la cual opera en la región us-east-1 y se distribuye automáticamente entre múltiples zonas de disponibilidad. Esta configuración está activa en todo momento y permite realizar un failover automático hacia una réplica en caso de que el nodo principal presente fallas.

**2. Almacenamiento Seguro y Distribuido**

El almacenamiento de documentos legales y biométricos se realiza en Amazon S3, mientras que DynamoDB se configura con respaldo continuo mediante Point-in-Time Recovery. Estos mecanismos se activan cada vez que se cargan o modifican datos, y garantizan una recuperación confiable en caso de pérdidas o errores.

| Recurso | Tecnología | Implementación | Activación | Ubicación |
| ------- | ---------- | -------------- | ---------- | --------- |
| Documentos | **Amazon S3** | Versionado y replicación cruzada semanal | Al cargar o modificar | `us-east-1` / `us-west-1` |
| Metadatos | **DynamoDB** | Backup continuo con Point-in-Time Recovery | En cada escritura | `us-east-1` |

**3. Estrategias Avanzadas de Monitoreo y Alertas**

La supervisión del backend se lleva a cabo en tiempo real gracias a **AWS CloudWatch** y **Prometheus**, que operan dentro del clúster `AWS EKS` donde residen los microservicios. Estas herramientas recogen métricas de uso, disponibilidad e integridad del sistema y emiten alertas inmediatas ante comportamientos inusuales. Grafana nos permite visualizar esta información mediante dashboards.

| Tecnología | Rol | Donde se ejecuta | Momento de ejecución |
| ------- | ---------- | -------------- | ---------- |
| **CloudWatch** | Captura métricas y logs de servicios AWS | Servicios AWS | En tiempo real y continuo |
| **Prometheus** | Recoge métricas internas de microservicios a través de endpoints personalizados | Dentro del clúster EKS | Cada vez que se actualizan métricas |
| **EKS** | Aloja los microservicios del backend y los componentes de monitoreo | AWS (región `us-east-1`) | Siempre activo durante operación |
| Grafana | Visualiza datos recolectados para análisis y diagnóstico | Conectado a CloudWatch y Prometheus | Monitoreo continuo |

**4. Sistema Automatizado de Backups**

Para afrontar pérdidas de información se implementaron respaldos automáticos diarios en **RDS** y **DynamoDB** a las 2:00 a.m. y respaldos cruzados semanales en buckets de **S3** en la región `us-west-1`. Esto se encuenta en ejecución continua desde el backend de AWS y se activa sin intervención manual.

**5. Balanceo de Carga y Escalabilidad**

El tráfico al backend es manejado por un Application Load Balancer de AWS, configurado dentro del clúster de EKS, que distribuye solicitudes entrantes de forma equitativa entre las instancias disponibles. Esta capa de balanceo está activa permanentemente y escala automáticamente cuando se detecta una sobrecarga, garantizando alta disponibilidad incluso cuando hay picos de trafico.

**6. Cifrado y Protección de Accesos**

Todo el backend se envuelve en políticas de seguridad implementadas con AWS KMS. Como fue mencionado en secciones anteriores, se cifra la información en tránsito y en reposo, y mediante roles IAM que limitan el acceso a los servicios según el contexto del microservicio. Estas medidas se aplican durante cualquier operación de lectura o escritura sobre S3, RDS o DynamoDB, y están definidas para ejecutarse en todos los componentes alojados en la región `us-east-1`.

**7. Recuperación Rápida ante Desastres**

En caso de incidentes que afecten la disponibilidad del sistema, la recuperación se realiza automáticamente con el uso de snapshots y versionado en RDS, S3 y DynamoDB. Se activan inmediatamente tras la detección de fallas, que seran alertadas por CloudWatch. Esto permite devolverse al estado original usando los backups de otras regiones.

##### Diagrama del backend

A continuación se presenta el diagrama del backend del Bioregistro. En él se evidencia cómo todo el ecosistema de AWS interactúa con los distintos microservicios desplegados en el clúster de Kubernetes provisto por EKS. También se describen los microservicios internos junto a sus distintas clases, los patrones de diseño utilizados, y cómo interactúan entre sí.

Se muestra cómo la contenerización de cada microservicio se realizará utilizando Docker, y cómo el monitoreo interno será gestionado por Prometheus. Además, se destaca que en la capa externa a AWS se encuentra SumSub, utilizado como sistema de terceros.

![image](img/DiagramaBackendBioregistro.svg)

#### Diseño de los Datos

##### Topología de Datos

  - **Tipo:** Base de Datos Replicada tipo OLTP, Almacenamiento de Objetos, Base de datos documental
    - Vamos a utilizar RDS con PostgreSQL como almacenamiento OLTP de los usuarios y sus distintos tipos. Se usará un módelo master-slave con 2 read replicas en us-east-1 . Además se activará el Multi-AZ failover para permitir pasar el rol de master a una de replica lista para failover, esto nos dará alta disponibilidad. Estos respaldos se harán todos los días a las 2 de la mañana de costa rica y se guaradarán en un S3 bucket de respaldos.
    - Utilizaremos un S3 Bucket como almacenamiento de objetos para guardar PDFs y documentos legales sobre las organizaciones.
    - Usaremos DynamoDB como base de datos documental, en ella se almacenará la metadata correspondiente a los documentos en el S3, y también los distintos datos no estructurados que tienen los distintos colectivos. No utilizaremos los servicios de Global Tables ya que el acceso al sistema es principalmente desde Costa Rica. Por lo que solo usaremos 1 region: us-east-1.
    - Cabe aclarar que el Id para las personas físicas será el mismo en Cognito y RDS, mientras que el Id de los colectivos será el mismo tanto en RDS como en Dynamo.
    - También se implementará el uso de Redis por medio de Amazon Elastic Caché. Se usará el modo Clustered para garantizar mayor escalamiento, y se configurará dentro de la misma VPC de los microservicios del Bioregistro, para que así seolo pueda ser accedida desde ahí.
- **Tecnología Cloud**:
  - RDS
  - DynamoDB
  - CloudWatch: Para el monitoreo de dichos servicios de AWS

- **Polítcias y Reglas**:
  - Single-region: Solo se usará una región para RDS y DynamoDB, us-east-1
  - Backups automáticos: Tanto RDS como Dynamo harán backups automáticos a las 2 de la mañana y lo subirán a un S3.
  - Backups cruzados: Para proteger los respaldos en caso de que la región de aws caiga (poco probable), se cargaran adicionalmente en un S3 Bucket en us-west-1. Esto se hará cada semana los viernes a las 2 de la mañana, ya que su prioridad es menor.
  - Failover Automático: Dynamo tiene nativamente integrado la opción de hace failover. Con RDS se logrará por medio del uso de Multi-AZ.

- **Beneficios**:
  - Mantenernos en una sola región, reduce la latencia entre replicas de las bases de datos y baja el costo de la arquitectura.
  - Tener backups automáticos, con regiones cruzadas permite tener el sistema listo para enfrentar cualquier caída en aws.
  - Postgres es una Base de Datos open source por lo que no hace falta pagar licensias.
  - DynamoDB es de las opciones de BD documental más veloces, además está completamente integrada con el ecosistema de aws, por lo que hacer respaldos o sacarle métricas es muy sencillo.
  - DynamoDB está respaldado por AWS, por lo que ofrece un SLA del 99.999% y es 100% compatible con el resto de nuestros servicios en AWS.


##### Tenency, Seguridad y Privacidad

- **Modelo**: Singe-Access-Point

  - En este caso la base de datos para los usarios y organizaciones no será multi-tenant ya que al ser un almacenamiento de registros no es necesario.

  - Para acceder a la base de datos, implementaremos un Singe-Access-Point mediante una clase llamada RDSRepository.

  - No se implementará validación mediante tokens JWT ni se utilizará Multi-Schema en esta base de datos, ya que está lógicamente aislada del resto del sistema, eliminando así cualquier posibilidad de intrusión o acceso no autorizado a datos sensibles o datasets.

  - También usaremos IAM de AWS para que los servicios solo puedan acceder a lo que deben. Por ejemplo solo el microservicio que guarda en la BD puede usar el kms:Encrypt en RDS y Dynamo.

  - La base de datos en RDS no almacenará contraseñas, ya que su propósito no es gestionar el inicio de sesión, sino mantener un registro estructurado de las entidades registradas en la plataforma.

  - El manejo de la encripción de las DEKs está a cargo del key-management-service, sin embargo, a dicha encripción también se le aplicará el encryption at rest.

- **Encripción**:
  - Metadata de las Organizaciones (detallada al inicio del capítulo de Bioregistro).
  - Emails de los usuarios.
  - Información de contacto de usuarios y organizaciones.
  - Configuraciones de pago.

- **Cloud**:
  - Amazon Cognito para el registro de personas físicas.
  - Amazon RDS para PostgreSQL con RLS.
  - Encryption at rest en DynamoDB gracias a AWS KMS
  - Encryption at rest en RDS gracias a AWS KMS
  - Encryption at rest en el S3 Buckets con SSE-S3, para que AWS KMS gestione las claves y cifrado
  - AWS IAM.

- **Beneficios**:
  - Gracias a que solo abrá un single point of acces regulado con AWS IAM, la intrusión de un tercero a la base de datos de usuarios es muy poco probable.
  - En caso de que alguién tenga acceso a la base de datos no podrá hacer nada ya que todo está encriptado.
  - Cognito permite manejar de formar eficiente y agil el registro de personas físicas.

##### Conexión a Base de datos

- **Modelo**: Transaccional vía Statements / Store Procedures y ORM

Usaremos SQLAlchemy como ORM para interactuar con PostgreSQL dentro de la aplicación. Además se usarán Store Procedures para operaciones más complejas como registrar a una organización y hacer las relaciones pertinentes con personas físicas.

  - **Patrones de POO**:
    - Factory: Usamos el patrón Factory para la creación de las clases RDSFactory, RDSRepository, DynamoFactory, DynamoRepository.


  - **Beneficios**:
    - El código es independiente del motor de base de datos relacional, lo que permite cambiarlo fácilmente si es necesario.
    - El desarrollo es más ágil que escribir SQL puro.
    - Se protege contra vulnerabilidades como SQL Injection.
    - Se puede garantizar el cumplimiento de las propiedades ACID.

- **Pool de Conexiones**
Usaremos el pool integrado en SQLAlchemy (QueuePool), el cual es dinámico. El tamaño base del pool será de 10 conexiones, y podrá escalar hasta 15 conexiones simultáneas.

  - **Beneficios**:
    - La escalabilidad se ajusta bajo demanda.
    - Proporciona mayor estabilidad en ambientes productivos.

- **Drivers**
Para PostgreSQL utilizaremos el driver nativo psycopg2, integrado con SQLAlchemy, lo cual ofrece mejor rendimiento. Para DynamoDB y S3 emplearemos boto3, un cliente interpretado ampliamente soportado en el ecosistema AWS.

  - **Beneficios**:
    - Aprovechamos lo mejor de cada entorno: para PostgreSQL un driver nativo rápido, y para DynamoDB/S3 un driver interpretado más portátil y flexible.


##### Diagrama de Base de Datos

A continuación se presenta el diagrama de base de datos correspondiente al módulo de bioregistro. En él se muestra cómo se gestionan tanto las personas físicas como los colectivos, incluyendo una relación muchos a muchos que permite registrar qué personas representan a cada colectivo. Para clasificar los tipos de colectivo, se utiliza una tabla catálogo.

Aunque en RDS los colectivos comparten una estructura general para mantener la base simple y normalizada, es importante destacar que estos pueden tener campos específicos según su tipo. Por ejemplo, los ministerios no poseen cédula jurídica, a diferencia de otros colectivos. Por esta razón, se decidió almacenar la metadata variable de cada colectivo en DynamoDB, utilizando el mismo id que en RDS. Esto permite extender la información sin preocuparse por rigidez en el schema, manteniendo flexibilidad sin perder trazabilidad entre sistemas.

Además, un aspecto clave es el manejo de las llaves en el esquema tripartito. La KEK del usuario se almacena en una tabla que guarda las claves correspondientes a los representantes de la empresa, junto con un indicador que marca si ya fueron validadas mediante el proceso de aprobación tripartita. Esto permite que, una vez aprobadas, los usuarios no necesiten autenticarse cada vez que acceden a la cuenta empresarial.

Por su parte, la empresa almacena su propia KEK directamente en su tabla correspondiente, mientras que existe una tabla específica que asocia las KEKs de Data Pura Vida con cada empresa registrada.

![image](img/DiagramaBDBioregistro.png)


### 4.2 La Bóveda

El componente de La Bóveda constituye el núcleo de la plataforma, ya que es el responsable del almacenamiento y gestión de todos los datasets. Este módulo permite alojar datasets con distintos niveles de acceso y monetización, incluyendo opciones de descarga gratuita, pago único, suscripciones por cuotas, y configuraciones de visibilidad pública o privada.

Uno de los aspectos más críticos de La Bóveda es la seguridad. Solo los usuarios que hayan adquirido un dataset o que hayan sido aprobados explícitamente pueden acceder a su contenido. El nivel de resguardo es tan alto que ni siquiera los administradores del sistema tienen acceso directo a los datos almacenados, garantizando así una separación estricta de responsabilidades y máxima confidencialidad.

Adicionalmente, este componente debe ser altamente resiliente y escalable, ya que se espera una carga intensiva tanto en volumen de datos como en frecuencia de acceso. La infraestructura debe soportar cargas en batch de datos, así como consultas analíticas complejas, sin comprometer la integridad ni el rendimiento del sistema.

Por estas razones, en esta sección se detalla el diseño de La Bóveda con énfasis en los aspectos de seguridad, escalabilidad, resiliencia y eficiencia, pilares fundamentales para asegurar su correcto funcionamiento dentro del ecosistema de la plataforma.

En cuanto a como se planean guardar los datasets a continuacióń se muestra un diagrama con la vista a alto nivel:

![image](img/BovedaAltoNivel.png)

En la imagen se puede ver cómo se debe tener un almacenamiento central, el cual debe estar dividido lógicamente para los colectivos. Ya después cada colectivo tendrá sus datasets guardados junto con sus tablas, que en ocasiones pueden ser usadas en datasets distintos. Más adelante se verá cómo es que este enfoque será logrado.

#### Diseño del Backend

El backend de este componente es más simple, ya que la mayor parte del peso cae en la estructura de la base de datos y su modelo de seguridad. En esta sección solo se comentarán dos funcionalidades: la funcionalidad de trazabilidad y cómo el API interactúa con Redshift.

**Trazabilidad:**

En este componente es sumamente importante que se tenga trazabilidad de quién ejecuta qué tarea. Por lo que, al hacer un query a Redshift, siempre se adjuntará como variable de sesión el ID de Cognito de la persona que pidió el query.

Luego, gracias a la funcionalidad de Amazon Redshift logs, se podrá ver detalladamente la información del query de la siguiente forma:

| Nombre de columna | Descripción |
|-------------------|-------------|
| recordtime        | Hora en la que ocurrió el evento. |
| db                | Nombre de la base de datos. |
| user              | Nombre de usuario. |
| pid               | ID del proceso asociado con la sentencia. |
| userid            | ID del usuario. |
| xid               | ID de la transacción. |
| query             | Un prefijo `LOG:` seguido del texto de la consulta. |

Ahora bien, estos logs sirven tanto para tener un registro de qué consultas se han hecho (para más adelante dar contexto Agentes sobre como consultar un dataset), como para llevar cuotas de uso de datasets que se usan por cuotas definidas.

Por ello, cuando estos logs lleguen a AWS CloudWatch, se disparará una Lambda Function que se encargue de obtener el query y también el ID del usuario que se seteó en la consulta. Luego, se revisará si el dataset al que se le realizó la consulta es de tipo cuota, y en dado caso se va a la tabla de cuota en RDS para hacer la deducción.

Para el resto de los casos (incluyendo cuando el dataset es de tipo cuota), se insertará el query en un índice de OpenSearch, el servicio gestionado de Elasticsearch que ofrece AWS. Gracias a la naturaleza de time series de Elastic Search, podremos almacenar estos logs de manera eficiente, organizándolos en índices mensuales por dataset con el formato de nombre `DATASETNAME-YYYY-MM`.
Esto evitará almacenamiento masivo y poco escalable típico de motores SQL, y además funcionará como una fuente sencilla para que los agentes de IA puedan alimentarse con los queries asociados a cada dataset.

A continuación un ejemplo de código de como se puede realizar dicha lambda function:
``` python
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

``` json
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



##### Servicios en AWS

Se mencionarán solo los servicios de AWS que aún no han sido descritos en algún punto de la arquitectura. En caso de querer ver todos los servicios de AWS que se usarán y como se desplegarán por medio de terraform ir a dicha sección después de la explicación de los microservicios.

**AWS Lambda:**
Para las funciones serverless que obtienen información de los datasets y la loguean.

**Configuración de Hardware:**  Aunque no gestionamos hardware directamente, sí configuraremos los recursos, como:
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

#### Diseño de los Datos

##### Topología de Datos

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
    ``` sql
    CREATE EXTERNAL SCHEMA rds_schema
    FROM POSTGRES
    DATABASE 'admin_db'
    URI 'my-db-instance.abc123xyz.us-east-1.rds.amazonaws.com'
    PORT 5432
    IAM_ROLE 'arn:aws:iam::cuenta-dpv:role/admin-dpv'
    SECRET_ARN 'arn:aws:secretsmanager:us-east-1:123456789012:secret:MySecret'
    ```
  - Redshift permite copiar en Batch archivos de Parquet desde un S3 y mapearlos a tablas en su almacenamiento interno:
    ``` sql
      COPY esquema.tabla_destino
      FROM 's3://tu-bucket/ruta/a/parquets/'
      IAM_ROLE 'arn:aws:iam::cuenta-dpv:role/admin-dpv'
      FORMAT AS PARQUET;
    ```

##### RLS

No se usará RLS ya que el acceso a datasets se hace por tablas, entonces una vez un usuario tenga acceso a un dataset, podrá ver todo el contenido que este tenga; no habrán filas a las que esté restringido. Nuestro diseño es seguro porque en una misma tabla solo se guarda información correspondiente a un solo colectivo. Puede ser que esa tabla se comparta entre datasets del colectivo, pero igual no pasa nada, dado que el acceso sigue siendo por tabla. En la siguiente sección se dirá cómo se gestiona el acceso por tabla.


##### Tenency, Seguridad y Privacidad

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
    ``` python
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
    ``` python
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
    ``` python
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

##### Conexión a Base de datos

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

##### Diseño para IA

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




##### Diagrama de Base de Datos

A continuación se presenta el diagrama de base de datos correspondiente al módulo de La Bóveda. En él se muestra cómo se utiliza la misma base de datos de RDS que en el bioregistro, ya que su rol es meramente administrativo.

Se puede ver cómo existe una tabla que almacena la información principal de los datasets, y que se asocia con PersonaFisica para poder revisar quiénes tienen acceso a dichos datasets. Además, para mantener el diseño normalizado, se tiene una tabla extra que guarda los datasets de pago y dice si son por cuota o pago único, además de su costo. Y finalmente, la tabla de Cuotas que guarda cuántas consultas le restan a un usuario con respecto a un dataset.

Con respecto a la estructura de Redshift, esta es imprescindible, por ello no se muestra en el diagrama; dependerá completamente de lo que suban los usuarios. Eso sí, definitivamente estará separada por schema para cada colectivo.

![image](img/DiagramaBDBoveda.png)



### 4.3 Centro de Carga

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

#### Diseño del Frontend

#### ARQUITECTURA DEL CLIENTE

#### Client-Side Rendering con Renderizado Estático

La arquitectura implementa **CSR** con contenido estático servido desde **S3** y **CloudFront** como CDN. Los bundles de React generados durante el build se almacenan en buckets S3 y se distribuyen globalmente através de CloudFront para optimizar latencia y disponibilidad.


**API única** desarrollada en **FastAPI** para toda la comunicación backend, centralizando autenticación, validación y procesamiento de datos.

### Gestión de Estado Durante Uploads Largos

- **Persistencia automática** en `localStorage` para mantener progreso de uploads pausables/resumibles entre sesiones del navegador
- **Recovery automático** tras desconexiones de red mediante detección de sesiones interrumpidas y restauración del estado exacto
- **Optimización de memoria** para archivos grandes procesando muestras de 10KB usando FileReader API

### PATRONES DE DISEÑO IMPLEMENTADOS


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

### DIAGRAMA DE DISEÑO


El diagrama muestra la integración de todos los patrones de diseño implementados en el frontend. La arquitectura se organiza en **5 capas** claramente diferenciadas:

![alt text](image-1.png)

1. **Capa Singleton/Facade**: UploadGateway mantiene una instancia única para toda comunicación con el backend, mientras ChunkUploadManager gestiona la fragmentación de archivos grandes

2. **Capa Chain of Responsibility**: AbstractSourceHandler coordina el procesamiento secuencial de diferentes fuentes de datos (archivos, APIs, bases de datos)

3. **Capa Builder**: DatasetConfigBuilder construye configuraciones paso a paso mediante el wizard interactivo

4. **Capa Strategy**: ConfigurationStrategy y sus implementaciones (Public, Private, Paid) manejan las diferentes configuraciones de acceso

5. **Capa Observer**: ProgressTracker notifica a múltiples observers para actualizar la interfaz de usuario en tiempo real

### COMPONENTES VISUALES

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

### ESTRUCTURA DE CARPETAS

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

### TECNOLOGÍAS INTEGRADAS

#### Stack Principal

- **React 18**: Base del frontend con hooks y context API
- **Tailwind CSS**: Styling siguiendo Atomic Design principles
- **Formik + Yup**: Formularios robustos con validación completa
- **Plotly**: Visualización de datos durante preview
- **Axios**: HTTP client con interceptors configurados

#### Servicios AWS

- **S3**: Almacenamiento de bundles estáticos
- **CloudFront**: CDN global para optimización
- **Lambda@Edge**: Restricción geográfica por IP
- **Cognito**: Autenticación con tokens JWT

#### Diagrama del Frontend

![alt text](image.png)

#### Diseño del Backend

##### Microservicios en los Componentes

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
  - Para MongoDB se usará el comando "mongodump", que crea un snapshot de la base de datos en formato bson, el cual se dejará en el S3 Posteriormente.
  - Tanto MariaDB, MySQL, PostgreSQL y SQL Server tienen la misma funcionalidad del Dump, la diferencia es que da archivos de tipos .sql. Pero de igual modo serán guardados en el S3.
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

| Tipo de evento | Handlers |
| -------  | ----------  |
|`upload_success`|`EmailNotificationHandler`, `AppNotificationHandler`|
|`validation_failed` |`EmailNotificationHandler, AdminAuditHandler` |
|`external_alert` |`WebhookNotificationHandler`|
|`quota_exceeded` |`AppNotificationHandler`, `EmailNotificationHandler` |
|`admin_warning` |`AdminAuditHandler`, `EmailNotificationHandler`|

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

##### Diagramas de Clases

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

![identity clases](img/ClasesCentroCarga1.png)



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

![identity clases](img/ClasesCentroCarga2.png)

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


![identity clases](img/ClasesCentroCarga3.png)


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

![identity clases](img/ClasesCentroCarga4.png)



##### Servicios de AWS
**Amazon S3**
El servicio de **AWS S3** será el almacén principal para la carga de datos en crudo de los datasets este será utilizado por **TemporaryStorageHandler** en **dataset-upload-service**. También es importante mencionar que este servicio servirá para el acceso a los datasets por **validation-service** para el análisis de los datos.

**Configuración de Hardware:** Servicio de almacenamiento de objetos, ilimitadamente escalable. No requiere configuración de hardware directa.

**AWS KMS:**
Los datasets necesitan ser protegidos para ello utilizamos **AWS KMS** ya que este servicio nos será de utilidad para proporcionar las claves criptográficas para el cifrado y descifrado de los datos.
Se utilizará para proteger los datasets almacenados temporalmente en **S3** por **TemporaryStorageHandler** en **dataset-upload-service** y para el cifrado/descifrado de secretos gestionados por el **security-service**.

**Configuración de Hardware:** Servicio gestionado, serverless. No requiere configuración de hardware. Sin embargo, se pueden configurar la creación de claves.
-	**Tipo de clave:**  Simétrico
-	**Uso de claves:** Cifrado y descifrado
-	**Origen del material de claves:** KMS
-	**Regionalidad:** Clave de una sola región

**AWS RDS**
Servirá como la base de datos relacional primaria para metadatos estructurados.
Se utilizará para almacenar la metadata de los datasets en el microservicio de DatasetMetadata.

**Configuración de Hardware:**
- **Método de creación**
  -	 Creación estándar
- **Motor de base de datos**
  -	Aurora PostgreSQL
  -	Versión: Compatible con PostgreSQL 16.6
  -	Soporte extendido de RDS: No
- **Plantilla**
  -	Desarrollo y pruebas
- **Identificador del clúster**
  -	database-1
- **Credenciales**
  -	Usuario maestro: postgres
  -	Contraseña: Autoadministrada
  -	Administración de credenciales: Autoadministrado
  -	Clave de cifrado: aws/secretsmanager (por defecto)
- **Almacenamiento**
  -	Tipo: Aurora optimizado para operaciones de E/S
- **Instancia**
  -	Clase de instancia: db.r6g.2xlarge (8 vCPUs, 64 GiB RAM)
  -	Multi-AZ: No (sin réplica de Aurora)
- **Conectividad**
  -	EC2 conectado: No
  -	Tipo de red: IPv4
  -	VPC: Default VPC (vpc-0d710bc7833e39b85)
  -	Grupo de subredes: predeterminado
  -	Acceso público: Sí
  -	Grupo de seguridad de VPC: default

**Amazon DynamoDB**
Se consideraría como un complemento a RDS para metadatos de alta concurrencia o naturaleza dinámica como las sesiones de usuario, y los contadores de consumo de datasets en tiempo real.
Esta será utilizada por DatasetUploadTemp en el dataset-upload-service, dada su necesidad de escritura y lectura rápidas al gestionar el estado temporal de los archivos.

**Configuración de Hardware:** Servicio completamente gestionado y serverless. La configuración se basa en las unidades de capacidad de lectura/escritura.

**AWS SES**
Será el servicio para el envío de correos electrónicos transaccionales a los usuarios finales (ej., notificación de carga exitosa, fallo de validación), gestionado por el **EmailNotificationHandler** dentro del **notification-service**.

**Configuración de Hardware:**
Para configurar un SES simplemente necesitamos dirigirnos a crear una identidad. En tipo de identidad utilizaremos **Dirección de correo electrónico**, luego en **Dirección de correo electrónico** colocamos el correo electrónico que utilizaremos (ej. notificacionesDatos@gmail), luego nos llega una notificación al correo donde tendremos que verificar la dirección de correo electrónico.

##### Sistema de Monitoreo
El monitoreo del Componente del Centro de Carga de Datos se implementará siguiendo una estrategia de observabilidad integral que permita supervisar en tiempo real el comportamiento, rendimiento y seguridad de todo el proceso de ingesta inicial de datasets.

**Métricas y Rendimiento**

**AWS CloudWatch** será el servicio para monitoreo más importante se encargara de recopilar y almacenar métricas operacionales del Componente del Centro de Carga de Datos. Se monitorizarán aspectos críticos como:

**Métricas de Negocio:**
-	Cantidad de datasets cargados exitosamente por formato (CSV, Excel, JSON).
-	Tasa de éxito en la validación inicial de esquema y estructura del archivo.
-	Tiempo promedio del proceso completo de carga (desde la recepción hasta el almacenamiento temporal en S3).
-	Volumen de datos (en GB) ingesados diariamente.
-	Cantidad de notificaciones de carga enviadas (éxito/fracaso).

**Métricas de Infraestructura:**
-	**S3 (data-temp-storage):** Latencia de operaciones PutObject, GetObject, ListObjects; cantidad de PutRequests, GetRequests; tasa de errores (4xx, 5xx).
-	**RDS/DynamoDB:** Latencia de conexiones, ReadIOPS, WriteIOPS, utilización de recursos para las tablas DatasetUploadTemp y DatasetMetadata.
-	**AWS RabbitMQ:** Tamaño de la cola de notificaciones de notification-queue, mensajes entrantes/salientes, latencia de conexión al broker.
-	**AWS KMS:** Tasa de solicitudes y errores en las operaciones de cifrado/descifrado de las claves usadas por dataset-upload-service.

**Prometheus** complementará a CloudWatch recopilando métricas específicas como las del microservicio de **dataset-upload-service** a través de un **endpoint** dedicado. Esto permitirá obtener métricas más granulares sobre el comportamiento interno de la aplicación, como:
-	Los contadores de operaciones específicas (ej., validation_attempts_total, encryption_calls_total).
-	Los histogramas de distribución de tiempos (ej., file_parsing_duration_seconds, db_write_duration_seconds).

**Visualización y Dashboards**
**Grafana** se utilizará como plataforma principal de visualización, integrándose tanto con CloudWatch como con Prometheus para crear dashboards interactivos que permitan:
-	**Dashboard Operacional de Carga:** Vista en tiempo real del estado general del proceso de carga de datos. Mostrará el volumen de cargas activas, la distribución de archivos por formato, la tasa de éxito/fracaso de las cargas, y el estado de salud de los pods de dataset-upload-service y sus dependencias (S3, DBs, MQ).

-	**Dashboard de Rendimiento de Carga:** Monitoreo específico de las latencias. Incluirá el tiempo promedio del proceso de carga, la latencia de escritura en S3, la latencia de registro de metadatos en DBs, y el consumo de recursos (CPU/memoria) del **dataset-upload-service**.

-	**Dashboard de Calidad y Seguridad de Carga:** Seguimiento de eventos relacionados con la calidad inicial y la seguridad del proceso de carga. Mostrará la tasa de errores en la validación inicial de esquema, intentos de acceso no autorizado a recursos de carga vía security-service, y monitoreo de las operaciones de cifrado.

**Logs y Trazabilidad**
El sistema de logging aprovechará **CloudWatch Logs** para centralizar todos los registros generados por los componentes del Centro de Carga de Datos. Se implementará un esquema de logging estructurado que facilite:

-	**Trazabilidad Completa con AWS X-Ray:** Cada transacción de carga tendrá un identificador único de correlación (ID de traza X-Ray) que permitirá seguir su flujo desde la recepción del archivo, pasando por la interacción con S3, KMS, el registro de metadatos en RDS/DynamoDB, y la interacción con security-service o validation-service, hasta la notificación final.

-	**Auditoría y Diagnóstico**
    - **CloudWatch Logs Insights:** Permite la consulta interactiva de logs para identificar rápidamente la causa raíz de cualquier incidencia (ej., errores en el procesamiento de un tipo de archivo específico).
    -  **AWS CloudTrail:** Registra todas las llamadas a la API de AWS realizadas por el dataset-upload-service y sus roles asociados (ej., s3:PutObject, kms:Encrypt, secretsmanager:GetSecretValue), esencial para auditoría y seguridad.

**Sistema de Alertas y Notificaciones**
Se configurará un sistema proactivo de alertas utilizando **CloudWatch Alarms** que notificará al equipo de operaciones cuando se detecten condiciones anómalas:
-	**Alertas Críticas (respuesta inmediata requerida):**
    -	Fallo total del **dataset-upload-service** o indisponibilidad de su **endpoint** de **health check**.
    -	Tasa de error (HTTP 5xx en el UploadController o en S3) superior al 5% en una ventana de 5 minutos.
    - Fallo en la conexión con servicios críticos (S3, RDS/DynamoDB, KMS, Amazon MQ).
    -	Detección de un incremento súbito de errores en operaciones de cifrado/descifrado (KMS).
    -	Errores críticos registrados en CloudWatch Logs por el dataset-upload-service (ej., Unhandled Exception).

-	**Alertas de Advertencia (revisión prioritaria):**
    -	Degradación del rendimiento con latencias de carga de datasets superiores a 30 segundos.
    -	Uso de recursos (CPU, memoria) del pod de **dataset-upload-service** por encima del 80% de capacidad.
    -	Incremento inusual en las validaciones iniciales de datasets fallidas.
    -	Acumulación de objetos sin procesar en el bucket data-temp-storage por más de un umbral de tiempo.

-	**Alertas Informativas (seguimiento regular):**
    -	Resumen diario de métricas operacionales de carga (ej., total de cargas exitosas del día).
    -	Reporte semanal de tendencias de volumen de datos ingesados.

**Monitoreo de Cumplimiento y Seguridad**
Dado el manejo de datos sensibles en la carga, se implementarán controles específicos de monitoreo para garantizar el cumplimiento normativo y la seguridad:
-	**Auditoría de Accesos a Datos Cargados:** Registro detallado usando CloudTrail y CloudWatch Logs de todos los accesos PutObject, GetObject al bucket data-temp-storage, identificando quién accedió, cuándo y con qué propósito.
-	**Verificación de Cifrado:** Monitoreo continuo del estado de cifrado de datos en reposo en S3 mediante políticas de bucket y eventos de KMS, asegurando que todos los archivos cargados estén cifrados correctamente.
-	**Monitoreo de Acceso a Secretos:** Seguimiento de los intentos de acceso y las rotaciones de credenciales en AWS Secrets Manager utilizadas por el dataset-upload-service para conectarse a fuentes externas o bases de datos.

**Health Checks y Disponibilidad**
Los microservicios del Centro de Carga implementarán múltiples niveles de verificación de salud que serán monitoreados continuamente por Kubernetes y los sistemas de monitoreo:
-	**Liveness Probe:** Verificación básica de que el dataset-upload-service está activo y respondiendo, ejecutada cada 10 segundos por Kubernetes.
-	**Readiness Probe:** Verificación comprehensiva de que el dataset-upload-service puede procesar solicitudes de carga, incluyendo conectividad con S3, KMS, bases de datos (RDS/DynamoDB) y Amazon RabbitMQ.
-	**Deep Health Checks:** Verificaciones periódicas más exhaustivas que validan la integridad de configuraciones críticas (ej., validación de esquemas de carga), la disponibilidad de claves de cifrado, y la correcta operación del flujo completo de carga de un archivo de prueba simulado.

**Análisis y Mejora Continua**
El sistema de monitoreo no solo detectará problemas, sino que proporcionará insights para la mejora continua del proceso de carga:
-	**Análisis de Tendencias:** Identificación de patrones en el volumen y tipo de cargas (ej., picos horarios, aumento de un formato específico) para optimizar recursos y predecir necesidades futuras.
-	**Detección de Anomalías:** Uso de las capacidades de CloudWatch para identificar comportamientos inusuales (ej., caída repentina en el número de cargas exitosas) que podrían indicar problemas emergentes.
-	**Reportes de Capacidad:** Proyecciones basadas en datos históricos de volumen de carga y uso de recursos para planificar el crecimiento de la infraestructura de almacenamiento (S3) y cómputo (EKS).
-	**Optimización de Costos:** Análisis del uso de recursos de S3, EKS y DBs para identificar oportunidades de optimización de costos sin comprometer el rendimiento.



##### Modelo de seguridad detallado

#### Diseño de los Datos

La influencia de este componente sobre la base de datos es mínima, ya que reutiliza la misma instancia de RDS compartida con La Bóveda y el Bioregistro, cuyas especificaciones ya fueron detalladas previamente. Del mismo modo, las configuraciones para DynamoDB y S3 se mantienen idénticas a las de esos componentes.
El único aporte nuevo se encuentra reflejado en el diagrama de base de datos que se presenta a continuación, el cual será explicado en detalle.

##### Diagrama de Base de Datos

A continuación se presenta el diagrama de base de datos correspondiente al módulo del Centro de Carga. Este diagrama incluye las tablas clave que componen el componente, entre ellas:

- **AccesoADataset**: registra qué personas tienen acceso a cada dataset.
- **DatasetDePago y TipoDePago**: gestionan la configuración de pagos asociados a datasets, incluyendo su categorización.
- **DatasetCrons**: define el modo de carga que tendrán los datasets recurrentes (Delta, Complete), y el tipo de fuente del que pueden venir (Base de datos o API). Esta tabla será consultada por Airflow para aplicar los DAGs correspondientes de forma automatizada.

![image](img/DiagramaBDCentroCarga.png)


## 5. Validación de los requerimientos

- Validar que el diseño cubre todos los requerimientos funcionales y no funcionales del sistema
- Identificar ventajas y desventajas del diseño, proponiendo mitigaciones a los riesgos y limitaciones

### Componente: MarketPlace 
### Patrones de Diseño de Objetos - Frontend del Marketplace
El diseño del frontend del componente Marketplace de Data Pura Vida sigue principios de diseño orientado a objetos que buscan flexibilidad, mantenibilidad y escalabilidad. Los principales patrones aplicados son los siguientes:

#### 1 **Patrón de Strategy**

- Ubicación: En los filtros de búsqueda de datasets.
- Descripción: El frontend permite al usuario aplicar distintos tipos de filtros (por precio, categoría, tipo de dataset, popularidad, etc). Cada filtro implementa una estrategia diferente de ordenamiento o filtrado, pero todos heredan de una interfaz común, lo que permite agregar nuevos filtros en el futuro sin modificar el flujo principal.
- Beneficio: Permite extender fácilmente nuevos criterios de búsqueda sin alterar el resto del sistema.

#### 2️ **Patrón de Singleton**

- Ubicación: Cliente HTTP centralizado (por ejemplo ApiConnector o MarketplaceApiClient).
- Descripción: Todo el frontend utiliza una única instancia para gestionar las conexiones al backend (requests HTTP a la API REST de Marketplace).
- Beneficio: Garantiza un único punto de configuración de headers, manejo de tokens, interceptores de error, y manejo centralizado de respuestas.

#### 3️ **Patrón de Observer (Pub-Sub)**

- Ubicación: Sistema de notificaciones y actualización de componentes de UI.
- Descripción: Algunos componentes de la interfaz están suscritos a eventos globales como la finalización de una compra, actualización de un dataset o expiración de accesos.
- Beneficio: Desacopla los componentes visuales del flujo de negocio, permitiendo que reaccionen a eventos sin depender directamente unos de otros.

#### 4️ **Patrón de Facade**

- Ubicación: Módulo de servicios de pago.
- Descripción: Las operaciones de compra, validación de pagos, visualización de precios y confirmación de compra son orquestadas desde un único módulo de servicios, el cual encapsula la comunicación con Stripe y la lógica de negocio asociada.
- Beneficio: Simplifica el uso de APIs externas, ocultando la complejidad de validaciones, formatos de respuesta y errores.

#### 5️ Patrón MVVM (Model-View-ViewModel)

- Ubicación: Arquitectura general del frontend.
- Descripción:
  - Model: Define los objetos de negocio como Dataset, Order, PaymentTransaction.
  - ViewModel: Implementado mediante custom hooks como useDatasetSearch(), useMarketplaceCart().
  - View: Los componentes visuales de React, organizados bajo Atomic Design.
- Beneficio: Separa de forma clara la lógica de presentación, la lógica de negocio y el manejo de estado de UI.

### Estructura de Carpetas del Sistema - Frontend del Marketplace

El frontend del componente Marketplace sigue una estructura modular basada en el patrón de diseño Atomic Design, el patrón MVVM y principios de escalabilidad y mantenibilidad. La organización permite extender fácilmente nuevos módulos de negocio dentro del Marketplace.

```plaintext
frontend/
├── public/                     # Archivos estáticos
├── src/
│   ├── api/                    # Lógica de conexión con el backend (Axios + interceptores)
│   │   ├── marketplaceApi.ts   # Endpoints específicos del Marketplace
│   │   └── authApi.ts          # Autenticación general vía Cognito
│   │
│   ├── models/                 # Definición de los modelos de negocio
│   │   ├── Dataset.ts
│   │   ├── Order.ts
│   │   └── Payment.ts
│   │
│   ├── hooks/                  # ViewModels (gestión de estado y lógica de UI)
│   │   ├── useDatasetSearch.ts
│   │   ├── useCart.ts
│   │   └── usePayment.ts
│   │
│   ├── components/             # Componentes visuales según Atomic Design
│   │   ├── atoms/              # Botones, inputs, etiquetas
│   │   ├── molecules/          # Formularios de búsqueda, carritos
│   │   ├── organisms/          # Composición de vistas completas
│   │   └── templates/          # Layouts reutilizables
│   │
│   ├── pages/                  # Rutas principales del sistema
│   │   ├── MarketplaceHome.tsx
│   │   ├── DatasetDetails.tsx
│   │   ├── Cart.tsx
│   │   └── Checkout.tsx
│   │
│   ├── contexts/               # Contexto global de usuario y carrito
│   │   ├── UserContext.tsx
│   │   └── CartContext.tsx
│   │
│   ├── services/               # Lógica externa: pagos, facturación, etc.
│   │   ├── stripeService.ts
│   │   └── invoiceService.ts
│   │
│   ├── utils/                  # Funciones utilitarias comunes
│   └── App.tsx                 # Punto de entrada de la aplicación
│
├── amplify/                    # Configuración de AWS Amplify y Cognito
│   ├── backend/
│   └── aws-exports.js
│
└── tests/                      # Pruebas unitarias e integración
    ├── unit/
    └── integration/
```

### Arquitectura del Cliente - Frontend del Marketplace

El frontend del componente Marketplace sigue una arquitectura moderna basada en principios de MVVM (Model-View-ViewModel), Atomic Design y desacoplamiento de responsabilidades. Este diseño permite mantener la lógica de negocio separada de las vistas, simplificando su mantenimiento y escalabilidad.

#### 📐 Arquitectura General

```plaintext
[ Usuario ]
   ↓
[ View (components/pages) ]
   ↓
[ ViewModel (hooks) ]
   ↓
[ Model (models) ]
   ↓
[ API Layer (apiConnector) ]
```
#### Seguridad en el cliente

- El acceso al Marketplace requiere autenticación mediante AWS Cognito, gestionando usuarios institucionales y ciudadanos.
- Los tokens JWT son gestionados desde el cliente y renovados automáticamente.
- Los permisos de visualización y compra de datasets se validan tanto en el cliente (UI) como en el backend (control real de acceso).

#### Tecnologías utilizadas en el cliente

| Tecnología      | Descripción                               |
|------------------|-------------------------------------------|
| React            | Framework principal para UI              |
| Tailwind CSS     | Framework de estilos responsivos         |
| Axios            | Cliente HTTP centralizado                |
| AWS Amplify      | Integración con Cognito y servicios AWS  |
| Stripe           | Gestión de pagos y facturación           |
| React Context    | Manejo de estado global (usuario, carrito)|
| React Router     | Control de rutas y navegación            |

#### Beneficios de esta arquitectura

- Separación clara de responsabilidades.
- Alta reutilización de componentes.
- Lógica de negocio desacoplada de las vistas.
- Facilidad para agregar nuevos tipos de datasets, métodos de pago o reglas de negocio sin romper el flujo principal.
