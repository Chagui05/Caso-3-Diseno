# Caso-3-Diseno

## 1. Planeamiento

### Estructura del Equipo, Stakeholders, Key Players
Definición de estructura del equipo, Stakeholders (Matríz de StakeHolders), Key Players y Sistemas y Ecosistemas de Software Existentes

### Gestión de la Comunicación y Documentación del proyecto

### Entendimiento del problema

entrevistas y diagramas de flujo ... 

### Customer Journeys
Al menos 3 customer journeys completos y visuales, con Service Design y que use herramientas como Blueprints, Value Maps o UX Journey Maps

### Plan de ejecución del proyecto 
Plan de ejecución del proyecto con un timeline visual y tareas por etapa

### WBS del sistema 
Creación de WBS del sistema

### Evaluación de Riesgos
Evaluación de riesgos utilizando metodologías reconocidas como ISO 31000 o NIST RMF o otras tablas similares simplificadas

### KPIs 
Definición de KPIs clave y mecanismos para su recolección y cálculo en cada milestone

## 2. Supuestos del proyecto

### Estándares y Regulaciones
Revisión de estándares y regulaciones nacionales/internacionales, incluyendo Ley 8968 (Costa Rica), GDPR, ISO/IEC 27001, OECD Data Governance y similares

### Prácticas de Manejo de Código
Definir prácticas de manejo de códio (OWASp, Clean Code, Twelve-Factor App), y como las implemtaremos

### Sistema de Versionamiento
que sistema de versionamiento se usará y ramas  (Git Flow, GitHub Actions, Terraform,)

### Sistemas de Teceros
Con que sistemas de terceros se interactuará: apis, protocolos de autenticación (OAuth2, JWT)

### Aspectos de Calidad/SLA
Hacer Enfasis en que será Escalabilidad y Mantenibilidad, Reutilización y Eficiencia y Claridad y Gestión de Complejidad

## 3. Stack Tecnológico 
En cada una documentar versiones de frameworks, SDKs, lenguajes y herramientas utilizadas, así como sus restricciones y licencias  

 - Herramientas para Frontend, Backend, Data
 - Herramientas para AI
 - que sistemas de Terceros, Cloud y Protocolos se usarán 
 - Herramientas para testing y DevOps

## 4. Diseño de los componentes
A conitnuación cada una de estas secciones fue sacada del punto 7 de los documentos del repo del profe, hace falta aplicar cada uno de estos para todos los componentes del sistema
### Análisis del Componente
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
  - Como funcionará el proceso ETDL 
  - Usar como base el proyecto anterior 
  - El diseño de datos considera donde sea necesario prácticas y patrones para AI. Unidad 8.

### Prototipado 
No hace falta implementarlo todo, seguramente solo una prueba de concepto para algunos

### Implementación de Componentes
No hace falta implementarlo todo, seguramente solo una prueba de concepto para algunos
solo si aplica:
 - Incluir guías de integración (how to) y ejemplos de código funcional para los servicios principales
 - Incorporar pruebas de concepto, prototipos o ejemplos que guíen la futura ejecución y validen elecciones tecnológicas

### Pruebas e Integración
Solo explicar como se hará

solo si aplica:
 - Incluir guías de integración (how to) y ejemplos de código funcional para los servicios principales
 - Incorporar pruebas de concepto, prototipos o ejemplos que guíen la futura ejecución y validen elecciones tecnológicas
   
### Despliegue y Mantenimiento
Solo explicar como se hará, tal véz una prueba de concepto

### Diagrama General del Frontend
Este si es general de todos los componentes

### Diagrama General del Backend
Este si es general de todos los componentes

## 5. Validación de los requerimientos
- Validar que el diseño cubre todos los requerimientos funcionales y no funcionales del sistema
- Identificar ventajas y desventajas del diseño, proponiendo mitigaciones a los riesgos y limitaciones
