# 6.2 Algoritmo de Aprendizaje de Árboles

## ¿Cómo "aprende" un árbol?

El árbol se construye recursivamente eligiendo en cada nodo la **mejor pregunta** (split) que separe los datos.

## Criterio de split: Impureza

¿Cómo medir qué tan "buena" es una pregunta? Usando métricas de **impureza**:

### Gini (por defecto en scikit-learn)

```text
Gini = 1 - Σ(pᵢ²)
```

- Gini = 0 → nodo puro (todos de la misma clase)
- Gini = 0.5 → máxima impureza (50/50)

### Entropía

```text
Entropía = -Σ(pᵢ · log₂(pᵢ))
```

Ambas funcionan similar en la práctica.

## El algoritmo paso a paso

```text
1. Para cada feature y cada posible valor de corte:
   - Dividir datos en dos grupos
   - Calcular la impureza de cada grupo
   - Calcular la ganancia de información

2. Elegir el split con mayor ganancia

3. Repetir recursivamente en cada subgrupo

4. Parar cuando se cumple un criterio de parada
```

## Ejemplo numérico

```python
import numpy as np

# Datos: [ingreso, edad] → default (1) o no (0)
# Nodo actual: 100 muestras, 30 default, 70 no default
# Gini del nodo = 1 - (0.3² + 0.7²) = 1 - 0.58 = 0.42

# Si dividimos por ingreso > 40k:
#   Izquierda: 60 muestras (5 default, 55 no default)
#     Gini = 1 - (5/60)² - (55/60)² = 0.15
#   Derecha: 40 muestras (25 default, 15 no default)
#     Gini = 1 - (25/40)² - (15/40)² = 0.47

# Gini ponderado después del split:
# (60/100)*0.15 + (40/100)*0.47 = 0.09 + 0.19 = 0.28

# Ganancia = 0.42 - 0.28 = 0.14 (¡bueno!)
```

## Criterios de parada

Sin restricciones, el árbol crece hasta que cada hoja tenga una sola muestra (overfitting total). Necesitamos criterios de parada:

- **max_depth**: profundidad máxima del árbol
- **min_samples_split**: mínimo de muestras para hacer un split
- **min_samples_leaf**: mínimo de muestras en cada hoja

```python
arbol = DecisionTreeClassifier(
    max_depth=5,
    min_samples_split=10,
    min_samples_leaf=5,
    random_state=42
)
```

---

**Anterior**: [Árboles de Decisión](01-arboles-decision.md) | **Siguiente**: [Tuning de Árboles](03-tuning-arboles.md)
