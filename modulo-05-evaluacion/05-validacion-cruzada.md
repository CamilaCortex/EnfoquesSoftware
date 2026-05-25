# 5.5 Validación Cruzada

## El problema

Con un solo split train/validation, el resultado depende de **qué datos cayeron en cada conjunto**. Podríamos tener suerte o mala suerte.

## Solución: K-Fold Cross-Validation

Dividimos los datos en K partes (folds). Entrenamos K veces, cada vez usando un fold diferente como validación:

```text
Fold 1: [VAL][Train][Train][Train][Train]
Fold 2: [Train][VAL][Train][Train][Train]
Fold 3: [Train][Train][VAL][Train][Train]
Fold 4: [Train][Train][Train][VAL][Train]
Fold 5: [Train][Train][Train][Train][VAL]
```

El resultado final es el **promedio** de las K evaluaciones.

## Implementación

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

modelo = LogisticRegression(solver='liblinear', max_iter=1000)

# 5-fold cross-validation con AUC como métrica
scores = cross_val_score(modelo, X_train_full, y_train_full,
                         cv=5, scoring='roc_auc')

print(f"AUC por fold: {scores}")
print(f"AUC promedio: {scores.mean():.4f} ± {scores.std():.4f}")
```

## ¿Cuántos folds usar?

- **K=5 o K=10** son los más comunes
- K pequeño (3-5): más rápido, más varianza
- K grande (10-20): más lento, menos varianza
- K=N (Leave-One-Out): muy lento, solo para datasets pequeños

## Comparar modelos con cross-validation

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

modelos = {
    'Logística': LogisticRegression(solver='liblinear', max_iter=1000),
    'Árbol (depth=5)': DecisionTreeClassifier(max_depth=5),
    'Random Forest': RandomForestClassifier(n_estimators=100, max_depth=5),
}

print(f"{'Modelo':<20} {'AUC medio':>10} {'± Std':>8}")
print("-" * 40)

for nombre, modelo in modelos.items():
    scores = cross_val_score(modelo, X_train_full, y_train_full,
                             cv=5, scoring='roc_auc')
    print(f"{nombre:<20} {scores.mean():>10.4f} {scores.std():>8.4f}")
```

## Ventajas de cross-validation

- Resultado más **robusto** (no depende de un solo split)
- Usa **todos los datos** para entrenar y validar
- Permite detectar **overfitting** (alta varianza entre folds)

## Flujo completo recomendado

```text
1. Cross-validation para seleccionar modelo e hiperparámetros
2. Entrenar modelo final con TODOS los datos de train
3. Evaluar UNA VEZ en test
```

---

**Anterior**: [ROC y AUC](04-roc-auc.md) | **Volver al módulo**: [README](README.md)
