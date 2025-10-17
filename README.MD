# Laboratorio de Microservicios (Django + React)

## Arquitectura inicial
- auth-service/      → Autenticación y tokens JWT
- blog-service/      → Publicaciones, autores y categorías
- email-service/     → Notificaciones y formularios
- frontend/          → Interfaz React
- reverse-proxy/     → Balanceo / Gateway local

Servicios base:
- PostgreSQL (5432)
- Redis (6379)

## Arranque con Docker Compose
- Requisitos: tener instalado `Docker Desktop` y `docker compose v2`.
- Arrancar servicios base:
  - `cd Microservicios/microservices-lab`
  - `docker compose up -d`
  - `docker compose ps`
- Parar y eliminar contenedores:
  - `docker compose down`

### Accesos
- PostgreSQL: `localhost:5432` (usuario `devuser`, contraseña `devpass`, base `main_db`).
- Redis: `localhost:6379`.

### Persistencia
- Los datos de PostgreSQL se guardan en el volumen `pgdata`.
