# 3.6 Regularización

## El problema: Overfitting

Cuando el modelo se ajusta **demasiado** a los datos de entrenamiento, pierde capacidad de generalizar a datos nuevos.

```text
Entrenamiento: RMSE = 0.10  (muy bajo)
Validación:    RMSE = 0.85  (mucho mayor)
→ El modelo memorizó en vez de aprender patrones
```

## ¿Qué es regularización?

La regularización **penaliza pesos grandes** en el modelo, forzándolo a ser más simple y generalizable.

## Ridge (L2)

Agrega una penalización proporcional al **cuadrado de los pesos**:

```text
Objetivo = Error + α · Σ(wᵢ²)
```

- `α` (alpha) controla la fuerza de la penalización
- α = 0 → regresión lineal normal
- α grande → pesos se acercan a 0

```python
from sklearn.linear_model import Ridge

# Probar diferentes valores de alpha
for alpha in [0.001, 0.01, 0.1, 1, 10, 100]:
    modelo = Ridge(alpha=alpha)
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_val)
    score = root_mean_squared_error(y_val, y_pred)
    print(f"alpha={alpha:>6}: RMSE = {score:.4f}")
```

## Encontrar el mejor alpha

```python
from sklearn.linear_model import Ridge
from sklearn.metrics import root_mean_squared_error
import numpy as np

alphas = np.logspace(-3, 3, 50)  # De 0.001 a 1000
resultados = []

for alpha in alphas:
    modelo = Ridge(alpha=alpha)
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_val)
    rmse = root_mean_squared_error(y_val, y_pred)
    resultados.append((alpha, rmse))

# Mejor alpha
mejor = min(resultados, key=lambda x: x[1])
print(f"Mejor alpha: {mejor[0]:.4f}, RMSE: {mejor[1]:.4f}")
```

## Visualizar el efecto

```python
import matplotlib.pyplot as plt

alphas_list, rmses = zip(*resultados)
plt.plot(alphas_list, rmses)
plt.xscale('log')
plt.xlabel('Alpha (regularización)')
plt.ylabel('RMSE')
plt.title('Efecto de la regularización')
plt.show()
```

## Modelo final

Una vez elegido el mejor alpha:

```python
# Entrenar con train + val combinados
import numpy as np

X_full = np.vstack([X_train, X_val])
y_full = np.concatenate([y_train, y_val])

modelo_final = Ridge(alpha=mejor_alpha)
modelo_final.fit(X_full, y_full)

# Evaluar en test (solo una vez)
y_pred_test = modelo_final.predict(X_test)
rmse_test = root_mean_squared_error(y_test, y_pred_test)
print(f"RMSE final (test): {rmse_test:.4f}")
```

## Resumen

| Situación | Solución |
|-----------|----------|
| RMSE train ≈ RMSE val | Modelo bien ajustado |
| RMSE train << RMSE val | Overfitting → más regularización |
| RMSE train ≈ RMSE val pero ambos altos | Underfitting → más features o modelo más complejo |

---

**Anterior**: [Feature Engineering](05-feature-engineering.md) | **Volver al módulo**: [README](README.md)
