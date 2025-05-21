# Requerimientos del Sistema

## Requerimientos Generales

- RNF1: La documentación y el sistema será escrito en español.


## bio registro verde

### Requerimientos Funcionales 

- RF1: El sistema debe permitir el registro de personas físicas, jurídicas, instituciones, cámaras, grupos y empresas.
- RF2: El formulario de registro debe adaptarse dinámicamente según el tipo de entidad seleccionada.
- RF3: El sistema debe solicitar y capturar información personal, societaria, legal y tributaria según el tipo de entidad.
- RF4: El sistema debe revisar que cuando se van a asignar personas físicas a la organización al crearla, efectivamente formen parte de dicho conjunto.
- RF5: El registro debe pasar por una etapa de validación interna manual, con estados como: pendiente, aprobado, rechazado.
- RF6: El sistema debe implementar validación automática por inteligencia artificial de los documentos subidos.
- RF7: El sistema debe exigir a los representantes legales el registro como individuos con: identidad digital, biometría, prueba de vida y autenticación multifactor (MFA).
- RF8: Cada organización debe recibir llaves de seguridad que le permitan delegar o revocar accesos a sus usuarios.
- RF9: Un usuario debe poder administrar múltiples organizaciones desde una única cuenta.
- RF10: El sistema debe capturar datos preliminares de cuentas IBAN y/o tarjetas de crédito como parte del registro.
- RF11: El sistema debe enviar una notificación por correo electrónico cuando un registro sea aprobado.
- RF12: El sistema debe exigir documentos específicos según el tipo de entidad: cédulas físicas o jurídicas, actas, RTN, dirección, etc.
- RF13: El sistema debe permitir registrar direcciones IP institucionales (listas blancas) para permitir acceso autorizado.

### Requerimientos No Funcionales 

- RNF1: El sistema debe implementar validaciones inteligentes con IA personalizadas a los requisitos según el tipo de entidad.
- RNF2: El sistema debe restringir el acceso al portal exclusivamente a IPs ubicadas en Costa Rica.
- RNF3: El sistema debe generar claves criptográficas (simétricas y asimétricas) para cada entidad o persona registrada.
- RNF4: El sistema debe proteger las claves generadas mediante un esquema de llave tripartita, distribuidas entre Data Pura Vida y dos custodios.
- RNF5: Las autenticaciones deben soportar MFA y biometría, cumpliendo estándares de identidad digital avanzada.

## Feliz Compartiendo Datos

### Carga y publicación de datos

- RF1: Permitir a los usuarios decidir qué datos compartir dentro del ecosistema.
- RF2: Soportar múltiples métodos de carga de datos: archivos Excel, CSV, JSON, APIs y conexiones directas a bases de datos SQL y NoSQL.
- RF3: Permitir configurar los parámetros de conexión de forma cifrada para cada medio de carga.
- RF4: Requerir nombre, descripción y metadata útil para IA sobre las columnas del dataset.
- RF5: Validar el formato, estructura y contenido de cada dataset cargado.
- RF6: Requerir que cada dataset tenga un nombre único.
- RF7: Indicar si la carga es única o recurrente, completa o por deltas.
- RF8: Configurar parámetros para carga por deltas: campos diferenciales, frecuencia (timed pull) o mediante callbacks.

### Privacidad, permisos y configuración de acceso

- RF9: Permitir configurar si el dataset es público o privado, gratuito o pagado, permanente o con disponibilidad temporal.
- RF10: Habilitar control granular de acceso por institución, persona o grupo.
- RF11: Asignar permisos de acceso a los datasets privados.
- RF12: Permitir seleccionar campos específicos del dataset a cifrar.
- RF13: Restringir acceso a datos por tiempo, volumen o frecuencia de consulta.
- RF14: Definir si el acceso a los datos es de solo lectura o también escritura, y el mecanismo de escritura (API, archivo o conexión directa).

### Relaciones y modelado

- RF15: Permitir especificar columnas que relacionan un dataset con otros datasets del ecosistema.

### Procesamiento inteligente

- RF16: Automatizar el proceso de carga mediante un motor de IA que aplique un flujo ETDL (extracción, transformación, limpieza, detección de contexto, modelado y carga).

- RF17: Detectar duplicidades, optimizar relaciones y ajustar el modelo de datos automáticamente según las interrelaciones detectadas.

