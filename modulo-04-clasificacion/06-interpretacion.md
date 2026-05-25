# 4.6 Interpretación del Modelo

## Coeficientes del modelo

Cada feature tiene un peso (coeficiente) que indica su impacto en la predicción:

```python
# Ver coeficientes
feature_names = dv.get_feature_names_out()
coefs = modelo.coef_[0]

# Ordenar por importancia absoluta
importancia = pd.DataFrame({
    'feature': feature_names,
    'coef': coefs,
    'abs_coef': np.abs(coefs)
}).sort_values('abs_coef', ascending=False)

print(importancia.head(15))
```

## ¿Cómo interpretar los coeficientes?

- **Coeficiente positivo**: aumenta la probabilidad de churn
- **Coeficiente negativo**: disminuye la probabilidad de churn
- **Magnitud**: indica qué tan fuerte es el efecto

```python
# Top 10 features que AUMENTAN churn
print("Features que aumentan churn:")
print(importancia[importancia['coef'] > 0].head(10)[['feature', 'coef']])

# Top 10 features que DISMINUYEN churn
print("\nFeatures que disminuyen churn:")
print(importancia[importancia['coef'] < 0].head(10)[['feature', 'coef']])
```

## Ejemplo de interpretación

```text
contract=Month-to-month:  coef = +0.85  → contrato mensual AUMENTA riesgo
contract=Two year:         coef = -1.20  → contrato 2 años PROTEGE
tenure:                    coef = -0.03  → más antigüedad, menos churn
monthly_charges:           coef = +0.02  → cargo más alto, más churn
```

## Visualizar los coeficientes más importantes

```python
import matplotlib.pyplot as plt

top_n = 15
top_features = importancia.head(top_n)

colors = ['red' if c > 0 else 'blue' for c in top_features['coef']]
plt.barh(top_features['feature'], top_features['coef'], color=colors)
plt.xlabel('Coeficiente')
plt.title('Top features (rojo=aumenta churn, azul=protege)')
plt.tight_layout()
plt.show()
```

## Usar el modelo para un cliente específico

```python
# Datos de un cliente nuevo
cliente = {
    'contract': 'Month-to-month',
    'tenure': 3,
    'monthly_charges': 75.0,
    'internet_service': 'Fiber optic',
    'online_security': 'No',
    # ... otros features
}

# Predecir
X_cliente = dv.transform([cliente])
prob_churn = modelo.predict_proba(X_cliente)[0, 1]

print(f"Probabilidad de churn: {prob_churn:.1%}")
if prob_churn >= 0.5:
    print("ACCIÓN: Contactar al cliente con oferta de retención")
```

## Resumen

La regresión logística es un modelo **interpretable**: podemos explicar exactamente por qué clasifica a un cliente como potencial churn. Esto es valioso en contextos donde necesitamos justificar las decisiones del modelo.

---

**Anterior**: [Entrenamiento con sklearn](05-entrenamiento-sklearn.md) | **Volver al módulo**: [README](README.md)
