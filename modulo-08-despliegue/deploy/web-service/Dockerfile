# Imagen base de Python
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Copiar archivos de configuración
COPY pyproject.toml ./

# Instalar dependencias directamente con pip
RUN pip install --no-cache-dir \
    fastapi>=0.136.3 \
    uvicorn[standard]>=0.49.0 \
    mlflow>=3.13.0 \
    xgboost>=3.2.0 \
    scikit-learn>=1.4

# Copiar código fuente
COPY app.py ./
COPY src/ ./src/
COPY templates/ ./templates/

# Copiar modelo (debe existir antes de build)
COPY model/ ./model/

# Exponer puerto
EXPOSE 8000

# Comando para iniciar la API
CMD ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
