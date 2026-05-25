# 1.6 Configuración del Entorno con uv

## ¿Qué es uv?

[uv](https://docs.astral.sh/uv/) es un gestor de paquetes y entornos virtuales para Python, extremadamente rápido. Reemplaza a pip, pipenv y virtualenv en un solo comando.

## Instalación de uv

### macOS / Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows (PowerShell)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verifica la instalación:

```bash
uv --version
```

## Configurar el entorno del curso

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd machine-learning-zoomcamp
```

### 2. Instalar Python 3.13 con `uv`

No necesitas instalar Python por tu cuenta. `uv` puede descargar y gestionar cualquier versión de Python directamente:

```bash
uv python install 3.13
```

Verifica que se instaló:

```bash
uv python list
```

> **💡 Tip:** Puedes instalar varias versiones de Python con `uv` y cambiar entre ellas según el proyecto. Por ejemplo: `uv python install 3.11` o `uv python install 3.12`.

### 3. Crear el entorno virtual e instalar dependencias

```bash
uv sync --python 3.13
```

Este comando hace tres cosas a la vez:

- Crea un entorno virtual (`.venv/`) con Python 3.13
- Instala todas las dependencias definidas en `pyproject.toml`
- Genera/actualiza el `uv.lock` con versiones exactas

### 4. Verificar la instalación

```bash
uv run python --version
# Debería mostrar: Python 3.13.x
```

### 5. Iniciar Jupyter

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

## Comandos útiles de uv

```bash
# Agregar un paquete nuevo
uv add nombre-paquete

# Agregar paquete de desarrollo
uv add --dev nombre-paquete

# Actualizar dependencias
uv sync --upgrade

# Ejecutar un script sin activar el venv
uv run python mi_script.py

# Ejecutar jupyter sin activar el venv
uv run jupyter notebook
```

## Estructura del proyecto

Después de `uv sync`, tu carpeta tendrá:

```text
machine-learning-zoomcamp/
├── .venv/              ← entorno virtual (no se sube a git)
├── pyproject.toml      ← definición de dependencias
├── uv.lock             ← versiones exactas (sí se sube a git)
├── modulo-01-introduccion/
├── modulo-02-python-para-ml/
└── ...
```

## Verificación

Ejecuta esto para confirmar que todo funciona:

```python
import numpy as np
import pandas as pd
import sklearn

print(f"NumPy: {np.__version__}")
print(f"Pandas: {pd.__version__}")
print(f"Scikit-learn: {sklearn.__version__}")
```

Si ves las versiones sin errores, tu entorno está listo.

---

**Anterior**: [Selección de Modelos](05-seleccion-modelos.md) | **Volver al módulo**: [README](README.md)
