# 5.4 Curva ROC y AUC

## ¿Qué es la curva ROC?

La curva ROC (Receiver Operating Characteristic) muestra el rendimiento del modelo en **todos los umbrales posibles**.

Ejes:
- **X**: False Positive Rate (FPR) = FP / (FP + TN)
- **Y**: True Positive Rate (TPR) = TP / (TP + FN) = Recall

## Calcular y graficar

```python
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

# Calcular la curva
fpr, tpr, umbrales = roc_curve(y_val, y_pred_proba)

# Graficar
plt.plot(fpr, tpr, label='Modelo')
plt.plot([0, 1], [0, 1], 'k--', label='Aleatorio')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate (Recall)')
plt.title('Curva ROC')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

## Interpretación

- **Esquina superior izquierda** (0,1) = modelo perfecto
- **Diagonal** = modelo aleatorio (no aporta nada)
- Cuanto más se aleja la curva de la diagonal → mejor modelo

## AUC (Area Under the Curve)

El AUC resume la curva ROC en un solo número:

```python
auc = roc_auc_score(y_val, y_pred_proba)
print(f"AUC: {auc:.4f}")
```

**Interpretación del AUC:**

- AUC = 1.0 → modelo perfecto
- AUC = 0.5 → modelo aleatorio (inútil)
- AUC > 0.8 → generalmente bueno
- AUC < 0.6 → modelo pobre

**Significado intuitivo**: si tomas un cliente con churn y uno sin churn al azar, el AUC es la probabilidad de que el modelo asigne mayor score al que sí hace churn.

## Comparar modelos con AUC

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

modelos = {
    'Logística': LogisticRegression(solver='liblinear', max_iter=1000),
    'Árbol': DecisionTreeClassifier(max_depth=5),
}

plt.figure(figsize=(8, 6))
for nombre, modelo in modelos.items():
    modelo.fit(X_train, y_train)
    y_proba = modelo.predict_proba(X_val)[:, 1]
    fpr, tpr, _ = roc_curve(y_val, y_proba)
    auc = roc_auc_score(y_val, y_proba)
    plt.plot(fpr, tpr, label=f'{nombre} (AUC={auc:.3f})')

plt.plot([0, 1], [0, 1], 'k--', label='Aleatorio')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Comparación de modelos - ROC')
plt.legend()
plt.show()
```

## ¿Por qué usar AUC?

- **Independiente del umbral**: evalúa el modelo en general, no para un umbral específico
- **Funciona con clases desbalanceadas** (a diferencia de accuracy)
- **Fácil de comparar** entre modelos

---

**Anterior**: [Precision y Recall](03-precision-recall.md) | **Siguiente**: [Validación Cruzada](05-validacion-cruzada.md)
