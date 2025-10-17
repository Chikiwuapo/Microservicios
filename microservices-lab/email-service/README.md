# Servicio de Correo Electrónico (email-service)

El servicio de correo electrónico es uno de los componentes fundamentales dentro de la arquitectura de microservicios que facilita la comunicación por correo electrónico entre los diferentes servicios. Este servicio es responsable de enviar notificaciones por correo electrónico a los usuarios, y su configuración está optimizada para integrarse de forma transparente con otros microservicios, como `auth-service` y `blog-service`.

## Descripción

Este servicio se encarga de enviar correos electrónicos a los usuarios en base a solicitudes provenientes de otros microservicios. Puede ser utilizado para notificar a los usuarios sobre actualizaciones, cambios de contraseña, confirmaciones de registro, entre otros.

### Funcionalidades

- **Envío de correos electrónicos**: Se utiliza para enviar correos a los usuarios en diversas situaciones (ej., registro, notificaciones de blog, alertas, etc.)
- **Plantillas de correo**: Las plantillas de correo electrónico son dinámicas y configurables según las necesidades del sistema.
- **Configuración de SMTP**: El servicio está preparado para ser configurado con un servidor SMTP de terceros (como Gmail, SendGrid, etc.)
  
## Tecnologías

- Node.js (o el lenguaje de preferencia)
- Docker
- API RESTful
- Configuración con Docker Compose

## Instalación

### Prerequisitos

Asegúrate de tener Docker y Docker Compose instalados en tu máquina. Si no tienes estos programas, puedes instalarlos siguiendo los siguientes enlaces:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Pasos para ejecutar el servicio

1. **Clona el repositorio**

   ```bash
   git clone https://github.com/tu_usuario/microservicios-lab.git
   cd microservicios-lab/email-service

2. **Configura las variables de entorno**

Copia el archivo .env.example a .env y ajusta los valores según tu configuración de correo electrónico (por ejemplo, servidor SMTP, credenciales, etc.)

- cp .env.example .env

Asegúrate de configurar las variables correctas para el servidor SMTP que estés utilizando.

3. **Construye y ejecuta los contenedores Docker**

Si ya tienes Docker Compose configurado, puedes iniciar el servicio utilizando:

- docker-compose up --build

Esto construirá las imágenes necesarias y levantará los contenedores para que el servicio esté operativo.