# 4.1 El Problema de Clasificación

## ¿Qué es clasificación?

A diferencia de regresión (donde predecimos un número), en clasificación predecimos una **categoría**.

## Clasificación binaria

Dos posibles resultados:

- Spam / No spam
- Fraude / Legítimo
- **Churn / No churn** (nuestro proyecto)
- Enfermo / Sano

## Nuestro proyecto: Predicción de Churn

**Churn** = un cliente cancela el servicio.

¿Por qué importa? Porque es mucho más caro adquirir un cliente nuevo que retener uno existente. Si podemos predecir quién va a cancelar, podemos tomar acciones preventivas.

## El dataset

Datos de una empresa de telecomunicaciones con información sobre:

- Datos del cliente: género, antigüedad, tipo de contrato
- Servicios contratados: internet, teléfono, streaming
- Facturación: cargo mensual, cargo total
- **Target**: ¿canceló? (sí/no)

```python
import pandas as pd

df = pd.read_csv('data.csv')
print(f"Clientes: {df.shape[0]}")
print(f"Features: {df.shape[1]}")

# Distribución del target
print(df['churn'].value_counts(normalize=True))
```

## Formulación

```text
Features (X)                              Target (y)
──────────────────────────────────────    ──────────
contrato, antigüedad, cargo, servicios →  churn (0/1)
```

El modelo predice una **probabilidad** entre 0 y 1:

- P(churn) = 0.85 → muy probable que cancele
- P(churn) = 0.12 → probablemente se quede

Nosotros definimos un **umbral** (ej: 0.5) para tomar la decisión.

---

**Siguiente**: [Preparación de Datos](02-preparacion-datos.md)
