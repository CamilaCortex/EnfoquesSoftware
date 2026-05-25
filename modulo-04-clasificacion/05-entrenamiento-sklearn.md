# 4.5 Entrenamiento con scikit-learn

## Entrenar el modelo

```python
from sklearn.linear_model import LogisticRegression

modelo = LogisticRegression(solver='liblinear', max_iter=1000)
modelo.fit(X_train, y_train)
```

## Predecir probabilidades

```python
# Probabilidades (lo que realmente calcula el modelo)
y_pred_proba = modelo.predict_proba(X_val)[:, 1]

# Primeros 10 resultados
for prob in y_pred_proba[:10]:
    print(f"P(churn) = {prob:.3f} → {'Churn' if prob >= 0.5 else 'No churn'}")
```

## Predecir clases directamente

```python
# Clases con umbral por defecto (0.5)
y_pred = modelo.predict(X_val)

# Accuracy simple
accuracy = (y_pred == y_val).mean()
print(f"Accuracy: {accuracy:.4f}")
```

## Cambiar el umbral

A veces 0.5 no es el mejor umbral. Depende del costo de los errores:

```python
# Umbral más bajo → capturamos más churners (pero más falsos positivos)
umbral = 0.3
y_pred_custom = (y_pred_proba >= umbral).astype(int)

accuracy_custom = (y_pred_custom == y_val).mean()
print(f"Accuracy con umbral {umbral}: {accuracy_custom:.4f}")
```

## Comparar con un modelo dummy

```python
from sklearn.dummy import DummyClassifier

# Modelo que siempre predice la clase mayoritaria
dummy = DummyClassifier(strategy='most_frequent')
dummy.fit(X_train, y_train)
y_pred_dummy = dummy.predict(X_val)

accuracy_dummy = (y_pred_dummy == y_val).mean()
print(f"Accuracy dummy: {accuracy_dummy:.4f}")
print(f"Accuracy logística: {accuracy:.4f}")
```

Si tu modelo no supera al dummy, algo está mal.

## Pipeline completo

```python
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

# 1. Encoding
dv = DictVectorizer(sparse=False)
train_dicts = df_train[categoricas + numericas].to_dict(orient='records')
X_train = dv.fit_transform(train_dicts)

val_dicts = df_val[categoricas + numericas].to_dict(orient='records')
X_val = dv.transform(val_dicts)

# 2. Entrenamiento
modelo = LogisticRegression(solver='liblinear', C=1.0, max_iter=1000)
modelo.fit(X_train, y_train)

# 3. Predicción
y_pred_proba = modelo.predict_proba(X_val)[:, 1]
y_pred = (y_pred_proba >= 0.5).astype(int)

# 4. Evaluación básica
accuracy = (y_pred == y_val).mean()
print(f"Accuracy: {accuracy:.4f}")
```

---

**Anterior**: [Regresión Logística](04-regresion-logistica.md) | **Siguiente**: [Interpretación](06-interpretacion.md)
