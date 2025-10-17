# Servicio de Blog (blog-service)

El servicio de blog es un componente central dentro de la arquitectura de microservicios que gestiona todo lo relacionado con las publicaciones, autores y categorías del sistema. Este servicio está diseñado para funcionar de manera independiente mientras se integra perfectamente con otros microservicios como `auth-service` y `email-service`.

## Descripción

Este servicio se encarga de la gestión completa del contenido del blog, incluyendo la creación, edición, eliminación y consulta de publicaciones. Proporciona una API RESTful robusta que permite a otros servicios y al frontend interactuar con el contenido del blog de manera eficiente.

### Funcionalidades Principales

- **Gestión de Publicaciones**: Crear, leer, actualizar y eliminar posts del blog
- **Gestión de Autores**: Administración de perfiles de autores y sus publicaciones
- **Sistema de Categorías**: Organización del contenido mediante categorías temáticas
- **API RESTful**: Endpoints bien definidos para todas las operaciones CRUD
- **Integración con Autenticación**: Validación de tokens JWT del `auth-service`
- **Notificaciones**: Integración con `email-service` para notificar sobre nuevas publicaciones

### Características Técnicas

- **Persistencia de Datos**: Utiliza PostgreSQL para almacenar toda la información
- **Cache**: Implementa Redis para mejorar el rendimiento de consultas frecuentes
- **Validación de Datos**: Validación robusta de entrada y salida de datos
- **Paginación**: Soporte para paginación en listados de publicaciones
- **Filtros y Búsqueda**: Capacidades de filtrado por categoría, autor y búsqueda de texto

## Tecnologías

- **Django**: Framework web de Python para el desarrollo del backend
- **Django REST Framework**: Para la creación de APIs RESTful
- **PostgreSQL**: Base de datos relacional principal
- **Redis**: Sistema de cache en memoria
- **Docker**: Containerización del servicio
- **Docker Compose**: Orquestación de contenedores

## Arquitectura del Servicio

### Modelos de Datos

- **Post**: Representa una publicación del blog
  - Título, contenido, fecha de creación/actualización
  - Relación con autor y categoría
  - Estado de publicación (borrador/publicado)

- **Author**: Información del autor
  - Perfil del autor, biografía
  - Relación con el sistema de autenticación

- **Category**: Categorías para organizar el contenido
  - Nombre, descripción, slug
  - Jerarquía de categorías (opcional)

### Endpoints Principales

```
GET    /api/posts/          # Listar publicaciones
POST   /api/posts/          # Crear nueva publicación
GET    /api/posts/{id}/     # Obtener publicación específica
PUT    /api/posts/{id}/     # Actualizar publicación
DELETE /api/posts/{id}/     # Eliminar publicación

GET    /api/authors/        # Listar autores
GET    /api/authors/{id}/   # Obtener autor específico

GET    /api/categories/     # Listar categorías
POST   /api/categories/     # Crear nueva categoría
```

## Instalación y Configuración

### Prerequisitos

Asegúrate de tener instalados los siguientes componentes:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Python 3.9+ (para desarrollo local)

### Pasos para ejecutar el servicio

1. **Clona el repositorio**

   ```bash
   git clone https://github.com/tu_usuario/microservicios-lab.git
   cd microservicios-lab/blog-service
   ```

2. **Configura las variables de entorno**

   Copia el archivo `.env.example` a `.env` y ajusta los valores según tu configuración:

   ```bash
   cp .env.example .env
   ```

   Variables importantes a configurar:
   ```env
   DATABASE_URL=postgresql://devuser:devpass@postgres:5432/main_db
   REDIS_URL=redis://redis:6379/0
   SECRET_KEY=tu_clave_secreta_django
   DEBUG=True
   AUTH_SERVICE_URL=http://auth-service:8000
   EMAIL_SERVICE_URL=http://email-service:8000
   ```

3. **Ejecuta los servicios de base de datos**

   Desde el directorio raíz del proyecto:

   ```bash
   docker-compose up -d postgres redis
   ```

4. **Construye y ejecuta el servicio**

   ```bash
   docker-compose up --build blog-service
   ```

   O para desarrollo local:

   ```bash
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver 8002
   ```

## Desarrollo

### Estructura del Proyecto

```
blog-service/
├── blog/                   # Aplicación principal de Django
│   ├── models.py          # Modelos de datos
│   ├── serializers.py     # Serializadores DRF
│   ├── views.py           # Vistas de la API
│   └── urls.py            # Configuración de URLs
├── config/                # Configuración de Django
│   ├── settings.py        # Configuraciones
│   └── urls.py            # URLs principales
├── requirements.txt       # Dependencias de Python
├── Dockerfile            # Configuración de Docker
├── manage.py             # Script de gestión de Django
└── README.md             # Este archivo
```

### Comandos Útiles

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar tests
python manage.py test

# Recopilar archivos estáticos
python manage.py collectstatic
```

## Integración con otros Servicios

### Auth Service
- Valida tokens JWT para operaciones que requieren autenticación
- Obtiene información del usuario autenticado para asociar con publicaciones

### Email Service
- Envía notificaciones cuando se publican nuevos posts
- Notifica a suscriptores sobre actualizaciones de categorías de interés

### Frontend
- Proporciona datos para la interfaz de usuario React
- Recibe solicitudes de creación y edición de contenido

## API Documentation

La documentación completa de la API está disponible en:
- Swagger UI: `http://localhost:8002/swagger/`
- ReDoc: `http://localhost:8002/redoc/`

## Testing

```bash
# Ejecutar todos los tests
python manage.py test

# Ejecutar tests con coverage
coverage run --source='.' manage.py test
coverage report
```

## Deployment

Para producción, asegúrate de:

1. Configurar `DEBUG=False`
2. Usar una base de datos PostgreSQL dedicada
3. Configurar un servidor Redis externo
4. Implementar SSL/TLS
5. Configurar logging apropiado
6. Usar un servidor web como Nginx + Gunicorn

## Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Soporte

Para reportar bugs o solicitar nuevas funcionalidades, por favor crea un issue en el repositorio del proyecto.