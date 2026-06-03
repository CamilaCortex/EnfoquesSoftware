# Módulo 7: Despliegue de Modelos

> **Objetivo**: Al terminar este módulo podrás empaquetar un modelo de ML como un servicio web usando FastAPI y Docker, listo para producción.

---

## Contenido

| Lección | Tema |
|---------|------|
| 7.1 | [Serialización de Modelos](01-serializacion.md) |
| 7.2 | [Introducción a FastAPI](02-fastapi-intro.md) |
| 7.3 | [Crear el Servicio de Predicción](03-servicio-prediccion.md) |
| 7.4 | [Docker: Contenedores](04-docker.md) |
| 7.5 | [Dockerizar el Servicio](05-dockerizar.md) |
| BONUS | [Serverless](06-bonus-serverless.md) |
| BONUS | [Kubernetes](07-bonus-kubernetes.md) |

---

## Resumen

- Guardar y cargar modelos con joblib/pickle
- Crear APIs REST con FastAPI
- Validar datos de entrada con Pydantic
- Contenedores Docker: concepto y uso
- Crear un Dockerfile para el servicio de ML
- Ejecutar y probar el servicio dockerizado

## Prerrequisitos

- Docker Desktop instalado ([descargar](https://www.docker.com/products/docker-desktop/))
- Modelo entrenado del módulo anterior
