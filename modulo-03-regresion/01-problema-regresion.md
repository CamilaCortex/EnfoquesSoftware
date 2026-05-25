# 3.1 El Problema de Regresión

## ¿Qué es regresión?

Un problema de regresión busca predecir un **valor numérico continuo**. A diferencia de clasificación (donde predecimos categorías), aquí predecimos cantidades.

## Ejemplos

- Predecir el **precio** de una casa
- Estimar el **salario** según años de experiencia
- Calcular el **tiempo de entrega** de un pedido
- Predecir la **temperatura** de mañana

## Nuestro proyecto: Precio de autos

Vamos a predecir el precio de autos usados basándonos en sus características:

- Marca y modelo
- Año de fabricación
- Kilometraje
- Tipo de motor y combustible
- Potencia (HP)

## El dataset

```python
import pandas as pd

df = pd.read_csv('data.csv')
print(f"Observaciones: {df.shape[0]}")
print(f"Features: {df.shape[1]}")
df.head()
```

## Formulación del problema

```text
Features (X)                    Target (y)
─────────────────────────────   ──────────
año, km, marca, motor, hp  →   precio
```

Queremos encontrar una función `g` tal que:

```text
g(año, km, marca, motor, hp) ≈ precio
```

## Plan de trabajo

1. Explorar y preparar los datos
2. Construir un modelo baseline (simple)
3. Medir qué tan bueno es
4. Mejorar el modelo iterativamente

---

**Siguiente**: [Preparación de Datos](02-preparacion-datos.md)
