# 🧩 Frontend — Microservices Lab

## 📘 Descripción General
Este módulo corresponde al **Frontend** del proyecto **Microservices Lab**, una arquitectura basada en **microservicios** desplegados mediante **Docker Compose**.  
El frontend funciona como la interfaz gráfica del sistema, centralizando la interacción del usuario con los diferentes servicios backend: autenticación, blog, correo y otros.

---

## 🏗️ Rol dentro de la Arquitectura
El frontend actúa como **puerta de entrada visual** del ecosistema. Se comunica con los microservicios a través del **Reverse Proxy (NGINX)**, que enruta las peticiones a cada servicio interno.

### 🔄 Flujo de Comunicación
```
[Usuario] ⇄ [Frontend React] ⇄ [Reverse Proxy] ⇄ [Microservicios]
├── Auth Service
├── Blog Service
└── Email Service
```

- **Reverse Proxy**: Encargado de redirigir las solicitudes a los servicios correctos.
- **Frontend**: Consume los endpoints expuestos a través del proxy (por ejemplo: `/api/auth`, `/api/blog`).
- **Microservicios**: Procesan la lógica de negocio independiente (autenticación, blog, notificaciones, etc.).

---

## ⚙️ Estructura Interna
La carpeta `frontend/` contendrá el código fuente de la aplicación React y su configuración de entorno:
```
frontend/
├── src/
│ ├── api/ # Comunicación con servicios (auth, blog, email)
│ ├── assets/ # Imágenes, íconos y recursos estáticos
│ ├── components/ # Componentes reutilizables (botones, formularios, etc.)
│ ├── layouts/ # Plantillas base (Dashboard, Login, etc.)
│ ├── modules/ # Módulos funcionales
│ │ ├── auth/ # Pantallas y lógica de autenticación
│ │ ├── blog/ # Publicaciones y manejo de contenidos
│ │ └── email/ # Envío y gestión de correos
│ ├── router/ # Configuración de rutas con React Router
│ ├── store/ # Estado global (Zustand o Redux Toolkit)
│ └── main.jsx # Punto de entrada de la app
│
├── public/ # Archivos públicos (index.html, favicon)
├── Dockerfile # Imagen Docker del frontend
├── .env.example # Variables de entorno ejemplo
├── package.json # Dependencias del proyecto
└── README.md # Este archivo
```
---

## 🧱 Tecnologías Clave
| Tipo | Herramienta | Propósito |
|------|--------------|-----------|
| Framework | React + Vite | Interfaz moderna y rápida |
| Estilos | TailwindCSS | Estilizado dinámico |
| Estado | Zustand / Redux Toolkit | Manejo global de datos |
| Rutas | React Router v6 | Navegación SPA |
| UI | shadcn/ui + lucide-react | Componentes e íconos |
| HTTP | Axios | Comunicación con API Gateway |
| Gráficos | Recharts | Visualización de métricas |

---

## 🌐 Comunicación con el Backend
El frontend no se conecta directamente con los microservicios, sino mediante el **Reverse Proxy**, normalmente configurado con NGINX dentro de Docker.

### Ejemplo de rutas esperadas:
| Servicio | Ruta pública | Internamente redirige a |
|-----------|---------------|--------------------------|
| Auth | `/api/auth` | `http://auth-service:4000` |
| Blog | `/api/blog` | `http://blog-service:4001` |
| Email | `/api/email` | `http://email-service:4002` |

---

## 🧠 Variables de Entorno
Archivo `.env` o `.env.example`:
```
VITE_API_URL=http://localhost/api

VITE_ENV=development
```

> En Docker Compose, esta variable debe apuntar al **proxy** que agrupa los microservicios.

---

## 🐳 Integración con Docker Compose
El contenedor del frontend será parte del `docker-compose.yml` ubicado en la raíz (`/microservices-lab/reverse-proxy/docker-compose.yml`).

Ejemplo de servicio dentro del compose:
```yaml
frontend:
  build: ./frontend
  container_name: frontend
  ports:
    - "5173:5173"
  environment:
    - VITE_API_URL=http://reverse-proxy/api
  depends_on:
    - reverse-proxy
```
--- 

## 🚀 Scripts Principales
```bash
# Instalar dependencias
npm install

# Ejecutar en desarrollo
npm run dev

# Compilar para producción
npm run build

# Previsualizar build
npm run preview
```
---

## 📦 Objetivo del Módulo

* Servir como interfaz gráfica del ecosistema de microservicios.

* Facilitar autenticación, visualización y gestión de datos del blog.

* Permitir comunicación segura con los servicios de backend a través del proxy.

* Escalable y adaptable para futuras integraciones.