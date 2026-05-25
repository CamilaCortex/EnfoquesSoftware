# 2.4 Álgebra Lineal para ML

## ¿Por qué importa?

La mayoría de algoritmos de ML operan internamente con vectores y matrices. No necesitas ser experto, pero entender los conceptos básicos te ayudará a comprender cómo funcionan los modelos.

## Vectores

Un vector es una lista ordenada de números. En ML, cada observación se representa como un vector.

```python
import numpy as np

# Un auto descrito por sus features: [km, año, potencia]
auto = np.array([50000, 2019, 150])
```

## Operaciones con vectores

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Suma
a + b  # [5, 7, 9]

# Multiplicación por escalar
a * 3  # [3, 6, 9]

# Producto punto (dot product)
np.dot(a, b)  # 1*4 + 2*5 + 3*6 = 32
```

### ¿Qué significa el producto punto?

El producto punto mide la **similitud** entre dos vectores. Es la base de la regresión lineal:

```text
predicción = w₁·x₁ + w₂·x₂ + w₃·x₃ + ... = w · x (producto punto)
```

## Matrices

Una matriz es una colección de vectores. En ML, la **matriz de features X** tiene:

- Filas = observaciones (autos, clientes, emails...)
- Columnas = features (km, año, precio...)

```python
# 3 autos, cada uno con 3 features
X = np.array([
    [50000, 2019, 150],  # Auto 1
    [30000, 2021, 120],  # Auto 2
    [80000, 2017, 180],  # Auto 3
])

X.shape  # (3, 3) → 3 observaciones, 3 features
```

## Multiplicación matriz-vector

Esto es lo que hace un modelo lineal internamente:

```python
# Pesos del modelo (aprendidos durante entrenamiento)
w = np.array([−0.0001, 500, 100])

# Predicciones para todos los autos
predicciones = X.dot(w)
# Equivalente: np.dot(X, w)
```

Cada predicción es el producto punto de una fila de X con el vector de pesos w.

## Transpuesta

Intercambia filas por columnas:

```python
X.T        # shape pasa de (3, 3) a (3, 3) en este caso
# Si X fuera (100, 5), X.T sería (5, 100)
```

## Matriz identidad e inversa

```python
# Identidad: el "1" de las matrices
I = np.eye(3)

# Inversa (no siempre existe)
A = np.array([[1, 2], [3, 4]])
A_inv = np.linalg.inv(A)

# Verificar: A * A_inv = Identidad
np.dot(A, A_inv)  # ≈ [[1, 0], [0, 1]]
```

## Resumen: ¿Qué necesitas recordar?

| Concepto | En ML se usa para... |
|----------|---------------------|
| Vector | Representar una observación o los pesos del modelo |
| Producto punto | Calcular predicciones en modelos lineales |
| Matriz | Representar todo el dataset (X) |
| Multiplicación matriz-vector | Predecir para múltiples observaciones a la vez |
| Inversa | Resolver la ecuación normal (regresión lineal) |

---

**Anterior**: [EDA](03-eda.md) | **Volver al módulo**: [README](README.md)
