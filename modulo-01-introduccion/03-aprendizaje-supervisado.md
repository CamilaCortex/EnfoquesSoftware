# 1.3 Aprendizaje Supervisado

## ¿Qué es?

En el aprendizaje supervisado, el modelo aprende a partir de ejemplos **etiquetados**: datos donde ya conocemos la respuesta correcta (target).

## Representación matemática

- **X** (matriz de features): cada fila es una observación, cada columna es un feature
- **y** (vector target): el valor que queremos predecir para cada observación
- **g** (modelo): una función que aprende a mapear X → y

```
g(X) ≈ y
```

El proceso de encontrar la función **g** se llama **entrenamiento**.

## Tipos de problemas supervisados

### Regresión

El target es un **número continuo**.

- Predecir el precio de una casa
- Estimar la temperatura de mañana
- Calcular el tiempo de entrega

### Clasificación

El target es una **categoría**.

- **Binaria**: spam / no spam, fraude / legítimo
- **Multiclase**: tipo de flor (setosa, versicolor, virginica)

### Ranking

El target es un **orden o puntuación** (usado en sistemas de recomendación).

## Flujo de trabajo

```
1. Recopilar datos etiquetados (X, y)
2. Dividir en entrenamiento y prueba
3. Entrenar el modelo con datos de entrenamiento
4. Evaluar con datos de prueba
5. Usar el modelo para predecir datos nuevos
```

## Ejemplo concreto

| Km | Año | Marca | Precio (target) |
|----|-----|-------|-----------------|
| 50000 | 2019 | Toyota | $15,000 |
| 120000 | 2015 | Ford | $8,000 |
| 30000 | 2021 | Honda | $20,000 |

El modelo aprende la relación entre (Km, Año, Marca) y Precio.

---

**Anterior**: [ML vs. Reglas](02-ml-vs-reglas.md) | **Siguiente**: [CRISP-DM](04-crisp-dm.md)
