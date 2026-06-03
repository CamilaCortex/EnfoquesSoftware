# Curso de Machine Learning para Ingeniería de Software

Aprende Machine Learning de forma práctica: desde los fundamentos matemáticos hasta orquestar y desplegar modelos en producción con MLflow, Prefect, FastAPI y Docker.

---

## Información del Curso

- **Nivel**: Básico a intermedio
- **Duración**: 8 módulos
- **Requisitos**: Conocimientos básicos de Python y línea de comandos
- **Herramientas**: Python 3.13, uv, scikit-learn, XGBoost, MLflow, Prefect, FastAPI, Docker

---

## Configuración del Entorno (paso a paso)

### 1. Instalar `uv`

`uv` es un gestor de paquetes y entornos virtuales ultrarrápido para Python. Con él podemos instalar versiones de Python, crear entornos virtuales e instalar dependencias, todo desde una sola herramienta.

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Cierra y abre tu terminal después de instalar para que el comando `uv` esté disponible.

### 2. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd machine-learning-zoomcamp
```

### 3. Instalar Python 3.13 con `uv`

No necesitas instalar Python por tu cuenta. `uv` puede descargar y gestionar versiones de Python directamente:

```bash
uv python install 3.13
```

Puedes verificar que se instaló correctamente:

```bash
uv python list
```

### 4. Crear el entorno virtual e instalar dependencias

```bash
uv sync --python 3.13
```

Esto hace tres cosas a la vez:

- Crea un entorno virtual (`.venv/`) con Python 3.13
- Lee las dependencias del `pyproject.toml`
- Instala todos los paquetes necesarios

### 5. Verificar la instalación

```bash
uv run python --version
# Debería mostrar: Python 3.13.x
```

### 6. Iniciar Jupyter

```bash
uv run jupyter notebook
```

> **Nota:** Usamos `uv run` para ejecutar comandos dentro del entorno virtual sin necesidad de activarlo manualmente. Si prefieres activarlo:
>
> ```bash
> # macOS / Linux
> source .venv/bin/activate
>
> # Windows
> .venv\Scripts\activate
> ```

---

## Contenido del Curso

| Módulo | Carpeta | Descripción |
|--------|---------|-------------|
| 00 | [Gestión de Entornos](modulo-00-gestion-entornos-virtuales/) | uv, entornos virtuales, gestión de dependencias |
| 01 | [Introducción al ML](modulo-01-introduccion/) | Qué es ML, tipos de aprendizaje, CRISP-DM |
| 02 | [Python para ML](modulo-02-python-para-ml/) | NumPy, Pandas, análisis exploratorio, álgebra lineal |
| 03 | [Regresión](modulo-03-regresion/) | Regresión lineal, RMSE, regularización, validación |
| 04 | [Clasificación](modulo-04-clasificacion/) | Regresión logística, importancia de features, encoding |
| 05 | [Evaluación de Modelos](modulo-05-evaluacion/) | Precision, recall, ROC-AUC, validación cruzada |
| 06 | [Experiment Tracking](modulo-06-tracking/) | MLflow: tracking de experimentos, model registry |
| 07 | [Orquestación](modulo-07-orchestration/) | Prefect: pipelines, flows, tasks, scheduling |
| 08 | [Despliegue](modulo-08-despliegue/) | Serialización, FastAPI, Docker, batch deploy, AWS |
| — | [Proyecto Integrador](modulo-08-proyecto-integrador/) | Proyecto end-to-end: datos → modelo → API → Docker |

---

## Módulo 08 — Despliegue en detalle

El módulo de despliegue incluye cuatro proyectos prácticos en `modulo-08-despliegue/deploy/`:

| Proyecto | Descripción |
|----------|-------------|
| [`intro-dockers/`](modulo-08-despliegue/deploy/intro-dockers/) | App FastAPI con gatitos — introducción a Docker y HTTP |
| [`web-service/`](modulo-08-despliegue/deploy/web-service/) | API REST de predicción de duración de viajes NYC Taxi |
| [`batch-deploy/`](modulo-08-despliegue/deploy/batch-deploy/) | Pipeline batch con Prefect: predicciones programadas cada hora |
| [`web-service-aws/`](modulo-08-despliegue/deploy/web-service-aws/) | Despliegue del servicio en AWS EC2 |

---

## Estructura del Proyecto

Cada módulo contiene:

- **README.md** — Objetivos y mapa del módulo
- **Lecciones** (.md) — Explicaciones teóricas con ejemplos de código
- **notebook.ipynb** — Práctica guiada en Jupyter
- **ejercicios.md** — Ejercicios para reforzar lo aprendido

---

## Proyecto Integrador

El curso culmina con un proyecto donde aplicarás todo lo aprendido:

1. Elegir un problema y dataset
2. Análisis exploratorio y preparación de datos
3. Entrenar y evaluar modelos (con MLflow)
4. Orquestar el pipeline (con Prefect)
5. Crear una API con FastAPI
6. Contenerizar con Docker

---

## Tecnologías

| Herramienta | Uso |
|-------------|-----|
| **uv** | Gestión de entorno y dependencias |
| **NumPy / Pandas** | Manipulación de datos |
| **scikit-learn** | Modelos de ML |
| **XGBoost** | Gradient boosting |
| **Matplotlib / Seaborn / Plotly** | Visualización |
| **MLflow** | Experiment tracking y model registry |
| **Prefect** | Orquestación de pipelines |
| **Optuna** | Optimización de hiperparámetros |
| **FastAPI** | API REST para servir modelos |
| **Docker** | Contenerización y despliegue |
| **AWS EC2** | Despliegue en nube |
