# 🏗️ Laboratorio de Microservicios (Django + React)

Este proyecto implementa una arquitectura de microservicios completa utilizando Django para los servicios backend, React para el frontend, y Docker Compose para la orquestación de contenedores.

## 📋 Descripción del Proyecto

El **Microservices Lab** es un sistema distribuido que demuestra las mejores prácticas en el desarrollo de microservicios. Cada servicio tiene una responsabilidad específica y se comunica con otros servicios a través de APIs REST bien definidas.

### 🎯 Objetivos del Proyecto
- Implementar una arquitectura de microservicios escalable
- Demostrar la comunicación entre servicios independientes
- Utilizar contenedores Docker para el despliegue
- Implementar patrones de diseño de microservicios
- Proporcionar una base sólida para el aprendizaje y desarrollo

## 🏛️ Arquitectura del Sistema

### Diagrama de Arquitectura
```
┌─────────────────────────────────────────────────────────────┐
│                        USUARIO                               │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│                 REVERSE PROXY                               │
│                   (NGINX)                                   │
│              Puerto: 80/443                                 │
└─────┬─────────┬─────────┬─────────┬─────────────────────────┘
      │         │         │         │
      ▼         ▼         ▼         ▼
┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────────────┐
│ FRONTEND│ │  AUTH   │ │  BLOG   │ │     EMAIL       │
│ (React) │ │SERVICE  │ │SERVICE  │ │    SERVICE      │
│Port:3000│ │Port:8001│ │Port:8002│ │   Port:8003     │
└─────────┘ └─────┬───┘ └─────┬───┘ └─────────┬───────┘
                  │           │               │
                  └─────┬─────┴─────┬─────────┘
                        │           │
              ┌─────────▼───┐ ┌─────▼─────┐
              │ PostgreSQL  │ │   Redis   │
              │ Puerto:5432 │ │Puerto:6379│
              └─────────────┘ └───────────┘
```

### 🔄 Flujo de Comunicación
1. **Usuario** → **Reverse Proxy** (Punto de entrada único)
2. **Reverse Proxy** → **Servicios** (Enrutamiento inteligente)
3. **Servicios** ↔ **Base de Datos** (Persistencia de datos)
4. **Servicios** ↔ **Redis** (Cache y sesiones)
5. **Servicios** ↔ **Otros Servicios** (Comunicación inter-servicios)

## 🧩 Servicios Implementados

### 🔐 Auth Service (Puerto 8001)
**Propósito**: Gestión centralizada de autenticación y autorización
- **Funcionalidades**:
  - Registro y login de usuarios
  - Generación y validación de tokens JWT
  - Gestión de perfiles de usuario
  - Middleware de autenticación para otros servicios
- **Tecnologías**: Django, Django REST Framework, JWT
- **Base de Datos**: PostgreSQL (tabla de usuarios)
- **Cache**: Redis (tokens y sesiones)

### 📝 Blog Service (Puerto 8002)
**Propósito**: Gestión completa del contenido del blog
- **Funcionalidades**:
  - CRUD de publicaciones (posts)
  - Gestión de autores y perfiles
  - Sistema de categorías y etiquetas
  - Comentarios y interacciones
  - Búsqueda y filtrado de contenido
- **Tecnologías**: Django, Django REST Framework
- **Base de Datos**: PostgreSQL (posts, categorías, comentarios)
- **Integración**: Auth Service (validación de usuarios)

### 📧 Email Service (Puerto 8003)
**Propósito**: Gestión de notificaciones y comunicaciones por email
- **Funcionalidades**:
  - Envío de emails transaccionales
  - Plantillas de correo dinámicas
  - Notificaciones de nuevos posts
  - Confirmaciones de registro
  - Sistema de suscripciones
- **Tecnologías**: Django, SMTP, Celery (opcional)
- **Integración**: Blog Service (notificaciones), Auth Service (usuarios)

