# 6.5 XGBoost

## ¿Qué es Gradient Boosting?

A diferencia de Random Forest (que entrena árboles en paralelo), **Gradient Boosting** entrena árboles **secuencialmente**. Cada nuevo árbol intenta corregir los errores del anterior.

```text
Árbol 1 → errores → Árbol 2 → errores → Árbol 3 → ...
```

**XGBoost** (eXtreme Gradient Boosting) es la implementación más popular y eficiente.

## Instalación

Ya está incluido en `pyproject.toml`. Si necesitas instalarlo manualmente:

```bash
uv add xgboost
```

## Implementación básica

```python
import xgboost as xgb
from sklearn.metrics import roc_auc_score

# Crear matrices DMatrix (formato optimizado de XGBoost)
dtrain = xgb.DMatrix(X_train, label=y_train)
dval = xgb.DMatrix(X_val, label=y_val)

# Parámetros
params = {
    'objective': 'binary:logistic',
    'eval_metric': 'auc',
    'max_depth': 4,
    'learning_rate': 0.1,
    'verbosity': 0,
}

# Entrenar con early stopping
modelo = xgb.train(
    params,
    dtrain,
    num_boost_round=200,
    evals=[(dval, 'val')],
    early_stopping_rounds=20,
    verbose_eval=10
)

# Predecir
y_proba = modelo.predict(dval)
auc = roc_auc_score(y_val, y_proba)
print(f"XGBoost AUC: {auc:.4f}")
```

## Hiperparámetros clave

| Parámetro | Qué controla | Valores típicos |
|-----------|-------------|-----------------|
| `max_depth` | Profundidad de cada árbol | 3-8 |
| `learning_rate` (eta) | Velocidad de aprendizaje | 0.01-0.3 |
| `n_estimators` | Número de árboles | 100-1000 |
| `subsample` | Fracción de datos por árbol | 0.7-1.0 |
| `colsample_bytree` | Fracción de features por árbol | 0.7-1.0 |
| `reg_lambda` | Regularización L2 | 1-10 |

## Tuning de XGBoost

```python
mejores = []

for depth in [3, 4, 5, 6]:
    for lr in [0.05, 0.1, 0.2]:
        params = {
            'objective': 'binary:logistic',
            'eval_metric': 'auc',
            'max_depth': depth,
            'learning_rate': lr,
            'verbosity': 0,
        }
        modelo = xgb.train(
            params, dtrain,
            num_boost_round=200,
            evals=[(dval, 'val')],
            early_stopping_rounds=20,
            verbose_eval=False
        )
        y_proba = modelo.predict(dval)
        auc = roc_auc_score(y_val, y_proba)
        mejores.append((auc, depth, lr, modelo.best_iteration))

mejores.sort(reverse=True)
for auc, depth, lr, n_trees in mejores[:5]:
    print(f"AUC={auc:.4f} | depth={depth}, lr={lr}, trees={n_trees}")
```

## ¿Cuándo usar XGBoost?

- Cuando quieres el **mejor rendimiento** en datos tabulares
- Competencias de ML (Kaggle)
- Cuando tienes suficientes datos (>1000 filas)
- No es necesario para datasets pequeños o cuando la interpretabilidad es crítica

---

**Anterior**: [Random Forest](04-random-forest.md) | **Siguiente**: [Modelo Final](06-modelo-final.md)
