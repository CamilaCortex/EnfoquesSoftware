# 4.3 Importancia de Features

## ¿Por qué analizar la importancia?

Antes de entrenar un modelo, queremos saber qué variables tienen más relación con el target. Esto nos ayuda a:

- Entender el problema
- Seleccionar las mejores variables
- Detectar posibles problemas en los datos

## Método 1: Tasa de churn por categoría (Risk Ratio)

Para variables categóricas, comparamos la tasa de churn en cada grupo:

```python
# Tasa global de churn
tasa_global = y_train.mean()

# Tasa por tipo de contrato
for contrato in df_train['contract'].unique():
    mask = df_train['contract'] == contrato
    tasa = y_train[mask].mean()
    risk_ratio = tasa / tasa_global
    print(f"{contrato}: tasa={tasa:.2%}, risk_ratio={risk_ratio:.2f}")
```

**Interpretación del Risk Ratio:**
- RR > 1 → el grupo tiene más churn que el promedio
- RR < 1 → el grupo tiene menos churn
- RR ≈ 1 → no hay diferencia significativa

## Método 2: Correlación (variables numéricas)

```python
# Correlación de cada feature numérico con el target
correlaciones = df_train[numericas].corrwith(
    pd.Series(y_train, index=df_train.index)
)
print(correlaciones.sort_values())
```

- Correlación positiva: a mayor valor del feature, más churn
- Correlación negativa: a mayor valor del feature, menos churn
- Cerca de 0: poca relación lineal

## Método 3: Información Mutua (Mutual Information)

Mide cuánta información aporta un feature sobre el target. Funciona tanto para categóricas como numéricas.

```python
from sklearn.metrics import mutual_info_score

def mutual_info_churn(serie):
    return mutual_info_score(serie, y_train)

# Para variables categóricas
mi_scores = df_train[categoricas].apply(mutual_info_churn)
print(mi_scores.sort_values(ascending=False))
```

**Interpretación:**
- MI alto → el feature es muy informativo
- MI ≈ 0 → el feature no aporta información útil

## Resumen visual

```python
import matplotlib.pyplot as plt

# Top features por mutual information
mi_scores.sort_values(ascending=True).plot(kind='barh')
plt.xlabel('Mutual Information')
plt.title('Importancia de features categóricos')
plt.show()
```

## ¿Qué hacer con esta información?

- **Features con alta importancia**: incluir siempre en el modelo
- **Features con importancia nula**: candidatos a eliminar
- **Features redundantes**: si dos están muy correlacionados entre sí, quizás sobra uno

---

**Anterior**: [Preparación de Datos](02-preparacion-datos.md) | **Siguiente**: [Regresión Logística](04-regresion-logistica.md)