### Monitoreo y métricas
- RF18: Monitorear el proceso completo con métricas de transferencia, carga, limpieza, eliminación, modelado, volumen, datos omitidos, datos consultados y tasa de éxito.

### Comercialización de datasets

- RF19: Permitir definir montos de acceso para datasets con modelo de cobro.
- RF20: Incluir un módulo de compra donde se visualicen datasets disponibles bajo acceso pagado.
- RF21: Permitir seleccionar un dataset, visualizar precio, términos de uso, duración del acceso y condiciones de cobro.
- RF22: Soportar múltiples métodos de pago: tarjeta de crédito, débito y otros mecanismos nacionales compatibles.
- RF23: Asignar automáticamente los permisos de acceso una vez confirmado el pago.
- RF24: Mostrar confirmaciones de transacción y activar el acceso según condiciones (tiempo, volumen, frecuencia).

### Seguridad
- RNF1: Todos los datos cargados deben estar protegidos mediante cifrado, incluso frente al personal técnico ("ingenieros de la plataforma").
- RNF2: Los parámetros de conexión de bases de datos y APIs deben almacenarse de forma cifrada.
- RNF3: El sistema de permisos debe prevenir accesos no autorizados a datasets privados o pagos.

### Disponibilidad y rendimiento
- RNF4: El sistema debe ser capaz de procesar cargas recurrentes y automatizadas sin intervención manual.
- RNF5: El monitoreo debe ser en tiempo real o casi real para asegurar trazabilidad y diagnóstico rápido de fallas.

### Usabilidad
- RNF6: El usuario debe recibir confirmaciones claras e inmediatas sobre el estado de sus cargas, pagos y accesos.
- RNF7: La experiencia de compra de datasets debe ser fluida, transparente y accesible desde los dashboards personales.

## Descubriendo Costa Rica

### Visualización y exploración
- RF1: El sistema debe permitir visualizar todos los datasets accesibles como una fuente consolidada.
- RF2: El sistema debe permitir la construcción de dashboards personalizados de forma manual.
- RF3: El sistema debe permitir la construcción de dashboards mediante prompts inteligentes utilizando IA generativa.
- RF4: El sistema debe permitir representar visualmente los datos en tablas, gráficos, conteos, tendencias y predicciones.
- RF5: El sistema debe mostrar los dashboards primero con datos preliminares (modo de diseño) y luego con datos reales al ejecutar consultas.
- RF6: El sistema debe bloquear toda exportación directa de datos y gráficos desde el portal.

### Dashboards y colaboración
- RF7: El sistema debe permitir a los usuarios guardar sus dashboards personalizados.
- RF8: El sistema debe permitir compartir dashboards con otros usuarios o hacerlos públicos dentro de la plataforma.

### Control de consumo
- RF9: El sistema debe visualizar en tiempo real el consumo de datos pagados dentro de los dashboards.
- RF10: El sistema debe mostrar métricas de uso: volumen de datos consultados, número de consultas realizadas, tiempo restante o límites alcanzados.
- RF11: El sistema debe deshabilitar temporalmente el acceso a datasets cuando se superen los límites de consumo.
- RF12: El sistema debe mostrar opciones para renovar o ampliar los paquetes de acceso en caso de superar el límite.
- RF13: El sistema debe registrar todas las transacciones y consumos de datos en un historial accesible para cada usuario.

### Interacción sistema a sistema para IA
- RF14: El sistema debe permitir el acceso sistema a sistema únicamente para alimentar modelos de IA aprobados.
- RF15: El sistema debe ofrecer plataformas limitadas y controladas para esta alimentación de IA.
- RF16: El sistema debe entregar los datos en forma vectorial (opcional) como método controlado de acceso para IA.
- RF17: El sistema debe minimizar al máximo el riesgo de descargas indirectas mediante presunción de uso en IA.

### Requerimientos No Funcionales
- RNF1: El sistema no debe permitir en ningún momento la descarga directa de datasets o gráficos generados.
- RNF2: La visualización de datos debe realizarse exclusivamente dentro del portal, sin opciones de exportación, captura o embedding externo.
- RNF3: La interfaz de construcción de dashboards debe ser segura, intuitiva y con capacidad de respuesta en tiempo real.
- RNF4: La IA usada para generación de visualizaciones debe preservar la privacidad de los datos y no enviar información sensible a servicios externos sin anonimización.
- RNF5: Los límites de consumo deben aplicarse en tiempo real, sin permitir bypasses o reintentos abusivos.
- RNF6: La entrega de datos para modelos de IA debe ser monitoreada, registrada y limitada a contextos aprobados explícitamente por Data Pura Vida.
- RNF7: Todo el historial de consumo debe estar disponible para los usuarios bajo un esquema de auditoría simple y verificable.


