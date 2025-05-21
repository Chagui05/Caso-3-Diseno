# Respuestas de entrevista

## Bio Registro Verde: (edited)
- En que idioma debe estar la documentación y la aplicación

ustedes deciden.

---
- Se espera que se permita tanto el registro de instituciones como de personas. Pero en otra sección se dice que desde una misma cuenta se pueden administrar varias organizaciones. Lo cual deja la pregunta como es la "Jerarquía" para la creación de cuentas asociadas a organizaciones (cámaras, grupos y empresas), ¿se manejarán por medio de una cuenta "central", y luego con las llaves de seguridad, una persona física puede tener un acceso secundario a dicha organización?

las organizaciones deben ser administradas por personas físicas al final, entonces primero debe estar registrada la persona, o las personas, cuando se crea la organización, se escojen las personas que administran la organización. Le toca al sistema de forma manual y por AI, revisar la documentacion de la organización para verificar si esas personas efectivamente son los admins.

---

- Exactamente que completitud se desea validar con la IA? Porque es posible que ocupemos entrenar modelos innecesariamente, tomando en cuenta que existen servicios como SumSub que ya se encargan de esto.

Es decisión de diseño de ustedes lo que puedan o no hacer por 3rd parties, y lo que puedan o deban hacer por medio de entrenamientos custom de modelos para AIs.

---

- Existen sistemas que facilitan el registro de KYC, como SumSub (tiene soporte en costa rica) gracias a su SDK. ¿Se puede usar este servicio para el registro biométrico y comprobación de identidad, o se desea que se cree un sistema manual desde 0?

Ustedes deciden lo que consideren mejor para el proyecto.

---

- El proceso de validación interna de las cuentas aplica para todo tipo de cuenta?

correcto.

---

- El proceso de validación interna lo realiza un equipo humano, un flujo automatizado, o ambos?

ambos

---

- Además, que parte de la validación interna debe ser realizada por nosotros si ya se va a integrar a sistemas de terceros como SumSub (edited)

Depende de los registros de personas y organizaciones, deben de estar listo a procesos de registro donde puede que todo lo puedan valida rcon sumsub, o puede ser que para otra documentación necesitan sumsub con otro servicio de terceros adicional, o esos mismos dos con revision manual de algo, o esos mismos dos con revision manual, y con un LLM propio, etc. Al final el diseño debe poder dotar a la plataforma de configurar procesos de registros segun sus variables y eso llevar a los procesos de validacion que se ocupen.

---

- "Restringir el acceso al portal solo desde direcciones IP ubicadas en Costa Rica", puede resultar limitante para costarricenses que se encuentren de viaje en el extranjero. En su lugar, podría considerarse aplicar esta restricción solo a la página de registro.

Correcto, o bien hacen un proceso para registrar de forma autenticada mi IP de acceso. Permanente o temporal.

---


- Cual es la razón para capturar la cuenta de IBAN y tarjetas de crédito en el registro, ¿Por qué este proceso no se realiza luego, solo en caso de que el usuario esté interesado en realizar o recibir pagos?

La gerencia quiere evitar que se creen cuentan solo por "ver", si no que sean personas que van hacer un uso responsable de la plataforma.

---

- En cuanto al proceso de pago por acceso a datos, ¿la conciliación debe realizarse de forma externa entre las partes interesadas (por ejemplo, acordando transferencias vía SINPE o bancarias)? ¿O se contempla la posibilidad de integrar un sistema de pagos de terceros, como Stripe, para gestionar las transacciones directamente desde la plataforma?

Todas las platas las maneja la plataforma con los medios de pago que ofrezca la plataforma. Pero si los saldos y accesos que dan esos pagos lo controla la plataforma.

---

- En caso de que los pagos se hagan dentro del sistema, se requiere confirmar nuevamente con la clave criptográfica?

No entiendo esta pregunta.

---

- Quién define la whitelist para el sistema?

Los administradores de la plataforma de forma tripartita.

---

## Feliz compartiendo datos:

- Se espera que internamente, independientemente de la fuente de datos (excel, csv, NoSql-Documental, SQL, etc.), despues de ser subidos y aplicado el proceso de ETDL si use un formato unificado dentro de la BD, o se mantendrá el formato de origen?

Un solo formato.

---

- Con los datos proporcionados por conexión directa a BDs externas, se espera siempre obtener los datos mediante dicho connection string, o se hace una snapshot de dicha base de datos dentro de nuestra infraestructura cada n tiempo (definido por el usuario)?

Como ustedes diseñen el mecanimos, la idea es poder sacar los datos de la fuente y mantenerlos actualizados cuando quien los configura así lo decide.

---

- "Requerir nombre, descripción y metadata útil para IA sobre las columnas del dataset", ya las bases de datos tienen que traer esos datos internamente, o se dan al ingresar al sistema, y nosotros "Manualmente" tenemos que agregarlo a cada fila/documento.

Es muy probable que la data no lo traiga, porque los autores de la data no saben que les va a pedir el sistema al subir la data.

---

- El flujo ETDL con IA se construye desde cero o se pueden integrar motores existentes como Apache Nifi, Talend, Airflow o similares? (edited)

Ustedes deciden esos aspectos técnicos.

---

- Que implica "Validar el formato, estructura y contenido de cada dataset compartido", suena muy general, que formatos y estructuras son los que se tienen que validar.

