# 5.1 Accuracy y Modelo Dummy

## Accuracy: la métrica más simple

```python
accuracy = (predicciones_correctas) / (total_predicciones)
```

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_val, y_pred)
print(f"Accuracy: {accuracy:.4f}")
```

## El problema con accuracy

Imagina un dataset donde solo el 10% de clientes hace churn:

```python
# Modelo "tonto" que siempre dice "no churn"
import numpy as np
y_pred_dummy = np.zeros(len(y_val))
accuracy_dummy = accuracy_score(y_val, y_pred_dummy)
print(f"Accuracy del modelo dummy: {accuracy_dummy:.4f}")  # ¡0.90!
```

Un modelo que **no hace nada** ya tiene 90% de accuracy. Esto se llama el **problema de clases desbalanceadas**.

## ¿Cuándo es útil accuracy?

- Cuando las clases están **balanceadas** (50/50 aprox.)
- Como una primera referencia rápida
- Para comparar con un baseline

## ¿Cuándo NO es suficiente?

- Datasets **desbalanceados** (churn, fraude, enfermedades raras)
- Cuando el **costo de los errores** no es igual
  - Falso negativo (no detectar churn) puede ser más costoso que falso positivo

## Conclusión

Accuracy es un punto de partida, pero necesitamos métricas más informativas para entender realmente cómo se comporta nuestro modelo.

---

**Siguiente**: [Matriz de Confusión](02-matriz-confusion.md)