## Pura vida data lake

###  Backend API
- RF01: La API debe proveer autenticación, validación de identidad y gestión de usuarios.
- RF02: Debe permitir operaciones sobre datasets: creación, edición, eliminación y consulta.
- RF03: Gestionar llaves de acceso, incluyendo generación, revocación y expiración.
- RF04: Incluir endpoints para métricas del sistema y monitoreo de procesos.
- RF05: Ejecutar procesos administrativos como aprobación, auditoría y mantenimiento de entidades.
- RF06: Debe contar con módulos para:
    - Gestión de credenciales
    - Firmas digitales
    - Cifrado de datos
    - Monitoreo de integridad
    - Auditoría de eventos
- RF07: Permitir gestión de accesos temporales y granularidad por rol y contexto.
- RF08: Implementar versionamiento de endpoints.

### Portal Web de Backoffice
- RF09: Administrar usuarios: validación de identidad, membresía y roles.
- RF10: Gestionar reglas de carga de datos (formatos, estructuras, validaciones).
- RF11: Configurar conexiones externas (APIs, BDs, callbacks).
- RF12: Activar, desactivar y supervisar objetos de datos, pipelines y flujos.
- RF13: Revocar o regenerar llaves de seguridad (simétricas, asimétricas, tri-partitas).
- RF14: Administrar custodios de llaves y flujos de confirmación mancomunada.
- RF15: Auditar operaciones por usuario, fecha, acción y resultado.
- RF16: Generar reportes de uso, calidad, integración y anomalías.
- RF17: Monitorear el estado operativo de servicios y tareas.
- RF18: Extraer evidencias para procesos legales bajo autorización.
- RF19: Gestionar permisos y accesos mediante RBAC.

### Datalake o Infraestructura Equivalente
- RF20: Permitir almacenamiento masivo de datos estructurados y semiestructurados.
- RF21: Detectar y evitar duplicidad de datos en cargas.
- RF22: Soportar cargas delta con identificación de cambios.
- RF23: Realizar merges eficientes sin pérdida de integridad.
- RF24: Mantener trazabilidad de datos usados, no usados y descartados.
- RF25: Proveer monitoreo en tiempo real del estado operativo.
- RF26: Controlar accesos lógicos por entidad, usuario o tipo de dato.
- RF27: Implementar control de acceso a nivel de rol (RBAC) y a nivel de fila (RLS).
- RF28: Impedir acceso directo de personal técnico sin autorización a datos sensibles.
- RF29: Cifrar toda la data en tránsito y en reposo, dejando trazabilidad auditable.
- RF30: Aplicar IA para normalizar, rediseñar modelos de datos y vincularlos automáticamente.

### Backend API
- RNF01: Debe desarrollarse con la misma tecnología cloud usada en los portales web.
- RNF02: Debe protegerse con whitelist de IPs, tokens y MFA.
- RNF03: Inicialmente debe seguir una arquitectura monolítica con posibilidad de migración a microservicios.
- RNF04: El versionado debe garantizar compatibilidad hacia atrás en la medida de lo posible.
- RNF05: Todas las transacciones deben cumplir con requerimientos legales y dejar trazabilidad.

### Portal Web Backoffice
- RNF06: Debe ofrecer una interfaz robusta y segura solo para personal autorizado.
- RNF07: Toda acción debe ser auditable y segura.
- RNF08: Debe permitir gestión flexible pero estricta de accesos y configuraciones.

### Datalake
- RNF09: Debe escalar a millones de registros y miles de usuarios concurrentes.
- RNF10: Debe ser resiliente, auditable y alineado con estándares de gobierno de datos.
- RNF11: Debe impedir accesos privilegiados no autorizados, incluso por DevOps e ingenieros de datos.
- RNF12: Debe asegurar confidencialidad y trazabilidad total de accesos a datos sensibles.
- RNF13: Debe permitir crecimiento dinámico sin perder eficiencia.
- RNF14: El diseño debe ser flexible: no se requiere estructura técnica clásica, pero sí equivalencia funcional.
