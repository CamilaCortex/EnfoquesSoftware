# 3.4 Validación y RMSE

## ¿Cómo sabemos si el modelo es bueno?

Necesitamos una **métrica** que mida qué tan lejos están nuestras predicciones de los valores reales.

## RMSE (Root Mean Squared Error)

La métrica más común para regresión:

```text
RMSE = √(1/n · Σ(yᵢ - ŷᵢ)²)
```

En palabras: es el **promedio de los errores al cuadrado**, y luego la raíz. Tiene las mismas unidades que el target.

```python
import numpy as np

def rmse(y_real, y_pred):
    error = y_real - y_pred
    mse = (error ** 2).mean()
    return np.sqrt(mse)
```

O con scikit-learn:

```python
from sklearn.metrics import root_mean_squared_error

score = root_mean_squared_error(y_val, y_pred)
print(f"RMSE: {score:.4f}")
```

## Interpretación del RMSE

- RMSE = 0 → predicción perfecta (imposible en la práctica)
- Menor RMSE → mejor modelo
- Si predecimos log(precio), un RMSE de 0.5 significa que en promedio nos equivocamos por ~0.5 en escala log

## Framework de validación

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error

# Entrenar
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Evaluar en validación
y_pred_val = modelo.predict(X_val)
rmse_val = root_mean_squared_error(y_val, y_pred_val)
print(f"RMSE validación: {rmse_val:.4f}")

# Solo al final: evaluar en test
y_pred_test = modelo.predict(X_test)
rmse_test = root_mean_squared_error(y_test, y_pred_test)
print(f"RMSE test: {rmse_test:.4f}")
```

## Modelo baseline: predecir la media

Antes de hacer nada sofisticado, calcula el RMSE de simplemente predecir la media:

```python
# Baseline: predecir siempre la media del target
y_pred_baseline = np.full_like(y_val, y_train.mean())
rmse_baseline = root_mean_squared_error(y_val, y_pred_baseline)
print(f"RMSE baseline (media): {rmse_baseline:.4f}")
```

Si tu modelo no supera este baseline, algo está mal.

## Comparar modelos

```python
resultados = {
    'Baseline (media)': rmse_baseline,
    'Regresión lineal': rmse_val,
}

for nombre, score in sorted(resultados.items(), key=lambda x: x[1]):
    print(f"{nombre}: RMSE = {score:.4f}")
```

---

**Anterior**: [Regresión Lineal](03-regresion-lineal.md) | **Siguiente**: [Feature Engineering](05-feature-engineering.md)
