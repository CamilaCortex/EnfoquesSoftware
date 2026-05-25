# 6.6 Selección del Modelo Final

## Comparación de modelos

```python
from sklearn.metrics import roc_auc_score

resultados = {
    'Logística': auc_logistica,
    'Árbol (depth=5)': auc_arbol,
    'Random Forest': auc_rf,
    'XGBoost': auc_xgb,
}

print(f"{'Modelo':<20} {'AUC':>8}")
print("-" * 30)
for nombre, auc in sorted(resultados.items(), key=lambda x: -x[1]):
    print(f"{nombre:<20} {auc:>8.4f}")
```

## Entrenar el modelo final

Una vez elegido el mejor modelo y sus hiperparámetros:

```python
import numpy as np
import xgboost as xgb

# Combinar train + val para entrenar el modelo final
X_full = np.vstack([X_train, X_val])
y_full = np.concatenate([y_train, y_val])

# Entrenar con la mejor configuración
dfull = xgb.DMatrix(X_full, label=y_full)
dtest = xgb.DMatrix(X_test, label=y_test)

params_final = {
    'objective': 'binary:logistic',
    'eval_metric': 'auc',
    'max_depth': 4,
    'learning_rate': 0.1,
    'verbosity': 0,
}

modelo_final = xgb.train(params_final, dfull, num_boost_round=mejor_n_trees)

# Evaluación final en test
y_pred_test = modelo_final.predict(dtest)
auc_test = roc_auc_score(y_test, y_pred_test)
print(f"AUC final (test): {auc_test:.4f}")
```

## Guardar el modelo

```python
import joblib

# Guardar modelo y vectorizer
joblib.dump(modelo_final, 'modelo_final.joblib')
joblib.dump(dv, 'vectorizer.joblib')

# Para cargar después:
# modelo = joblib.load('modelo_final.joblib')
# dv = joblib.load('vectorizer.joblib')
```

## Resumen del flujo completo

```text
1. Preparar datos → train/val/test
2. Entrenar varios modelos (logística, árbol, RF, XGBoost)
3. Evaluar en validación (AUC, cross-validation)
4. Elegir el mejor modelo + hiperparámetros
5. Re-entrenar con train + val combinados
6. Evaluar en test (una sola vez)
7. Guardar el modelo final
```

---

**Anterior**: [XGBoost](05-xgboost.md) | **Volver al módulo**: [README](README.md)
