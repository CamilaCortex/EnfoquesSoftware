# 3.5 Feature Engineering

## ¿Qué es Feature Engineering?

Es el proceso de **crear, transformar o seleccionar variables** para mejorar el rendimiento del modelo. A menudo tiene más impacto que cambiar el algoritmo.

## Técnicas comunes

### 1. Variables categóricas → numéricas

Los modelos lineales solo entienden números. Necesitamos convertir categorías.

```python
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

# One-Hot Encoding manual con pandas
categoricas = ['make', 'transmission_type', 'vehicle_size']
df_encoded = pd.get_dummies(df_train[categoricas])

# Combinar con numéricas
numericas = ['year', 'engine_hp', 'engine_cylinders', 'highway_mpg', 'city_mpg']
X_train = pd.concat([df_train[numericas], df_encoded], axis=1).values
```

### 2. Crear nuevas variables

```python
# Antigüedad del auto (más interpretable que el año)
df['antiguedad'] = 2024 - df['year']

# Ratio de consumo
df['ratio_consumo'] = df['highway_mpg'] / (df['city_mpg'] + 1)
```

### 3. Transformaciones matemáticas

```python
import numpy as np

# Log para variables con distribución sesgada
df['log_hp'] = np.log1p(df['engine_hp'])
df['log_km'] = np.log1p(df['kilometraje'])
```

### 4. Binning (discretizar)

```python
# Convertir año a décadas
df['decada'] = (df['year'] // 10) * 10
```

## Impacto en el modelo

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error

# Modelo con features originales
modelo_v1 = LinearRegression().fit(X_train_v1, y_train)
rmse_v1 = root_mean_squared_error(y_val, modelo_v1.predict(X_val_v1))

# Modelo con features engineered
modelo_v2 = LinearRegression().fit(X_train_v2, y_train)
rmse_v2 = root_mean_squared_error(y_val, modelo_v2.predict(X_val_v2))

print(f"RMSE sin engineering: {rmse_v1:.4f}")
print(f"RMSE con engineering: {rmse_v2:.4f}")
print(f"Mejora: {(rmse_v1 - rmse_v2) / rmse_v1 * 100:.1f}%")
```

## Consejos prácticos

- **Empieza simple**: usa las variables tal cual antes de transformar
- **Piensa en el dominio**: ¿qué información podría ser útil?
- **Valida cada cambio**: no toda transformación mejora el modelo
- **Cuidado con data leakage**: no uses información del futuro o del target para crear features

---

**Anterior**: [Validación y RMSE](04-validacion-rmse.md) | **Siguiente**: [Regularización](06-regularizacion.md)
