# Reverse Proxy

Este proyecto sigue una arquitectura de microservicios orquestada con Docker Compose. La carpeta `reverse-proxy` concentra todo lo necesario para exponer un único punto de entrada HTTP/HTTPS hacia los servicios internos (auth, blog, email, frontend), ocupándose del enrutamiento, seguridad y observabilidad.

## Rol en la arquitectura
- Termina conexiones `HTTP/HTTPS` y gestiona certificados TLS.
- Encamina rutas públicas hacia contenedores internos (`/auth`, `/blog`, `/email` y `/`).
- Aplica cabeceras de seguridad, CORS, rate limiting y compresión.
- Centraliza logs de acceso/errores y páginas de error personalizadas.

## Contenido de la carpeta (previsto)
- `nginx/` (o `traefik/`): configuración del proxy por proveedor.
  - `nginx.conf`: configuración base.
  - `conf.d/`: bloques por servicio y reglas de enrutado.
- `certs/`: certificados y claves para desarrollo/producción.
- `errors/`: páginas HTML de error (404, 50x) para respuestas coherentes.
- `README.md`: este documento.
- `Dockerfile` (opcional): personalización de la imagen del proxy si se requiere.

> Por defecto se propone **Nginx** por su simplicidad; puedes sustituir por **Traefik** si deseas autogestión de certificados con Let’s Encrypt.

## Enrutado esperado
- `/auth/*` → `auth-service` (ej. puerto `8080`).
- `/blog/*` → `blog-service` (ej. puerto `8080`).
- `/email/*` → `email-service` (ej. puerto `8080`).
- `/` → `frontend` (SPA en puerto `3000`).

### Ejemplo de `conf.d/default.conf` (Nginx)
```nginx
server {
  listen 80;
  server_name _;

  location /auth/  { proxy_pass http://auth-service:8080/; }
  location /blog/  { proxy_pass http://blog-service:8080/; }
  location /email/ { proxy_pass http://email-service:8080/; }
  location /       { proxy_pass http://frontend:3000; }
}
```
Para TLS, añade `listen 443 ssl;` y referencia los archivos en `certs/`.

## Integración con Docker Compose
Ejemplo de servicio en el `docker-compose.yml` raíz:
```yaml
reverse-proxy:
  image: nginx:alpine
  container_name: reverse-proxy
  volumes:
    - ./microservices-lab/reverse-proxy/nginx/nginx.conf:/etc/nginx/nginx.conf:ro
    - ./microservices-lab/reverse-proxy/nginx/conf.d:/etc/nginx/conf.d:ro
    - ./microservices-lab/reverse-proxy/certs:/etc/nginx/certs:ro
    - ./microservices-lab/reverse-proxy/errors:/usr/share/nginx/html/errors:ro
  ports:
    - "80:80"
    - "443:443"
  depends_on:
    - auth-service
    - blog-service
    - email-service
    - frontend
  networks:
    - microservices-net
```
> Adapta el nombre de la red (`microservices-net`) al que uses en tu Compose.

## Variables de entorno (sugeridas)
- `DOMAIN`: dominio público (ej. `app.local`/`tudominio.com`).
- `ENABLE_HTTPS`: `true|false` para activar TLS.
- `LETSENCRYPT_EMAIL`: correo para certificados automáticos (si usas Traefik).

## Flujo de trabajo
- Desarrollo: arranca con `docker compose up -d reverse-proxy` y valida con `docker compose logs reverse-proxy`.
- Producción: monta certificados válidos en `certs/`, habilita `443` y endurece cabeceras de seguridad.

## Añadir un nuevo servicio
1. Crea un archivo en `nginx/conf.d/` con la nueva ruta.
2. Apunta `proxy_pass` al nombre del contenedor y puerto interno.
3. Reinicia o recarga el proxy: `docker compose restart reverse-proxy`.

## Seguridad y observabilidad
- Habilita HSTS, `X-Frame-Options`, `X-Content-Type-Options` y `Referrer-Policy`.
- Activa `gzip`/`brotli` para mejorar rendimiento.
- Centraliza logs y monitoriza códigos de respuesta para detectar problemas.

Con esto, `reverse-proxy` ofrece una capa uniforme de acceso y seguridad para todos los microservicios, manteniendo una interfaz pública única y coherente.