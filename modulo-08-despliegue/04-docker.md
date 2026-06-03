# 7.4 Docker: Contenedores

## ¿Qué es Docker?

Docker permite empaquetar tu aplicación con **todas sus dependencias** en un "contenedor" que funciona igual en cualquier máquina.

## ¿Por qué Docker para ML?

Sin Docker:

```text
"En mi máquina funciona..." 😅
- Versión de Python diferente
- Librería faltante
- Sistema operativo diferente
```

Con Docker:

```text
"Si funciona en el contenedor, funciona en producción" ✓
```

## Conceptos clave

- **Imagen**: plantilla con el sistema operativo + código + dependencias
- **Contenedor**: una instancia en ejecución de una imagen
- **Dockerfile**: receta para construir una imagen
- **Docker Hub**: repositorio público de imágenes base

## Comandos básicos

```bash
# Ver imágenes disponibles localmente
docker images

# Ver contenedores en ejecución
docker ps

# Ver todos los contenedores (incluso detenidos)
docker ps -a

# Ejecutar una imagen de forma interactiva
docker run -it python:3.11-slim bash

# Detener un contenedor
docker stop <container_id>

# Eliminar un contenedor
docker rm <container_id>
```

## Anatomía de un Dockerfile

```dockerfile
# Imagen base
FROM python:3.11-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivos de dependencias
COPY pyproject.toml .

# Instalar dependencias
RUN pip install --no-cache-dir .

# Copiar el código y modelos
COPY main.py .
COPY modelo_churn.joblib .
COPY vectorizer.joblib .

# Puerto que expone el servicio
EXPOSE 8000

# Comando para iniciar el servicio
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Construir y ejecutar

```bash
# Construir la imagen
docker build -t servicio-churn .

# Ejecutar el contenedor
docker run -p 8000:8000 servicio-churn
```

El flag `-p 8000:8000` mapea el puerto del contenedor al puerto de tu máquina.

## Verificar

```bash
# En otra terminal
curl http://localhost:8000/health
# {"status": "ok"}
```

---

**Anterior**: [Servicio de Predicción](03-servicio-prediccion.md) | **Siguiente**: [Dockerizar el Servicio](05-dockerizar.md)
