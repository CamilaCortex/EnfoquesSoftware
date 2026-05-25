# 6.4 Random Forest

## Idea principal

En lugar de un solo árbol, entrenamos **muchos árboles** y combinamos sus predicciones (votación). Esto reduce el overfitting y mejora la estabilidad.

## ¿Por qué funciona?

Cada árbol del bosque se entrena con:

- Una **muestra aleatoria** de los datos (bootstrap)
- Un **subconjunto aleatorio** de features en cada split

Esto hace que los árboles sean **diversos** entre sí. Al promediar sus predicciones, los errores individuales se cancelan.

## Implementación

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

rf = RandomForestClassifier(
    n_estimators=100,      # número de árboles
    max_depth=6,           # profundidad máxima
    min_samples_leaf=5,    # mín muestras por hoja
    random_state=42,
    n_jobs=-1              # usar todos los CPUs
)
rf.fit(X_train, y_train)

y_proba = rf.predict_proba(X_val)[:, 1]
auc = roc_auc_score(y_val, y_proba)
print(f"Random Forest AUC: {auc:.4f}")
```

## Tuning de Random Forest

```python
from sklearn.model_selection import cross_val_score

configs = [
    {'n_estimators': 50, 'max_depth': 5},
    {'n_estimators': 100, 'max_depth': 6},
    {'n_estimators': 200, 'max_depth': 7},
    {'n_estimators': 100, 'max_depth': 10},
]

for cfg in configs:
    rf = RandomForestClassifier(**cfg, min_samples_leaf=5, 
                                random_state=42, n_jobs=-1)
    scores = cross_val_score(rf, X_train, y_train, cv=5, scoring='roc_auc')
    print(f"n={cfg['n_estimators']}, depth={cfg['max_depth']}: "
          f"AUC={scores.mean():.4f} ± {scores.std():.4f}")
```

## Feature Importance

```python
importancia = pd.DataFrame({
    'feature': feature_names,
    'importancia': rf.feature_importances_
}).sort_values('importancia', ascending=False)

importancia.head(10).plot(x='feature', y='importancia', kind='barh')
plt.title('Feature Importance - Random Forest')
plt.show()
```

## Random Forest vs Árbol individual

| Aspecto | Árbol | Random Forest |
|---------|-------|---------------|
| Overfitting | Alto | Bajo |
| Interpretabilidad | Alta | Media |
| Rendimiento | Moderado | Alto |
| Velocidad | Rápido | Más lento |

---

**Anterior**: [Tuning de Árboles](03-tuning-arboles.md) | **Siguiente**: [XGBoost](05-xgboost.md)
