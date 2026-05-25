# 5.3 Precision y Recall

## Definiciones

**Precision**: De todos los que el modelo dijo que son churn, ¿cuántos realmente lo son?

```text
Precision = TP / (TP + FP)
```

**Recall** (Sensibilidad): De todos los que realmente son churn, ¿cuántos detectó el modelo?

```text
Recall = TP / (TP + FN)
```

## Ejemplo intuitivo

Imagina que el modelo marca 100 clientes como "riesgo de churn":

- **Precision = 80%**: de esos 100, 80 realmente cancelarán
- **Recall = 60%**: pero en total había 133 clientes que iban a cancelar, solo detectamos 80

## Calcular con scikit-learn

```python
from sklearn.metrics import precision_score, recall_score, f1_score

precision = precision_score(y_val, y_pred)
recall = recall_score(y_val, y_pred)
f1 = f1_score(y_val, y_pred)

print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-score:  {f1:.4f}")
```

## El trade-off Precision vs Recall

Al bajar el umbral:

- **Recall sube** → detectamos más positivos reales
- **Precision baja** → también aumentan los falsos positivos

```python
import numpy as np

umbrales = np.arange(0.1, 0.9, 0.05)
for umbral in umbrales:
    y_pred_t = (y_pred_proba >= umbral).astype(int)
    p = precision_score(y_val, y_pred_t, zero_division=0)
    r = recall_score(y_val, y_pred_t)
    print(f"Umbral {umbral:.2f}: Precision={p:.3f}, Recall={r:.3f}")
```

## F1-Score: combinando ambas

El F1-score es la **media armónica** de precision y recall:

```text
F1 = 2 · (Precision · Recall) / (Precision + Recall)
```

- F1 = 1.0 → perfecto
- F1 es alto solo si AMBAS métricas son altas

## ¿Cuál priorizar?

| Situación | Priorizar | Ejemplo |
|-----------|-----------|---------|
| FN es muy costoso | **Recall** | Detectar cáncer, fraude |
| FP es muy costoso | **Precision** | Bloquear cuentas bancarias |
| Balance | **F1** | Churn prediction general |

---

**Anterior**: [Matriz de Confusión](02-matriz-confusion.md) | **Siguiente**: [ROC y AUC](04-roc-auc.md)
