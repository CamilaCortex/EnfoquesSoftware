# 4.4 Regresión Logística

## Intuición

La regresión logística es un modelo de clasificación que predice la **probabilidad** de pertenecer a una clase.

A diferencia de la regresión lineal que puede dar cualquier número, la logística siempre devuelve un valor entre 0 y 1.

## ¿Cómo funciona?

### Paso 1: Combinación lineal (igual que regresión)

```text
z = w₀ + w₁·x₁ + w₂·x₂ + ... + wₙ·xₙ
```

### Paso 2: Función sigmoide

Transforma z (cualquier número) en una probabilidad (entre 0 y 1):

```text
P(y=1) = σ(z) = 1 / (1 + e^(-z))
```

```python
import numpy as np

def sigmoide(z):
    return 1 / (1 + np.exp(-z))

# Ejemplos
sigmoide(0)    # 0.5 (50% probabilidad)
sigmoide(3)    # 0.95 (muy probable positivo)
sigmoide(-3)   # 0.05 (muy probable negativo)
```

### Paso 3: Decisión

```python
umbral = 0.5
prediccion = 1 if probabilidad >= umbral else 0
```

## Visualización de la sigmoide

```python
import matplotlib.pyplot as plt
import numpy as np

z = np.linspace(-6, 6, 100)
plt.plot(z, sigmoide(z))
plt.axhline(y=0.5, color='r', linestyle='--', alpha=0.5)
plt.axvline(x=0, color='g', linestyle='--', alpha=0.5)
plt.xlabel('z (combinación lineal)')
plt.ylabel('P(y=1)')
plt.title('Función Sigmoide')
plt.grid(True, alpha=0.3)
plt.show()
```

## One-Hot Encoding

Antes de entrenar, necesitamos convertir variables categóricas a numéricas:

```python
from sklearn.feature_extraction import DictVectorizer

# Convertir DataFrame a lista de diccionarios
train_dicts = df_train[categoricas + numericas].to_dict(orient='records')

# DictVectorizer hace One-Hot Encoding automáticamente
dv = DictVectorizer(sparse=False)
X_train = dv.fit_transform(train_dicts)

# Para validación: solo transform (no fit)
val_dicts = df_val[categoricas + numericas].to_dict(orient='records')
X_val = dv.transform(val_dicts)

print(f"Features después de encoding: {X_train.shape[1]}")
```

## ¿Por qué DictVectorizer?

- Maneja categóricas y numéricas en un solo paso
- Las categóricas se convierten automáticamente a One-Hot
- Las numéricas pasan tal cual
- Sabe manejar categorías nuevas en validación/test

---

**Anterior**: [Importancia de Features](03-importancia-features.md) | **Siguiente**: [Entrenamiento con sklearn](05-entrenamiento-sklearn.md)