### 🌐 Frontend (Puerto 3000)
**Propósito**: Interfaz de usuario web
- **Funcionalidades**:
  - SPA (Single Page Application) con React
  - Autenticación de usuarios
  - Gestión de contenido del blog
  - Dashboard administrativo
  - Interfaz responsive y moderna
- **Tecnologías**: React, React Router, Axios, Material-UI/Bootstrap
- **Comunicación**: API REST a través del Reverse Proxy

### 🔄 Reverse Proxy
**Propósito**: Gateway y balanceador de carga
- **Funcionalidades**:
  - Enrutamiento de peticiones HTTP/HTTPS
  - Terminación SSL/TLS
  - Balanceo de carga
  - Compresión y cache de respuestas
  - Páginas de error personalizadas
- **Tecnologías**: NGINX
- **Configuración**: Enrutamiento por path (`/auth/*`, `/blog/*`, `/email/*`)

## 🗄️ Servicios de Infraestructura

### 🐘 PostgreSQL (Puerto 5432)
- **Base de datos principal** para todos los servicios
- **Configuración**:
  - Usuario: `devuser`
  - Contraseña: `devpass`
  - Base de datos: `main_db`
- **Persistencia**: Volumen Docker `pgdata`

### 🔴 Redis (Puerto 6379)
- **Cache en memoria** y almacén de sesiones
- **Usos**:
  - Cache de consultas frecuentes
  - Almacenamiento de tokens JWT
  - Sesiones de usuario
  - Cola de tareas (opcional con Celery)

## 🚀 Instalación y Configuración

### Prerequisitos
- **Docker Desktop** instalado y funcionando
- **Docker Compose v2** disponible
- **Git** para clonar el repositorio
- **4GB RAM** mínimo recomendado

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd Microservicios/microservices-lab
   ```

2. **Configurar variables de entorno**
   ```bash
   cp ../.env.example ../.env
   # Editar .env con tus configuraciones específicas
   ```

3. **Construir y ejecutar los servicios**
   ```bash
   # Iniciar servicios base (PostgreSQL y Redis)
   docker compose up -d postgres redis
   
   # Verificar que los servicios base están funcionando
   docker compose ps
   
   # Iniciar todos los servicios
   docker compose up -d
   ```

4. **Verificar el estado de los servicios**
   ```bash
   docker compose ps
   docker compose logs -f
   ```

### Accesos y URLs

| Servicio | URL Local | Descripción |
|----------|-----------|-------------|
| Frontend | http://localhost:3000 | Interfaz principal |
| Auth API | http://localhost:8001 | API de autenticación |
| Blog API | http://localhost:8002 | API del blog |
| Email API | http://localhost:8003 | API de emails |
| PostgreSQL | localhost:5432 | Base de datos |
| Redis | localhost:6379 | Cache y sesiones |

### Credenciales por Defecto
- **PostgreSQL**: 
  - Host: `localhost:5432`
  - Usuario: `devuser`
  - Contraseña: `devpass`
  - Base de datos: `main_db`
- **Redis**: 
  - Host: `localhost:6379`
  - Sin contraseña por defecto

## 🛠️ Comandos Útiles

### Docker Compose
```bash
# Iniciar todos los servicios
docker compose up -d

# Ver logs de todos los servicios
docker compose logs -f

# Ver logs de un servicio específico
docker compose logs -f auth-service

# Parar todos los servicios
docker compose down

# Parar y eliminar volúmenes
docker compose down -v

# Reconstruir imágenes
docker compose up --build

# Ver estado de los servicios
docker compose ps
```

### Desarrollo
```bash
# Acceder al contenedor de un servicio
docker compose exec auth-service bash

# Ejecutar migraciones de Django
docker compose exec auth-service python manage.py migrate

# Crear superusuario
docker compose exec auth-service python manage.py createsuperuser

