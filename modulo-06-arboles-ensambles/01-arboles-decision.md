# 6.1 Árboles de Decisión

## Intuición

Un árbol de decisión funciona como un **diagrama de flujo**: hace preguntas binarias sobre los features hasta llegar a una predicción.

```text
¿Antigüedad > 2 años?
├── Sí → ¿Ingreso > 50k?
│       ├── Sí → No default (bajo riesgo)
│       └── No → ¿Deuda > 30k?
│               ├── Sí → Default (alto riesgo)
│               └── No → No default
└── No → ¿Tiene aval?
        ├── Sí → No default
        └── No → Default (alto riesgo)
```

## Ventajas

- Fácil de **interpretar** y explicar
- No requiere normalización de datos
- Maneja variables numéricas y categóricas
- Captura **relaciones no lineales**

## Implementación básica

```python
from sklearn.tree import DecisionTreeClassifier

# Entrenar
arbol = DecisionTreeClassifier(max_depth=4, random_state=42)
arbol.fit(X_train, y_train)

# Predecir
y_pred = arbol.predict(X_val)
y_pred_proba = arbol.predict_proba(X_val)[:, 1]

# Evaluar
from sklearn.metrics import roc_auc_score
auc = roc_auc_score(y_val, y_pred_proba)
print(f"AUC: {auc:.4f}")
```

## Visualizar el árbol

```python
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 10))
plot_tree(arbol, feature_names=feature_names, 
          class_names=['No default', 'Default'],
          filled=True, rounded=True, max_depth=3)
plt.tight_layout()
plt.show()
```

## Importancia de features

```python
importancia = pd.DataFrame({
    'feature': feature_names,
    'importancia': arbol.feature_importances_
}).sort_values('importancia', ascending=False)

print(importancia.head(10))

# Gráfico
importancia.head(10).plot(x='feature', y='importancia', kind='barh')
plt.title('Feature Importance - Árbol de Decisión')
plt.show()
```

## Limitaciones

- **Overfitting**: sin restricciones, el árbol memoriza los datos
- **Inestable**: pequeños cambios en datos pueden generar árboles muy diferentes
- **No es el mejor** en rendimiento puro vs. ensambles

---

**Siguiente**: [Algoritmo de Aprendizaje](02-algoritmo-aprendizaje.md)
