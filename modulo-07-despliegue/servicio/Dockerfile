FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias
COPY pyproject.toml .
RUN pip install --no-cache-dir fastapi uvicorn scikit-learn joblib numpy

# Copiar código y modelos
COPY main.py .
COPY modelo_churn.joblib .
COPY vectorizer.joblib .

# Puerto
EXPOSE 8000

# Ejecutar
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
