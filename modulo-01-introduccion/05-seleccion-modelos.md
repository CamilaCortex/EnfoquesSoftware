# 1.5 Selección de Modelos

## El problema

Existen muchos algoritmos de ML:

- Regresión lineal / logística
- Árboles de decisión
- Random Forest
- XGBoost
- Redes neuronales

¿Cómo elegimos el mejor para nuestro problema?

## Estrategia: Train / Validation / Test

Dividimos los datos en **tres conjuntos**:

```text
┌──────────────────────────────────────────────┐
│        Datos totales (100%)                  │
├────────────────────┬──────────┬──────────────┤
│  Entrenamiento     │Validación│    Test      │
│      (60%)         │  (20%)   │   (20%)      │
└────────────────────┴──────────┴──────────────┘
```

### ¿Para qué sirve cada uno?

- **Entrenamiento**: el modelo aprende de estos datos
- **Validación**: comparamos modelos y ajustamos hiperparámetros
- **Test**: evaluación final (solo se usa una vez)

## Proceso paso a paso

1. Dividir datos en train / validation / test
2. Entrenar varios modelos con datos de entrenamiento
3. Evaluar cada modelo con datos de validación
4. Seleccionar el mejor modelo
5. Evaluar el modelo elegido con datos de test
6. Verificar que el rendimiento sea consistente

## ¿Por qué necesitamos test?

**Problema de comparaciones múltiples**: si comparamos muchos modelos en validación, por azar uno puede obtener buen puntaje sin ser realmente bueno.

El conjunto de test actúa como un "juez imparcial" que solo ve los resultados una vez.

## Tip práctico

Después de seleccionar el mejor modelo, puedes combinar entrenamiento + validación para re-entrenar el modelo final antes de evaluarlo en test. Así aprovechas más datos.

```python
from sklearn.model_selection import train_test_split

# División típica: 60% train, 20% val, 20% test
X_train_full, X_test, y_train_full, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
X_train, X_val, y_train, y_val = train_test_split(
    X_train_full, y_train_full, test_size=0.25, random_state=42
)
```

---

**Anterior**: [CRISP-DM](04-crisp-dm.md) | **Siguiente**: [Configuración del Entorno](06-entorno.md)
