# Requerimientos del Sistema

## bioregistro verde

- **R1.** El componente debe permitir el registro de personas físicas, jurídicas, instituciones, cámaras, grupos y empresas.  
- **R2.** El formulario de registro debe adaptarse dinámicamente según el tipo de entidad seleccionada.  
- **R3.** El registro de usuarios debe estar asegurado con MFA y biometría, cumpliendo estándares de identidad digital avanzada.  
- **R4.** El componente debe solicitar y capturar información personal, societaria, legal y tributaria según el tipo de entidad.  
- **R5.** El componente debe revisar que cuando se van a asignar personas físicas a la organización al crearla, efectivamente formen parte de dicho conjunto.  
- **R6.** El registro debe pasar por una etapa de validación interna manual para el registro de empresas.  
- **R7.** El componente debe implementar validación automática por inteligencia artificial de los documentos subidos.  
- **R8.** El componente debe exigir a los representantes legales el registro como individuos con: identidad digital, biometría, prueba de vida y autenticación multifactor (MFA).  
- **R9.** Cada organización debe recibir llaves de seguridad que le permitan delegar o revocar accesos a sus usuarios.  
- **R10.** Un usuario debe poder administrar múltiples organizaciones desde una única cuenta.  
- **R11.** El componente debe capturar datos preliminares de cuentas IBAN y/o tarjetas de crédito como parte del registro.  
- **R12.** El componente debe enviar una notificación por correo electrónico cuando un registro sea aprobado.  
- **R13.** El componente debe exigir documentos específicos según el tipo de entidad: cédulas físicas o jurídicas, actas, RTN, dirección, etc.  
- **R14.** El componente debe permitir registrar direcciones IP institucionales (listas blancas) para permitir acceso autorizado.  
- **R15.** El componente debe permitir únicamente IPs costarricenses en el registro.  
- **R16.** El sistema debe proteger las claves generadas mediante un esquema de llave tripartita, distribuidas entre Data Pura Vida y dos custodios.

## La Bóveda

- **R17.** La Bóveda tiene que almacenar los datos en un solo formato, por más de que las fuentes externas sean de distintos tipos (relacionales, documentales, csv, excel).  
- **R18.** La Bóveda debe permitir especificar columnas que relacionan un dataset con otros datasets del ecosistema.  
- **R19.** La Bóveda debe de estar monitoreada en todo momento para detectar movimientos sospechosos, para dar contenido de uso de un dataset, y para asegurar trazabilidad y diagnóstico rápido de fallas.  
- **R20.** Debe ser resiliente, auditable y alineado con estándares de gobierno de datos.  
- **R21.** Debe permitir crecimiento dinámico sin perder eficiencia.  
- **R22.** Debe escalar a millones de registros y miles de usuarios concurrentes.  
- **R23.** Mantener trazabilidad de datos usados, no usados y descartados.  
- **R24.** Todos los datos cargados deben estar protegidos mediante cifrado, incluso frente al personal técnico ("ingenieros de la plataforma").  
- **R25.** Cifrar toda la data en tránsito y en reposo, dejando trazabilidad auditable.  
- **R26.** Permitir almacenamiento masivo de datos estructurados y semiestructurados.  
- **R27.** Controlar accesos lógicos por entidad, usuario o tipo de dato.  
- **R28.** Implementar control de acceso a nivel de rol (RBAC) y a nivel de fila (RLS) o equivalentes.

## Módulo de Ingesta de dato / posibles nombres: El Ingestor, Centro de Carga, Dock de Datos

- **R29.** Permitir a los usuarios decidir qué datos compartir dentro del ecosistema.  
- **R30.** Requerir que cada dataset tenga un nombre único.  
- **R31.** Soportar múltiples métodos de carga de datos: archivos Excel, CSV, JSON, APIs y conexiones directas a bases de datos SQL y NoSQL.  
- **R32.** Requerir nombre, descripción y metadata útil para IA sobre las columnas del dataset.  
- **R33.** Permitir configurar los parámetros de conexión de forma cifrada para cada medio de carga.  
- **R34.** Los parámetros de conexión de bases de datos y APIs deben almacenarse de forma cifrada.  
- **R35.** Permitir configurar si el dataset es público o privado, gratuito o pagado, permanente o con disponibilidad temporal.  
- **R36.** El sistema de permisos debe prevenir accesos no autorizados a datasets privados o pagos.  
- **R37.** Asignar permisos de acceso a los datasets privados.  
- **R38.** Permitir definir montos de acceso para datasets con modelo de cobro.  
- **R39.** Restringir acceso a datos por tiempo, volumen o frecuencia de consulta.  
- **R40.** Indicar si la carga es única o recurrente, completa o por deltas.  
- **R41.** Configurar parámetros para carga por deltas: campos diferenciales, frecuencia (timed pull) o mediante callbacks.  
- **R42.** Habilitar control granular de acceso por institución, persona o grupo.

## Módulo de transformación de datos / posibles nombres: Motor de Transformación, Procesador ETDL

