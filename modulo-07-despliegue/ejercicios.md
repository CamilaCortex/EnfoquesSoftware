# Ejercicios - Módulo 7

## Ejercicio 1: Serialización

1. Toma tu mejor modelo del módulo 6 y guárdalo con joblib
2. Guarda también el DictVectorizer (o el preprocesador que uses)
3. En un script nuevo, carga ambos archivos y haz una predicción de prueba
4. Verifica que el resultado sea idéntico al del notebook

## Ejercicio 2: API básica con FastAPI

1. Crea un archivo `main.py` con un endpoint GET `/health`
2. Agrega un endpoint POST `/predecir` que reciba datos de un cliente
3. Define el modelo Pydantic con los campos necesarios
4. Ejecuta con `uvicorn` y prueba desde `/docs`

## Ejercicio 3: Servicio completo

1. Integra el modelo serializado en tu API
2. Implementa la lógica de predicción completa
3. Prueba con al menos 3 clientes diferentes
4. Verifica que los resultados tengan sentido

## Ejercicio 4: Dockerizar

1. Crea un `Dockerfile` para tu servicio
2. Crea un `.dockerignore` apropiado
3. Construye la imagen con `docker build`
4. Ejecuta el contenedor y prueba que funcione
5. Ejecuta `test_api.py` contra el contenedor

## Ejercicio 5 (bonus): Múltiples predicciones

Agrega un endpoint `/predecir_batch` que reciba una lista de clientes y devuelva predicciones para todos:

```python
@app.post("/predecir_batch")
def predecir_batch(clientes: list[ClienteInput]):
    # Implementar predicción en batch
    pass
```
