# 5.2 Matriz de Confusión

## ¿Qué es?

La matriz de confusión muestra **todos los tipos de aciertos y errores** del modelo:

```text
                    Predicción
                    No Churn    Churn
Real  No Churn  │    TN     │   FP    │
      Churn     │    FN     │   TP    │
```

- **TP** (True Positive): predijo churn y ERA churn ✓
- **TN** (True Negative): predijo no churn y NO ERA churn ✓
- **FP** (False Positive): predijo churn pero NO ERA churn ✗
- **FN** (False Negative): predijo no churn pero ERA churn ✗

## Calcular con scikit-learn

```python
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_val, y_pred)
print(cm)

# Más legible
tn, fp, fn, tp = cm.ravel()
print(f"True Negatives:  {tn}")
print(f"False Positives: {fp}")
print(f"False Negatives: {fn}")
print(f"True Positives:  {tp}")
```

## Visualizar

```python
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import ConfusionMatrixDisplay

ConfusionMatrixDisplay.from_predictions(
    y_val, y_pred,
    display_labels=['No Churn', 'Churn'],
    cmap='Blues'
)
plt.title('Matriz de Confusión')
plt.show()
```

## Interpretación en contexto de negocio

| Tipo | Significado | Costo |
|------|-------------|-------|
| TP | Detectamos al cliente que iba a cancelar | Podemos retenerlo |
| TN | Correctamente identificamos cliente fiel | Sin acción necesaria |
| FP | Creímos que iba a cancelar, pero no | Gasto innecesario en retención |
| FN | No detectamos que iba a cancelar | Perdemos al cliente |

## Relación con accuracy

```python
accuracy = (tp + tn) / (tp + tn + fp + fn)
```

Pero la matriz nos da mucha más información que un solo número.

---

**Anterior**: [Accuracy](01-accuracy-modelo-dummy.md) | **Siguiente**: [Precision y Recall](03-precision-recall.md)
