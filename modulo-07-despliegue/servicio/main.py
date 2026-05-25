"""Servicio de predicción de churn con FastAPI."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib

# Cargar modelo y vectorizer al iniciar
try:
    modelo = joblib.load("modelo_churn.joblib")
    dv = joblib.load("vectorizer.joblib")
except FileNotFoundError:
    modelo = None
    dv = None

app = FastAPI(
    title="Servicio de Predicción de Churn",
    description="API para predecir la probabilidad de cancelación de clientes",
    version="1.0.0",
)


class ClienteInput(BaseModel):
    """Datos de entrada de un cliente."""

    contract: str
    tenure: int
    monthly_charges: float
    total_charges: float
    internet_service: str
    online_security: str
    tech_support: str
    payment_method: str


class PrediccionOutput(BaseModel):
    """Resultado de la predicción."""

    churn_probability: float
    churn: bool


@app.get("/health")
def health():
    """Verificar que el servicio está funcionando."""
    model_loaded = modelo is not None and dv is not None
    return {"status": "ok", "model_loaded": model_loaded}


@app.post("/predecir", response_model=PrediccionOutput)
def predecir(cliente: ClienteInput):
    """Predecir la probabilidad de churn para un cliente."""
    if modelo is None or dv is None:
        raise HTTPException(
            status_code=503,
            detail="Modelo no cargado. Asegúrate de que los archivos .joblib existen.",
        )

    cliente_dict = cliente.model_dump()
    X = dv.transform([cliente_dict])
    prob = float(modelo.predict_proba(X)[0, 1])

    return PrediccionOutput(
        churn_probability=round(prob, 4),
        churn=prob >= 0.5,
    )


@app.post("/predecir_batch")
def predecir_batch(clientes: list[ClienteInput]):
    """Predecir churn para múltiples clientes."""
    if modelo is None or dv is None:
        raise HTTPException(status_code=503, detail="Modelo no cargado.")

    clientes_dicts = [c.model_dump() for c in clientes]
    X = dv.transform(clientes_dicts)
    probs = modelo.predict_proba(X)[:, 1]

    return [
        PrediccionOutput(churn_probability=round(float(p), 4), churn=p >= 0.5)
        for p in probs
    ]
