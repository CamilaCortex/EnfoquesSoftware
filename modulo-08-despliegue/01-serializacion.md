# 7.1 Serialización de Modelos

## ¿Qué es serialización?

Es el proceso de **guardar un modelo entrenado en disco** para poder usarlo después sin re-entrenar.

## ¿Por qué es necesario?

```text
Entrenamiento (notebook) → Guardar modelo → Cargar en producción (API)
```

Sin serialización, tendrías que re-entrenar el modelo cada vez que reinicies el servidor.

## Con joblib (recomendado para scikit-learn)

```python
import joblib

# Guardar
joblib.dump(modelo, 'modelo_churn.joblib')
joblib.dump(dv, 'vectorizer.joblib')

# Cargar
modelo = joblib.load('modelo_churn.joblib')
dv = joblib.load('vectorizer.joblib')
```

## Con pickle (alternativa estándar)

```python
import pickle

# Guardar
with open('modelo_churn.pkl', 'wb') as f:
    pickle.dump((modelo, dv), f)

# Cargar
with open('modelo_churn.pkl', 'rb') as f:
    modelo, dv = pickle.load(f)
```

## Para XGBoost

```python
import xgboost as xgb

# Guardar (formato nativo, más eficiente)
modelo.save_model('modelo_xgb.json')

# Cargar
modelo = xgb.Booster()
modelo.load_model('modelo_xgb.json')
```

## Verificar que funciona

```python
# Después de cargar, hacer una predicción de prueba
cliente_test = {
    'contract': 'Month-to-month',
    'tenure': 3,
    'monthly_charges': 75.0,
}

X_test = dv.transform([cliente_test])
prob = modelo.predict_proba(X_test)[0, 1]
print(f"Probabilidad de churn: {prob:.3f}")
```

## Buenas prácticas

- Guarda **todo lo necesario** para predecir (modelo + vectorizer + scaler, etc.)
- Usa nombres descriptivos con versión: `modelo_churn_v1.joblib`
- Incluye los archivos del modelo en tu repositorio o en un almacenamiento dedicado
- Documenta qué features espera el modelo

---

**Siguiente**: [Introducción a FastAPI](02-fastapi-intro.md)