# Ver logs en tiempo real
docker compose logs -f --tail=100
```

## 📋 Lista de Tareas del Proyecto

### ✅ Tareas Completadas
- [x] Configuración inicial de Docker Compose
- [x] Implementación de servicios base (PostgreSQL, Redis)
- [x] Estructura básica de microservicios
- [x] Documentación de arquitectura
- [x] README detallado del blog-service
- [x] Configuración de variables de entorno

### 🔄 Tareas en Progreso
- [ ] Implementación completa del Auth Service
  - [ ] Modelos de usuario Django
  - [ ] Endpoints de registro/login
  - [ ] Generación de tokens JWT
  - [ ] Middleware de autenticación
- [ ] Desarrollo del Blog Service
  - [ ] Modelos de Post, Author, Category
  - [ ] API REST completa (CRUD)
  - [ ] Sistema de comentarios
  - [ ] Búsqueda y filtros
- [ ] Configuración del Email Service
  - [ ] Integración SMTP
  - [ ] Plantillas de email
  - [ ] Sistema de notificaciones
- [ ] Desarrollo del Frontend React
  - [ ] Configuración inicial de React
  - [ ] Componentes de autenticación
  - [ ] Interfaz del blog
  - [ ] Dashboard administrativo

### 📅 Tareas Pendientes
- [ ] Configuración del Reverse Proxy (NGINX)
  - [ ] Configuración de enrutamiento
  - [ ] Certificados SSL para desarrollo
  - [ ] Páginas de error personalizadas
- [ ] Testing y Calidad
  - [ ] Tests unitarios para cada servicio
  - [ ] Tests de integración
  - [ ] Configuración de CI/CD
- [ ] Monitoreo y Observabilidad
  - [ ] Logging centralizado
  - [ ] Métricas de rendimiento
  - [ ] Health checks
- [ ] Seguridad
  - [ ] Configuración de CORS
  - [ ] Rate limiting
  - [ ] Validación de entrada
- [ ] Documentación
  - [ ] API documentation (Swagger/OpenAPI)
  - [ ] Guías de desarrollo
  - [ ] Diagramas de secuencia

### 🚀 Mejoras Futuras
- [ ] Implementación de Kubernetes
- [ ] Microservicio de notificaciones en tiempo real
- [ ] Sistema de métricas con Prometheus/Grafana
- [ ] Implementación de Event Sourcing
- [ ] API Gateway con autenticación centralizada
- [ ] Implementación de Circuit Breaker pattern
- [ ] Cache distribuido con Redis Cluster

## 🧪 Testing

### Ejecutar Tests
```bash
# Tests de un servicio específico
docker compose exec auth-service python manage.py test

# Tests con coverage
docker compose exec auth-service coverage run --source='.' manage.py test
docker compose exec auth-service coverage report
```

### Tests de Integración
```bash
# Verificar conectividad entre servicios
docker compose exec auth-service python test_connection.py
```

## 📚 Recursos y Referencias

### Documentación Técnica
- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [React Documentation](https://reactjs.org/docs/)
- [Docker Compose Reference](https://docs.docker.com/compose/)

### Patrones de Microservicios
- [Microservices Patterns](https://microservices.io/patterns/)
- [12-Factor App](https://12factor.net/)
- [API Design Guidelines](https://restfulapi.net/)

## 🤝 Contribución

### Cómo Contribuir
1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

### Estándares de Código
- Seguir PEP 8 para código Python
- Usar ESLint para código JavaScript/React
- Documentar todas las funciones y clases
- Escribir tests para nuevas funcionalidades

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Soporte

Para reportar bugs, solicitar funcionalidades o hacer preguntas:
- Crear un issue en el repositorio
- Contactar al equipo de desarrollo
- Revisar la documentación existente

---

**Nota**: Este es un proyecto educativo diseñado para demostrar conceptos de microservicios. Para uso en producción, considera implementar medidas adicionales de seguridad, monitoreo y escalabilidad.
