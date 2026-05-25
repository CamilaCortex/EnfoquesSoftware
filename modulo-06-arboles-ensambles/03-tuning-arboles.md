# 6.3 Tuning de Árboles

## Hiperparámetros clave

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score

# Buscar mejor max_depth
for depth in range(2, 15):
    arbol = DecisionTreeClassifier(max_depth=depth, random_state=42)
    arbol.fit(X_train, y_train)
    y_proba = arbol.predict_proba(X_val)[:, 1]
    auc = roc_auc_score(y_val, y_proba)
    print(f"max_depth={depth:>2}: AUC = {auc:.4f}")
```

## Combinación de hiperparámetros

```python
import itertools

depths = [3, 4, 5, 6, 7, 8]
min_samples = [5, 10, 20, 50]

mejores = []
for depth, min_s in itertools.product(depths, min_samples):
    arbol = DecisionTreeClassifier(
        max_depth=depth,
        min_samples_leaf=min_s,
        random_state=42
    )
    arbol.fit(X_train, y_train)
    y_proba = arbol.predict_proba(X_val)[:, 1]
    auc = roc_auc_score(y_val, y_proba)
    mejores.append((auc, depth, min_s))

mejores.sort(reverse=True)
print("Top 5 configuraciones:")
for auc, depth, min_s in mejores[:5]:
    print(f"  AUC={auc:.4f} | depth={depth}, min_samples_leaf={min_s}")
```

## Overfitting vs Underfitting

```python
import matplotlib.pyplot as plt

train_aucs, val_aucs = [], []
depths = range(1, 20)

for depth in depths:
    arbol = DecisionTreeClassifier(max_depth=depth, random_state=42)
    arbol.fit(X_train, y_train)
    
    train_aucs.append(roc_auc_score(y_train, arbol.predict_proba(X_train)[:, 1]))
    val_aucs.append(roc_auc_score(y_val, arbol.predict_proba(X_val)[:, 1]))

plt.plot(depths, train_aucs, label='Train')
plt.plot(depths, val_aucs, label='Validación')
plt.xlabel('max_depth')
plt.ylabel('AUC')
plt.title('Overfitting: Train vs Validación')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

El punto óptimo es donde validación deja de mejorar (o empieza a empeorar).

---

**Anterior**: [Algoritmo de Aprendizaje](02-algoritmo-aprendizaje.md) | **Siguiente**: [Random Forest](04-random-forest.md)