- **R43.** Validar el formato, estructura y contenido de cada dataset cargado sea correcto, o bien adaptarlo al interno de la Bóveda (formatos de fecha, booleans, etc.).  
- **R44.** Validar el formato, estructura y contenido de cada dataset cargado coincida con lo especificado en el proceso de carga.  
- **R45.** Automatizar el proceso de carga mediante un motor de IA que aplique un flujo ETDL (extracción, transformación, limpieza, detección de contexto, modelado y carga).  
- **R46.** Aplicar IA para normalizar, rediseñar modelos de datos y vincularlos automáticamente.  
- **R47.** Detectar duplicidades, optimizar relaciones y ajustar el modelo de datos automáticamente según las interrelaciones detectadas.  
- **R48.** Monitorear el proceso completo con métricas de transferencia, carga, limpieza, eliminación, modelado, volumen, datos omitidos, datos consultados y tasa de éxito.  
- **R49.** El sistema debe ser capaz de procesar cargas recurrentes y automatizadas sin intervención manual.  
- **R50.** Soportar cargas delta con identificación de cambios.  
- **R51.** Realizar merges eficientes sin pérdida de integridad.

## Centro de Visualización y Consumo

### Generador de dashboards

- **R52.** El sistema debe permitir la construcción de dashboards personalizados de forma manual.  
- **R53.** El sistema debe permitir construir dashboards manualmente o mediante prompts inteligentes que generen visualizaciones automáticas.  
- **R54.** El sistema debe permitir representar visualmente los datos en tablas, gráficos, conteos, tendencias y predicciones.  
- **R55.** El sistema debe permitir a los usuarios guardar sus dashboards personalizados.  
- **R56.** El sistema debe permitir compartir dashboards con otros usuarios o hacerlos públicos dentro de la plataforma.  
- **R57.** La interfaz de construcción de dashboards debe ser segura, intuitiva y con capacidad de respuesta en tiempo real.

### Visualización y Consumo

- **R58.** El sistema debe permitir visualizar todos los datasets accesibles como una fuente consolidada.  
- **R59.** El sistema debe bloquear toda exportación directa de datos y gráficos desde el portal.  
- **R60.** El sistema debe mostrar datos de forma preliminar en modo de construcción de dashboard y luego con datos reales al ejecutar consultas.  
- **R61.** El sistema debe deshabilitar temporalmente el acceso a datasets cuando se superen los límites de consumo.  
- **R62.** El sistema debe registrar todas las transacciones y consumos de datos en un historial accesible para cada usuario.  
- **R63.** El sistema debe mostrar métricas de uso: volumen de datos consultados, número de consultas realizadas, tiempo restante o límites alcanzados.  
- **R64.** El sistema no debe permitir en ningún momento la descarga directa de datasets o gráficos generados.  
- **R65.** La visualización de datos debe realizarse exclusivamente dentro del portal, sin opciones de exportación, captura o embedding externo.  
- **R66.** Los límites de consumo deben aplicarse en tiempo real, sin permitir bypasses o reintentos abusivos.

### Consumo para IA

- **R67.** El sistema debe permitir el acceso sistema a sistema únicamente para alimentar modelos de IA aprobados.  
- **R68.** La entrega de datos para modelos de IA debe ser monitoreada, registrada y limitada a contextos aprobados explícitamente por Data Pura Vida.  
- **R69.** El sistema debe ofrecer plataformas limitadas y controladas para esta alimentación de IA. Solo permitirá 2 por usuario.  
- **R70.** El sistema debe minimizar al máximo el riesgo de descargas indirectas mediante presunción de uso en IA.  
- **R71.** Los datos deben ser envíados en un formato que no permita poder ser desencriptado para otro uso que no sea alimentar IA (por ejemplo uso de embeddings).

## Marketplace

- **R72.** La experiencia de compra de datasets debe ser fluida, transparente y accesible desde los dashboards personales.  
- **R73.** Incluir un módulo de compra donde se visualicen datasets disponibles bajo acceso pagado.  
- **R74.** Permitir seleccionar un dataset, visualizar precio, términos de uso, duración del acceso y condiciones de cobro.  
- **R75.** Soportar múltiples métodos de pago: tarjeta de crédito, débito y otros mecanismos nacionales compatibles.  
- **R76.** Mostrar confirmaciones de transacción y activar el acceso según condiciones (tiempo, volumen, frecuencia).  
- **R77.** El sistema debe mostrar opciones para renovar o ampliar los paquetes de acceso en caso de superar el límite.

## Backoffice Administrativo

- **R78.** Administrar usuarios: validación de identidad, membresía y roles.  
- **R79.** Gestionar reglas de carga de datos (formatos, estructuras, validaciones).  
- **R80.** Configurar conexiones externas (APIs, BDs, callbacks).  
- **R81.** Activar, desactivar y supervisar objetos de datos, pipelines y flujos.  
- **R82.** Revocar o regenerar llaves de seguridad (simétricas, asimétricas, tri-partitas).  
- **R83.** Administrar custodios de llaves y flujos de confirmación mancomunada.  
- **R84.** Auditar operaciones por usuario, fecha, acción y resultado.  
- **R85.** Generar reportes de uso, calidad, integración y anomalías.  
- **R86.** Monitorear el estado operativo de servicios y tareas.  
- **R87.** Extraer evidencias para procesos legales bajo autorización.  
- **R88.** Gestionar permisos y accesos mediante RBAC.  
- **R89.** Debe ofrecer una interfaz robusta y segura solo para personal autorizado.  
- **R90.** Debe permitir gestión flexible pero estricta de accesos y configuraciones.


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
- RNF01: Debe desarrollarse con la misma tecnología cloud usada en los portales web.
- RNF02: Debe protegerse con whitelist de IPs, tokens y MFA.
- RNF04: El versionado debe garantizar compatibilidad hacia atrás en la medida de lo posible.
- RNF05: Todas las transacciones deben cumplir con requerimientos legales y dejar trazabilidad.