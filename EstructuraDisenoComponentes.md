# Estructura diseño de Componentes

Este documento se puede usar de referencia para armar la estructura del diseño de los componetes

## 4. Diseño de los componentes

A continuación cada una de estas secciones fue sacada del punto 7 de los documentos del repo del profe.

Además cabe aclarar que cada sección no aplica necesariamente para todos los componentes. Por ejemplo, el motor de transformación no ocupa realmente una sección de frontend ya que toda su funcionalidad ocurre en el backend.

### Diseño de la Arquitectura

- Diseño del Frontend
  - Que sistema de autenticación se usará
  - Como se llevará a cabo el KYC, y la verificación de identidad
  - Arquitectura del Client, N-Layer, Client Server, etc.
  - Componentes Visuales.
  - Patrones y Principios
  - Toolkkits y Standards
  - Estructura de carpetas del sistema
- Diseño del Backend
  - Definir porque el sistema tiene alta disponibilidad y como
  - Definir porque tiene monitoreo y como
  - Definir modelo de seguridad detallado: encriptación, auditoría, logging seguro.
  - REST, GraphQL, gRPC, Monolithic, or Monolithic-MVC?
  - Serverless, Cloud, On-Premise, or Hybrid?
  - Service vs. Microservices?
  - Event-Driven, Queues, Brokers, Producer/Consumer, Pub/Sub?
  - API Gateway (Security & Scalability)?
  - El de arquitectura considera donde sea necesario prácticas y patrones para AI. Unidad 8.
- Diseño de los Datos
  - Usar como base el proyecto anterior
  - El diseño de datos considera donde sea necesario prácticas y patrones para AI. Unidad 8.

### Prototipado

No hace falta implementarlo todo, seguramente solo una prueba de concepto para algunos

### Pruebas e Integración

Solo explicar como se hará

solo si aplica:

- Incluir guías de integración (how to) y ejemplos de código funcional para los servicios principales
- Incorporar pruebas de concepto, prototipos o ejemplos que guíen la futura ejecución y validen elecciones tecnológicas

### Despliegue y Mantenimiento

Solo explicar como se hará, tal véz una prueba de concepto
