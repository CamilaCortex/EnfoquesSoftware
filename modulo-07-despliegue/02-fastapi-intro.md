# 7.2 Introducción a FastAPI

## ¿Qué es FastAPI?

FastAPI es un framework moderno para crear APIs REST en Python. Es rápido, fácil de usar y genera documentación automática.

## ¿Por qué FastAPI?

- **Rápido**: uno de los frameworks más rápidos de Python
- **Validación automática**: valida los datos de entrada con Pydantic
- **Documentación auto-generada**: Swagger UI disponible en `/docs`
- **Tipado**: usa type hints de Python, por lo que el IDE te ayuda

## Tu primera API

Crea un archivo `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "¡API funcionando!"}

@app.get("/saludo/{nombre}")
def saludo(nombre: str):
    return {"mensaje": f"Hola, {nombre}!"}
```

## Ejecutar

```bash
uvicorn main:app --reload
```

- `main`: nombre del archivo (main.py)
- `app`: nombre de la variable FastAPI
- `--reload`: reinicia automáticamente al guardar cambios

Abre `http://localhost:8000/docs` para ver la documentación interactiva.

## Recibir datos con POST

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ClienteInput(BaseModel):
    contract: str
    tenure: int
    monthly_charges: float

@app.post("/predecir")
def predecir(cliente: ClienteInput):
    # Aquí irá la lógica de predicción
    return {
        "churn_probability": 0.75,
        "churn": True
    }
```

## Pydantic: validación de datos

Pydantic valida automáticamente que los datos tengan el tipo correcto:

```python
# Si envías tenure como string, FastAPI devuelve un error 422 automáticamente
# No necesitas escribir validación manual
```

## Probar la API

Con `httpx` o `requests`:

```python
import httpx

response = httpx.post("http://localhost:8000/predecir", json={
    "contract": "Month-to-month",
    "tenure": 3,
    "monthly_charges": 75.0
})
print(response.json())
```

O usando la interfaz de Swagger en `/docs`.

---

**Anterior**: [Serialización](01-serializacion.md) | **Siguiente**: [Servicio de Predicción](03-servicio-prediccion.md)
