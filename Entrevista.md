# Entrevista

## Bio Registro Verde 

- Se ocupa que el hosteo del sistema sea on-premise, cloud o híbrido? En caso de ser híbrido se le debe dar la opción al usuario para elegir si almacenar sus datos en territorio nacional, o usted como PO ya tiene la distribución hecha. 

- En que idioma debe estar la documentación y la aplicación

- Se espera que se permita tanto el registro de instituciones como de personas. Pero en otra sección se dice que desde una misma cuenta se pueden administrar varias organizaciones. Lo cual deja la pregunta como es la "Jerarquía" para la creación de cuentas asociadas a organizaciones (camaras, grupos y empresas), ¿se manejarán por medio de una cuenta "central", y luego con las llaves de seguridad, una persona física puede tener un acceso secundario a dicha organizacíon?

- Exactamente que completitud se desea validar con la IA? Porque es posible que ocupemos entrenar modelos tomando en cuenta que existen servicios como SumSub que ya se encargan de esto.

- Existen sistemas que facilitan el registro de KYC, como SumSub (tiene soporte en costa rica) gracias a su SDK. ¿Se puede usar este servicio para el registro biométrico y comprobación de identidad, o se desea que se cree un sistema manual desde 0? 

- El proceso de validación interna de las cuentas aplica para todo tipo de cuenta? 

- ¿El proceso de validación interna se realiza un equipo humano, un flujo automatizado, o ambos?

- Además, que parte de la validación interna debe ser realizada por nosotros si ya se va a integrar a sistemas de terceros como SumSub

- "Restringir el acceso al portal solo desde direcciones IP ubicadas en Costa Rica", puede resultar limitante para costarricenses que se encuentren de viaje en el extranjero. En su lugar, podría considerarse aplicar esta restricción solo a la página de registro.

- Cual es la razón para capturar la cuenta de IBAN y tarjetas de crédito en el registro, ¿Por qué este proceso no se realiza luego, solo en caso de que el usuario esté interesado en realizar o recibir pagos?

- En cuanto al proceso de pago por acceso a datos, ¿la conciliación debe realizarse de forma externa entre las partes interesadas (por ejemplo, acordando transferencias vía SINPE o bancarias)? ¿O se contempla la posibilidad de integrar un sistema de pagos de terceros, como Stripe, para gestionar las transacciones directamente desde la plataforma?

- En caso de que los pagos se hagan dentro del sistema, se requiere confirmar nuevamente con la clave criptográfica?

- Quién define la whitelist para el sistema?

## Feliz compartiendo datos

- Se espera que internamente, independientemente de la fuente de datos (excel, csv, NoSql-Documental, SQL, etc.), despues de ser subidos y aplicado el proceso de ETDL si use un formato unificado dentro de la BD, o se mantendrá el formato de origen?

- Con los datos proporcionados por conexión directa a BDs externas, se espera siempre obtener los datos mediante dicho connection string, o se hace una snapshot de dicha base de datos dentro de nuestra infraestructura cada n tiempo (definido por el usuario)?

- "Requerir nombre, descripción y metadata útil para IA sobre las columnas del dataset", ya las bases de datos tienen que traer esos datos internamente, o se dan al ingresar al sistema, y nosotros "Manualmente" tenemos que agregarlo a cada fila/documento. 

- El flujo ETDL con IA se construye desde cero o se pueden integrar motores existentes como Apache Nifi, Talend o similares?

- Que implica "Validar el formato, estructura y contenido de cada dataset compartido", suena muy general, que formatos y estructuras son los que se tienen que validar.

- Que modelos de cobro se implementaran, por uso (como para apis), pago único (dataset permanente), por suscripcion (dataset con disponibilidad temporal), etc.?

- Que implica que un Dataset también tenga escritura? se refiere a que los usuarios externos puedan modificar su interior?

- "Detectar y evitar duplicidades, optimizar relaciones con datos ya existentes y ajustar el modelo de datos en función de las interrelaciones", este requirimiento es parte del flujo ETDL de la IA?

- Con respecto a "Monitorear todo el proceso con métricas de transferencia, carga, limpieza, eliminación, modelado, volumen, datos omitidos, datos consultados y tasa de éxito", donde se deben mostrar dichas métricas y cuando? debe ser siempre que se cargue un nuevo dataset, o una actualización? quedan en un historial?

- Como dar garantía de que los datos a vender son verídicos? existe la posibilidad de dar una "preview" al comprador para que sepa más o menos que va a comprar?

## Descubriendo Costa Rica

- Al entrar al Dashboard no hay gráficos listos, y el usuario debe crearlos? O el que se los vendió previamente creo unos dashboards default?

- Debe existir una herramienta para que los tenientes de datasets puedan crear dashboards antes de sacarlos al mercado, para que los compradores obtengan los datos ya con dashboards hecho.

- Que estructura de consulta permite la aplicación? es definida por el tipo de sistema que lo almacena, es por lenguaje natural, todo se usa con SQL (como lenguaje de consulta)?

- Se comentó de usar visualizadores de data como Power BI, Kibana o Tableau, como se pretende esta integración? ya que como tal no están diseñados para embedir tablas en la web.

- La opción de compartir dashboards se hace por medio de una sección de comunidad con dashboards vacíos creados por usuarios? o se comparte generando un JSON que luego se cargue para mostrar los dashboards (como en el caso de grafana)?

- Qué criterios definen cuándo un acceso sistema-a-sistema para alimentar una IA está autorizado? Hace falta firmar un contrato de que los datos solo serán usados para dichos fines?

- Para el envío de data por medio de vectores. Esto hace referencia a que los datos se mandan listos para ya ser procesados por la IA en un formato que no es posible usar para otro método que no sea entrenado de inteligencia artificial? En dicho caso habría que tener un "módulo" en nuestro backend que vectorice las entradas de una BD (podríamos usar modelos de hugging face pre-entrenados como all-mpnet-base-v2).


## Pura vida data lake

### Backend API 

- Como tal el api es dirigida solo al portal web backoffice (solo puede ser accedida desde él)? ya la lógica del mercado por aparte se puede manejar por aparte? 

- El resto de sistemas aparte de este backend api si puede estar diseñado con una arquitectura event-driven y microservicios?

- En una sección dice que el API debe ser monolítica, pero luego dice que debe tener módulos separados. Podemos usar la que creamos mejor desde nuestro punto de vista de desarrolladores de software?

- Las opciones sobre el control granular son totalmente parametrizadas por el usuario?

###  Portal Web de Backoffice

- Este portal puede ver todos los usuarios existentes, junto con que datasets tienen, y a que organización tienen acceso?

- Que personas son los que acceden a este Backoffice. Ya que como tal este sistema no "pertenece" a nadie, quien es el encargado de monitorearlo, somos nosotros?

### Requerimientos del Datalake (o equivalente funcional)

- Nuevamente esta duda, cuando se ingresan los datos al "datalake", tienen que mantenerse en su formato de origen, o cuando se hace el proceso de ETDL se pueden mapear a un tipo de esquema específico (relacional, documental? Esta pregunta es importante porque de ella depende como se van a almacenar los datos en nuestro lake y como será el modelado de los datos.

- Ya que la inteligencia artificial se encargará de "normalizar los modelos de datos, rediseñarlos según uso y relacionarlos automáticamente con datasets existentes", que tipo de pruebas, o como debemos monitorear que lo que haga el IA sea correcto. Ya que en caso de dejarla en "modo automático", las probabilidades de que heche a perder la información son altas.

