# 3.3 Regresión Lineal

## Intuición

La regresión lineal busca una **línea recta** (o hiperplano) que mejor se ajuste a los datos.

```text
precio = w₀ + w₁·año + w₂·km + w₃·hp + ...
```

Donde:

- `w₀` es el **intercepto** (bias)
- `w₁, w₂, w₃...` son los **pesos** (importancia de cada feature)

## Implementación desde cero (concepto)

```python
import numpy as np

def entrenar_regresion_lineal(X, y):
    """Ecuación normal: w = (X^T · X)^(-1) · X^T · y"""
    # Agregar columna de 1s para el intercepto
    ones = np.ones(X.shape[0])
    X_con_bias = np.column_stack([ones, X])

    # Ecuación normal
    XTX = X_con_bias.T.dot(X_con_bias)
    XTX_inv = np.linalg.inv(XTX)
    w = XTX_inv.dot(X_con_bias.T).dot(y)

    return w[0], w[1:]  # bias, pesos


def predecir(X, bias, pesos):
    return bias + X.dot(pesos)
```

## Con scikit-learn (forma práctica)

```python
from sklearn.linear_model import LinearRegression

# Crear y entrenar el modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Predecir
y_pred = modelo.predict(X_val)

# Ver los pesos aprendidos
print(f"Intercepto: {modelo.intercept_:.4f}")
print(f"Pesos: {modelo.coef_}")
```

## ¿Qué significan los pesos?

Cada peso indica **cuánto cambia la predicción** cuando ese feature aumenta en 1 unidad (manteniendo los demás constantes).

```python
# Ejemplo de interpretación
for nombre, peso in zip(nombres_features, modelo.coef_):
    print(f"{nombre}: {peso:.4f}")

# Si peso de 'año' = 0.05, significa:
# por cada año más nuevo, el log(precio) sube 0.05
```

## Limitaciones de la regresión lineal

- Asume relación **lineal** entre features y target
- Sensible a **outliers**
- Puede tener problemas con features altamente correlacionadas (multicolinealidad)
- No captura relaciones complejas entre variables

## ¿Cuándo usarla?

- Como **modelo baseline** (primer intento rápido)
- Cuando la relación es aproximadamente lineal
- Cuando necesitas **interpretabilidad** (entender qué features importan)
- Cuando tienes pocos datos

---

**Anterior**: [Preparación de Datos](02-preparacion-datos.md) | **Siguiente**: [Validación y RMSE](04-validacion-rmse.md)
