# ⚡ Laboratorio Virtual de Electromagnetismo

Aplicación web educativa desarrollada como complemento didáctico para la asignatura **Física II** de la **Universidad Tecnológica Nacional - Facultad Regional Resistencia (UTN FRRe)**.

El proyecto permite explorar los principales conceptos del **Campo de Inducción Magnética** mediante simulaciones interactivas, visualizaciones dinámicas y laboratorios virtuales diseñados para facilitar el aprendizaje de los estudiantes.

---

## 🌐 Demo

> (https://simulador-de-electromagnetismo.onrender.com/)


> **Nota:** El proyecto se encuentra en desarrollo activo. Nuevas funcionalidades se incorporan de manera incremental en cada versión.
---
## ✨ Características principales

- 📚 Explicaciones teóricas paso a paso.
- 🧲 Simulaciones interactivas de Electromagnetismo.
- 📈 Gráficos dinámicos con Plotly.
- 🧪 Laboratorios virtuales.
- 📝 Ejercicios resueltos.
- 🐳 Ejecución mediante Docker.
- ☁️ Despliegue automático en Render.
- 🗄️ Persistencia con PostgreSQL.
- 👥 Contador global de visitas.

---

## 🛠️ Tecnologías

| Tecnología | Uso |
|------------|-----|
| Python 3 | Lenguaje principal |
| Flask | Framework Web |
| Plotly | Gráficos interactivos |
| Bootstrap 5 | Interfaz de usuario |
| PostgreSQL | Persistencia de datos |
| psycopg | Conector PostgreSQL |
| Docker | Contenedorización |
| Render | Despliegue en producción |
| Gunicorn | Servidor WSGI |

---

## 🚧 Estado del Proyecto

Actualmente el Laboratorio Virtual se encuentra en desarrollo activo.

### ✅ Implementado

- Campo magnético de un conductor rectilíneo infinito.
- Campo magnético total de dos conductores paralelos.
- Laboratorio virtual del Tema 2.
- Simulaciones interactivas.
- Ejercicios resueltos.
- Visualizaciones con Plotly.
- Persistencia con PostgreSQL.
- Contador global de visitas.
- Despliegue automático en Render.

### 🔄 En desarrollo

- Tema 3 — Campo Magnético de una Bobina Circular.
---
# 🚀 Instalación

## Requisitos

Antes de comenzar, asegúrese de tener instalado:

- Docker Desktop (Windows, macOS) o Docker Engine (Linux).
- Docker Compose.

No es necesario instalar Python ni PostgreSQL localmente.

---

## 1. Clonar el repositorio

```bash
git clone https://github.com/jhgakiyama/electromagnetismo-simulator.git

cd TU_REPOSITORIO
```

---

## 2. Construir la imagen

```bash
docker compose up --build
```

Este comando:

- Construye la imagen Docker.
- Instala todas las dependencias.
- Inicia la aplicación Flask.

---

## 3. Inicializar la base de datos

En otra terminal ejecutar:

```bash
docker compose exec web python init_db.py
```

Este comando:

- Se conecta a PostgreSQL.
- Crea automáticamente las tablas necesarias.
- No modifica tablas existentes.

---

## 4. Acceder a la aplicación

Abrir el navegador en:

```text
http://localhost:5000
```

---

## Variables de entorno

Durante el desarrollo se utiliza un archivo `.env`.

Ejemplo:

```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=...

DATABASE_URL=...
```

> El archivo `.env` no debe incluirse en el repositorio.

En producción, estas variables son administradas mediante Render.

---

## Base de datos

El proyecto utiliza PostgreSQL.

En desarrollo puede utilizarse la **External Database URL** proporcionada por Render.

En producción la aplicación utiliza automáticamente la **Internal Database URL**, configurada como variable de entorno.
## 🚀 Ejecución del Proyecto

### Construir la imagen Docker

```bash
docker-compose build
```

### Iniciar la aplicación

```bash
docker-compose up
```

### Acceder a la aplicación

```text
http://localhost:5000
```

---

# 🏗️ Arquitectura del proyecto

El proyecto sigue una arquitectura modular basada en la separación de responsabilidades.

Cada componente del sistema posee una única responsabilidad, facilitando el mantenimiento, la reutilización del código y la incorporación de nuevas funcionalidades.

```
                 Navegador
                      │
                      ▼
                 Flask Routes
                      │
                      ▼
                 Services
              ┌───────────────┐
              │               │
              ▼               ▼
         Physics         Database
              │               │
              ▼               ▼
           Plotly        PostgreSQL
                      ▲
                      │
             Context Processor
                      │
                      ▼
                Templates (Jinja2)
```

---

## Flujo de una petición

1. El navegador realiza una solicitud HTTP.
2. Flask recibe la petición mediante una Route.
3. La Route delega el trabajo al Service correspondiente.
4. El Service puede:
   - realizar cálculos físicos;
   - acceder a la base de datos;
   - generar información para la interfaz.
5. Finalmente se renderiza una plantilla HTML utilizando Jinja2.

---

## Principios utilizados

- Una única responsabilidad por módulo.
- Separación entre presentación, lógica y persistencia.
- Reutilización de componentes.
- Variables globales mediante Context Processor.
- Persistencia desacoplada mediante un módulo `database`.

---
## Responsabilidad de cada módulo

| Módulo | Responsabilidad |
|--------|-----------------|
| `routes` | Gestionar las peticiones HTTP |
| `services` | Contener la lógica de negocio |
| `physics` | Resolver los modelos físicos |
| `plots` | Generar gráficos interactivos |
| `database` | Gestionar la conexión con PostgreSQL |
| `templates` | Renderizar la interfaz HTML |
| `static` | Recursos estáticos (CSS, JS e imágenes) |

---
# 📁 Estructura del Proyecto

La aplicación está organizada siguiendo una arquitectura modular basada en la separación de responsabilidades.

```text
electromagnetismo-laboratorio/

│
├── app/
│   │
│   ├── database/
│   │   ├── connection.py
│   │   └── schema.py
│   │
│   ├── physics/
│   │
│   ├── plots/
│   │
│   ├── routes/
│   │
│   ├── services/
│   │
│   ├── static/
│   │   ├── css/
│   │   ├── img/
│   │   └── js/
│   │
│   ├── templates/
│   │
│   ├── context_processors.py
│   ├── errors.py
│   └── __init__.py
│
├── docker-compose.yml
├── Dockerfile
├── init_db.py
├── requirements.txt
├── run.py
├── README.md
└── .env
```

---

## Descripción de los directorios

### 📂 app/routes

Contiene las rutas HTTP de la aplicación.

Cada módulo representa una sección funcional del laboratorio.

Ejemplos:

- Home
- Tema 1
- Tema 2
- Laboratorio
- Health Check

---

### 📂 app/services

Implementa la lógica de negocio.

Los Services coordinan el trabajo entre las rutas, los cálculos físicos y la base de datos.

---

### 📂 app/physics

Contiene los modelos matemáticos y físicos utilizados por las simulaciones.

Su responsabilidad es exclusivamente realizar cálculos.

No conoce Flask ni HTML.

---

### 📂 app/plots

Genera los gráficos interactivos utilizando Plotly.

Toda la lógica de visualización se encuentra desacoplada del resto del sistema.

---

### 📂 app/database

Gestiona la persistencia de datos.

Actualmente incluye:

- conexión con PostgreSQL;
- inicialización del esquema de la base de datos.

---

### 📂 app/templates

Plantillas HTML desarrolladas con Jinja2.

Definen toda la interfaz de usuario del laboratorio.

---

### 📂 app/static

Recursos estáticos utilizados por la aplicación.

Incluye:

- hojas de estilo;
- imágenes;
- JavaScript.

---

## Archivos principales

| Archivo | Descripción |
|----------|-------------|
| `run.py` | Punto de entrada de la aplicación Flask. |
| `init_db.py` | Inicializa la base de datos PostgreSQL. |
| `Dockerfile` | Define la imagen Docker del proyecto. |
| `docker-compose.yml` | Orquesta los servicios utilizados durante el desarrollo. |
| `requirements.txt` | Dependencias Python del proyecto. |
| `.env` | Variables de entorno para desarrollo local. |

---

## 🗺️ Roadmap

### Tema 1 - Campo Magnético de un Conductor Rectilíneo Infinito

* [✔️] Implementado

### Tema 2 - Campo Magnético Total de Dos Conductores Paralelos

* [✔️] Implementado

Incluye:

* Superposición de campos magnéticos
* Regla de la mano derecha
* Suma vectorial
* Laboratorio

### Tema 3 - Campo Magnético de una Bobina Circular

* [ ] Pendiente

Incluye:

* Campo magnético en el centro de una espira

---

# 👨‍💻 Autor

Proyecto desarrollado por **Japo** como parte del proceso de aprendizaje y aplicación práctica de conceptos de Ingeniería en Sistemas y Física II.

El desarrollo combina conocimientos de programación, visualización científica, arquitectura de software y tecnologías web modernas con el objetivo de crear una herramienta educativa accesible para estudiantes y docentes.

---

## 🎓 Institución

**Universidad Tecnológica Nacional**

**Facultad Regional Resistencia**

Asignatura: **Física II**

---

⭐ Si este proyecto resulta útil para estudiantes o docentes, se agradece cualquier sugerencia o propuesta de mejora.