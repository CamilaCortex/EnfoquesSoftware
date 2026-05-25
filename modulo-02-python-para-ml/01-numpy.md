# 2.1 NumPy: Operaciones Vectoriales

## ¿Por qué NumPy?

NumPy es la base de todo el ecosistema de ML en Python. Permite operar con arrays de forma eficiente, mucho más rápido que las listas nativas de Python.

## Crear arrays

```python
import numpy as np

# Desde una lista
a = np.array([1, 2, 3, 4, 5])

# Arrays especiales
zeros = np.zeros(10)          # 10 ceros
ones = np.ones(5)             # 5 unos
rango = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
lineal = np.linspace(0, 1, 5) # 5 valores entre 0 y 1
```

## Operaciones vectorizadas

La gran ventaja: operar sobre todo el array sin loops.

```python
a = np.array([1, 2, 3, 4, 5])

# Operaciones elemento a elemento
a * 2        # [2, 4, 6, 8, 10]
a + 10       # [11, 12, 13, 14, 15]
a ** 2       # [1, 4, 9, 16, 25]

# Operaciones entre arrays
b = np.array([10, 20, 30, 40, 50])
a + b        # [11, 22, 33, 44, 55]
a * b        # [10, 40, 90, 160, 250]
```

## Indexación y slicing

```python
a = np.array([10, 20, 30, 40, 50])

a[0]         # 10 (primer elemento)
a[-1]        # 50 (último elemento)
a[1:4]       # [20, 30, 40]
a[a > 25]    # [30, 40, 50] (filtrado booleano)
```

## Funciones estadísticas

```python
datos = np.array([23, 45, 12, 67, 34, 89, 56])

datos.mean()    # Promedio
datos.std()     # Desviación estándar
datos.min()     # Mínimo
datos.max()     # Máximo
datos.sum()     # Suma total
np.median(datos) # Mediana
```

## Matrices (arrays 2D)

```python
# Crear matriz 3x3
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

matriz.shape      # (3, 3)
matriz[0]         # [1, 2, 3] (primera fila)
matriz[:, 0]      # [1, 4, 7] (primera columna)
matriz[1, 2]      # 6 (fila 1, columna 2)
```

## Generación de datos aleatorios

```python
np.random.seed(42)  # Para reproducibilidad

# Números aleatorios uniformes entre 0 y 1
np.random.rand(5)

# Números aleatorios normales (media=0, std=1)
np.random.randn(100)

# Enteros aleatorios
np.random.randint(1, 100, size=10)
```

---

**Siguiente**: [Pandas](02-pandas.md)