pueden ser muchas reglas, por ejemplo si vienen fechas esas vendran en mm/dd/yy, o mm/dd/YYYY, o dd/mm/yyyy, , o si los booleans son 1/0, o true, false, o Si, No, etc... si en el archivo vienen filas y columnas con nombres válidos de campos. Campos no nulos, datatypes correctos, etc.

---

## Descubriendo Costa Rica:

- Al entrar al Dashboard no hay gráficos listos, y el usuario debe crearlos? O el que se los vendió previamente creo unos dashboards default?

no existen los usuarios crean sus dashboards, ellos deciden a quienes darles accesso, compartirlos, ponerlos públicos, y asi.

---
- Se comentó de usar visualizadores de data como Power BI, Kibana o Tableau, como se pretende esta integración? ya que como tal no están diseñados para embedir tablas en la web.

No entiendo, lo idea es usar un visualizador que ya tenga un portal para dashboard con seguridad y todo lo que se necesite y si esto se consulta via web.

---

- La opción de compartir dashboards se hace por medio de una sección de comunidad con dashboards vacíos creados por usuarios? o se comparte generando un JSON que luego se cargue para mostrar los dashboards (como en el caso de grafana)?

Contestado arriba, lo ideal es que esta funcionalidad ya esté dada por el generador de dashboards

---

- Qué criterios definen cuándo un acceso sistema-a-sistema para alimentar una IA está autorizado? Hace falta firmar un contrato de que los datos solo serán usados para dichos fines?

La administración es celosa con esto, lo que se quiere es habilitar 1 o 2 integraciones para que las personas puedan personalizar modelos de AI.

---

- Para el envío de data por medio de vectores. Esto hace referencia a que los datos se mandan listos para ya ser procesados por la IA en un formato que no es posible usar para otro método que no sea entrenado de inteligencia artificial? En dicho caso habría que tener un "módulo" en nuestro backend que vectorice las entradas de una BD (podríamos usar modelos de hugging face pre-entrenados como all-mpnet-base-v2).

Si correcto o utilizar una base de datos para este caso como por ejemplo faiss.

---

- Que estructura de consulta permite la aplicación? es definida por el tipo de sistema que lo almacena, es por lenguaje natural, todo  se usa con SQL (como lenguaje de consulta)?

UI, lenguaje natural, SQL; drag and drop, prompting, todo lo que nos pueda dar el generador de dashboards.

---

## Preguntas sobre Backend API:
- Como tal el api es dirigida solo al portal web backoffice (solo puede ser accedida desde él)? ya la lógica del mercado por aparte se puede manejar por aparte?

Se necesita el api para todo lo que necesite api. Ustedes sabran, registro, pagos, share data, upload data, confgi data, etc etc.

---

- El resto de sistemas aparte de este backend api si puede estar diseñado con una arquitectura event-driven y microservicios?

es su decisión de diseño.

---

- En una sección dice que el API debe ser monolítica, pero luego dice que debe tener módulos separados. Podemos usar la que creamos mejor desde nuestro punto de vista de desarrolladores de software?

es su decisión de diseño. Eso es un error en la docu voy a revisar.

---

## Preguntas sobre Portal Web de Backoffice:

- Este portal puede ver todos los usuarios existentes, junto con que datasets tienen, y a que organización tienen acceso?

Si bajo los principios de privacidad que deben ser inviolables.

---

- Que personas son los que acceden a este Backoffice. Ya que como tal este sistema no "pertenece" a nadie, quien es el encargado de monitorearlo, somos nosotros?

El dueño es gobierno, lo administran usuarios registrados, para la organización registrada, con los permisos preestablecidos. Por ejemplo si esto lo maneja micitt, o se crea una institucion nueva, o lo maneja el registro nacional. Entonces se debe registrar las personas, registrar la entidad tal cual como cualquier otra, internamente debe existir algún mecanismo para declarar esta organización y el set de usuarios como los admins de la plataforma, y asi con todos los usuarios que sean necesarios, recordando que esa organización no son dueños de los datos, son custodios y facilitadores únicamente.

---

## Preguntas sobre Requerimientos del Datalake (o equivalente funcional):

- **Nuevamente esta duda, cuando se ingresan los datos al "datalake", tienen que mantenerse en su formato de origen, o cuando se hace el proceso de ETDL se pueden mapear a un tipo de esquema específico (relacional, documental)? Esta pregunta es importante porque de ella depende como se van a almacenar los datos en nuestro lake y como será el modelado de los datos.**

Si justo es asi, la gente sube diferentes contenidos, el sistema debe detectar por AI y por la metadata suministrada el "que" es esta información para incorporarla en el diseño "maestro" el cual es un diseño que se auto rediseña. ETDL.

--- 

- Ya que la inteligencia artificial se encargará de "normalizar los modelos de datos, rediseñarlos según uso y relacionarlos automáticamente con datasets existentes", que tipo de pruebas, o como debemos monitorear que lo que haga el IA sea correcto. Ya que en caso de dejarla en "modo automático", las probabilidades de que heche a perder la información son altas.

Existes test para agentes de AI, ahi hay que buscar los que necesitamos para garantizar esto, incluso también podría haber aprobación humana previa también de lo sugerido por la AI.