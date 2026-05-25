# Ejercicios - Módulo 2

## Ejercicio 1: NumPy

1. Crea un array con los números del 1 al 20
2. Calcula la media, mediana y desviación estándar
3. Filtra solo los números mayores a 10
4. Crea una matriz de 4x5 con números aleatorios entre 0 y 100
5. Calcula la suma de cada columna

## Ejercicio 2: Pandas

Usa el dataset de ejemplo (puedes usar cualquier CSV o crear uno):

```python
import pandas as pd

data = {
    'nombre': ['Ana', 'Luis', 'María', 'Carlos', 'Elena'],
    'edad': [25, 30, 28, 35, 22],
    'ciudad': ['Madrid', 'Barcelona', 'Madrid', 'Sevilla', 'Barcelona'],
    'salario': [30000, 45000, 38000, 52000, 28000]
}
df = pd.DataFrame(data)
```

1. Filtra las personas de Madrid
2. Calcula el salario promedio por ciudad
3. Agrega una columna `salario_mensual` (salario / 12)
4. Ordena por salario de mayor a menor
5. ¿Cuántas personas hay en cada ciudad?

## Ejercicio 3: EDA

Descarga un dataset de tu interés (sugerencia: [Kaggle Datasets](https://www.kaggle.com/datasets)) y realiza:

1. Vista general: dimensiones, tipos, nulos
2. Distribución del target (histograma)
3. Matriz de correlación con mapa de calor
4. Identifica los 3 features más correlacionados con el target
5. Escribe 3 observaciones que harías sobre los datos

## Ejercicio 4: Álgebra Lineal

```python
import numpy as np

X = np.array([
    [2, 3],
    [4, 1],
    [6, 5]
])
w = np.array([0.5, 1.2])
```

1. ¿Cuál es el shape de X?
2. Calcula el producto punto X · w (las "predicciones")
3. Calcula X^T (transpuesta) y su shape
4. Calcula X^T · X y explica qué dimensiones tiene el resultado
