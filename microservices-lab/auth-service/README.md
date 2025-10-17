# Auth Service

Este directorio corresponde al servicio de autenticación del laboratorio de microservicios.
Su función es gestionar el acceso de usuarios (registro, inicio de sesión), emitir y
verificar tokens JWT y centralizar la lógica de autenticación.

## Contenido actual
- `test_connection.py`: script de verificación de conexión a PostgreSQL y Redis usando
  variables de entorno. Útil para validar que la base de datos y el caché están accesibles
  desde la red de Docker Compose antes de implementar la lógica del servicio.
- `README.md`: documentación del módulo.

## Variables de entorno requeridas por el script
- `POSTGRES_HOST` (por defecto `localhost` o `postgres` dentro del compose)
- `POSTGRES_PORT` (por defecto `5432`)
- `POSTGRES_USER` (requerida)
- `POSTGRES_PASSWORD` (requerida)
- `POSTGRES_DB` (requerida)
- `REDIS_HOST` (por defecto `localhost` o `redis` dentro del compose)
- `REDIS_PORT` (por defecto `6379`)
- `REDIS_PASSWORD` (opcional)

Puedes tomar como referencia el archivo `Microservicios/.env.example` para los valores.

## Cómo ejecutar la prueba de conexión

### Opción A: desde tu host (Windows)
1. Instala dependencias:
   - `pip install psycopg2-binary redis`
2. Exporta variables de entorno (PowerShell):
   - `$env:POSTGRES_USER='devuser'`
   - `$env:POSTGRES_PASSWORD='devpass'`
   - `$env:POSTGRES_DB='main_db'`
   - `$env:POSTGRES_HOST='localhost'`
   - `$env:REDIS_HOST='localhost'`
3. Ejecuta:
   - `python auth-service/test_connection.py`

### Opción B: dentro de un contenedor (misma red que Postgres/Redis)
1. Crear el contenedor auxiliar una sola vez:
   - `docker run -d --name auth_exec --network microservices-lab_default --mount type=bind,source="c:\\Users\\Christian\\Desktop\\xammp\\htdocs\\PRACTICA_DOCKER\\Microservicios\\microservices-lab",target=/workspace -w /workspace python:3.12-slim sleep infinity`
2. Ejecutar el script con variables apuntando a servicios del compose:
   - `docker exec -it auth_exec sh -lc "pip install --no-cache-dir psycopg2-binary redis && POSTGRES_HOST=postgres POSTGRES_PORT=5432 POSTGRES_USER=devuser POSTGRES_PASSWORD=devpass POSTGRES_DB=main_db REDIS_HOST=redis REDIS_PORT=6379 python auth-service/test_connection.py"`
3. Limpiar (opcional):
   - `docker rm -f auth_exec`

## Próximos pasos (implementación del servicio)
- Crear la aplicación del servicio (p.ej., Django/FastAPI/Flask) con endpoints:
  - `POST /auth/register`, `POST /auth/login`, `POST /auth/refresh`, `GET /auth/me`.
- Añadir `Dockerfile` para `auth-service` y configurarlo en `docker-compose.yml` con `depends_on` de `postgres` y `redis`.
- Gestionar migraciones y modelos (usuarios, roles, tokens/blacklist si aplica).
- Integración con `reverse-proxy` para exponer el servicio.
