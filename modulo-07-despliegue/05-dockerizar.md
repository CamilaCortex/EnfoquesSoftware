# 7.5 Dockerizar el Servicio Completo

## Estructura final del servicio

```text
servicio-churn/
├── Dockerfile
├── main.py
├── modelo_churn.joblib
├── vectorizer.joblib
├── pyproject.toml
├── .dockerignore
└── test_api.py
```

## Dockerfile optimizado

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema si son necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Copiar solo dependencias primero (cache de Docker)
COPY pyproject.toml .
RUN pip install --no-cache-dir -e .

# Copiar código y modelos
COPY main.py .
COPY modelo_churn.joblib .
COPY vectorizer.joblib .

# Puerto
EXPOSE 8000

# Ejecutar con uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## pyproject.toml del servicio

```toml
[project]
name = "servicio-churn"
version = "1.0.0"
requires-python = ">=3.11"
dependencies = [
    "fastapi>=0.109",
    "uvicorn>=0.27",
    "scikit-learn>=1.4",
    "joblib>=1.3",
    "numpy>=1.26",
]
```

## .dockerignore

```text
__pycache__
*.pyc
.venv
.git
*.ipynb
```

## Construir y ejecutar

```bash
# Construir
docker build -t servicio-churn:v1 .

# Ejecutar en background
docker run -d -p 8000:8000 --name churn-api servicio-churn:v1

# Ver logs
docker logs churn-api

# Detener
docker stop churn-api
```

## Probar el servicio completo

```python
# test_api.py
import httpx

BASE_URL = "http://localhost:8000"

# Test health
r = httpx.get(f"{BASE_URL}/health")
assert r.status_code == 200
print("✓ Health check OK")

# Test predicción - cliente de alto riesgo
cliente_alto_riesgo = {
    "contract": "Month-to-month",
    "tenure": 1,
    "monthly_charges": 85.0,
    "total_charges": 85.0,
    "internet_service": "Fiber optic",
    "online_security": "No",
    "tech_support": "No",
    "payment_method": "Electronic check"
}

r = httpx.post(f"{BASE_URL}/predecir", json=cliente_alto_riesgo)
assert r.status_code == 200
resultado = r.json()
print(f"✓ Alto riesgo: prob={resultado['churn_probability']:.3f}, churn={resultado['churn']}")

# Test predicción - cliente de bajo riesgo
cliente_bajo_riesgo = {
    "contract": "Two year",
    "tenure": 48,
    "monthly_charges": 45.0,
    "total_charges": 2160.0,
    "internet_service": "DSL",
    "online_security": "Yes",
    "tech_support": "Yes",
    "payment_method": "Bank transfer (automatic)"
}

r = httpx.post(f"{BASE_URL}/predecir", json=cliente_bajo_riesgo)
assert r.status_code == 200
resultado = r.json()
print(f"✓ Bajo riesgo: prob={resultado['churn_probability']:.3f}, churn={resultado['churn']}")

print("\n¡Todos los tests pasaron!")
```

```bash
python test_api.py
```

## Resumen: de notebook a producción

```text
1. Entrenar modelo en Jupyter      → modelo_churn.joblib
2. Crear API con FastAPI           → main.py
3. Empaquetar con Docker           → Dockerfile
4. Construir imagen                → docker build
5. Ejecutar contenedor             → docker run
6. Probar                          → test_api.py
```

---

**Anterior**: [Docker](04-docker.md) | **Volver al módulo**: [README](README.md)
