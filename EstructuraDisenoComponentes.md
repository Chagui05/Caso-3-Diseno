# Estructura diseño de Componentes

Este documento se puede usar de referencia para armar la estructura del diseño de los componetes

Además cabe aclarar que cada sección no aplica necesariamente para todos los componentes. Por ejemplo, el motor de transformación no ocupa realmente una sección de frontend ya que toda su funcionalidad ocurre en el backend.

----

- Diseño del Frontend
  - Plataforma de Autenticación (En la mayoría no hace falta)
  - Arquitectura del Client, N-Layer, Client Server, etc.
  - Patrones de Diseño de Objetos
  - Componentes Visuales.
    - Patrones y Principios: Revisar Capítulo 4 del profe en github
    - Toolkits y Standards
  - Estructura de carpetas del sistema
  - Diagrama de Frontend

----
- Diseño del Backend
  - Diagrama de Clases
  - Explicación de las capas: Pueden variar, pero pueden ser de lógica de negocio, persistencia, handlers, etc.
  - Servicios de AWS: cuales servicios se usarán, y que configuración de hardware necesitan.
  - Microservicios en el Componentes: Listar cuales microservicios están en cada componente, por ejemplo, en el bioregistro hay un microservicio de interacción con SumSub, o en el Motor de Transformaación hay un microservicio de merging de tablas. Aquí también aplica hablar en que partes y como se usará Event-Driven si es necesario. Además de listarlos hay que decir que hacen y explicar que herramientas van a utilizar (Por ejemplo, el merger del motor de transformación usa spark para transformar N tablas en solo 1).
  - Monitoreo: Define como se va a monitorear, usualmente los microservicios es con Prometheus, y los servicios de AWS con CloudWatch, pero especificar como.
  - Modelo de seguridad detallado: encriptación, auditoría, logging seguro. Solo si aplica.
  - Elementos de Alta Disponibilidad: Cómo se va a garantizar la disponibilidad del sistema, por ejemplo, con réplicas, load balancing, etc.
  - Aporte al API Gateway: Ya que el API Gateway es la misma para todo el backend especificar que aporta este módulo a ella
  - Diagrama del Backend

----
- Diseño de los Datos: para esta sección usar la sección de diseño de la [capa de datos](https://github.com/vsurak/cursostec/blob/master/diseno/3.%20dise%C3%B1o%20de%20la%20l%C3%B3gica%20y%20los%20datos%2C%20o%20backend%20y%20data.md#dise%C3%B1o-de-la-capa-de-datos) del capítulo 3 del github del profe. También se puede usar como base el [Proyecto Pasado](https://github.com/Chagui05/Caso-2-diseno?tab=readme-ov-file#data-layer-design). En el documento de [semana 9](https://github.com/vsurak/cursostec/blob/master/diseno/week%209%20-10.md#week-9-1) el profe también comenta esta parte.
  - Topología de Datos
  - Motor de Base de Datos
  - Tenancy, Seguridad y Privacidad
  - Recuperación de Datos y Protección del Sistema
  - Conexión a Base de datos
    - ORM, como usaremos el ORM
    - Connection Pool, como se usará el connection pool
    - Drivers
  - Diseño para IA: El diseño de datos considera donde sea necesario prácticas y patrones para AI. [Unidad 8](https://github.com/vsurak/cursostec/blob/master/diseno/8.%20Tendencias%20en%20el%20dise%C3%B1o%20de%20software.md).
  - Diagrama de Base de Datos

----

Prototipado

No hace falta implementarlo todo, seguramente solo una prueba de concepto para algunos

----

Pruebas e Integración

Solo explicar como se hará

solo si aplica:

- Incluir guías de integración (how to) y ejemplos de código funcional para los servicios principales
- Incorporar pruebas de concepto, prototipos o ejemplos que guíen la futura ejecución y validen elecciones tecnológicas

----

Despliegue y Mantenimiento

Solo explicar como se hará, tal véz una prueba de concepto
