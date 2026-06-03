# 7.3 Crear el Servicio de Predicción

## Estructura del proyecto

```text
servicio-churn/
├── main.py              ← API con FastAPI
├── modelo_churn.joblib  ← Modelo serializado
├── vectorizer.joblib    ← DictVectorizer serializado
├── pyproject.toml       ← Dependencias
└── test_api.py          ← Script de pruebas
```

## El código completo del servicio

```python
# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Cargar modelo y vectorizer al iniciar
modelo = joblib.load('modelo_churn.joblib')
dv = joblib.load('vectorizer.joblib')

app = FastAPI(title="Servicio de Predicción de Churn")


class ClienteInput(BaseModel):
    contract: str
    tenure: int
    monthly_charges: float
    total_charges: float
    internet_service: str
    online_security: str
    tech_support: str
    payment_method: str


class PrediccionOutput(BaseModel):
    churn_probability: float
    churn: bool


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predecir", response_model=PrediccionOutput)
def predecir(cliente: ClienteInput):
    # Convertir a dict para el vectorizer
    cliente_dict = cliente.model_dump()

    # Transformar features
    X = dv.transform([cliente_dict])

    # Predecir probabilidad
    prob = modelo.predict_proba(X)[0, 1]

    return PrediccionOutput(
        churn_probability=round(float(prob), 4),
        churn=prob >= 0.5
    )
```

## Ejecutar el servicio

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Probar el servicio

```python
# test_api.py
import httpx

url = "http://localhost:8000/predecir"

cliente = {
    "contract": "Month-to-month",
    "tenure": 3,
    "monthly_charges": 75.0,
    "total_charges": 225.0,
    "internet_service": "Fiber optic",
    "online_security": "No",
    "tech_support": "No",
    "payment_method": "Electronic check"
}

response = httpx.post(url, json=cliente)
print(f"Status: {response.status_code}")
print(f"Resultado: {response.json()}")
```

## Documentación automática

Con el servicio corriendo, visita:

- `http://localhost:8000/docs` → Swagger UI (interactivo)
- `http://localhost:8000/redoc` → ReDoc (documentación limpia)

## Manejo de errores

FastAPI maneja errores automáticamente:

- Datos faltantes → Error 422 con detalle
- Tipo incorrecto → Error 422 con detalle
- Error interno → Error 500

Para errores personalizados:

```python
from fastapi import HTTPException

@app.post("/predecir")
def predecir(cliente: ClienteInput):
    if cliente.tenure < 0:
        raise HTTPException(status_code=400, detail="tenure no puede ser negativo")
    # ... resto de la lógica
```

---

**Anterior**: [FastAPI Intro](02-fastapi-intro.md) | **Siguiente**: [Docker](04-docker.md)
