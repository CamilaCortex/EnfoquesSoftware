# 3.2 Preparación de Datos

## ¿Por qué preparar los datos?

Los datos reales siempre vienen "sucios": valores faltantes, formatos inconsistentes, columnas innecesarias. Antes de modelar, necesitamos limpiarlos.

## Paso 1: Exploración inicial

```python
import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')

# Vista general
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)
df.isnull().sum()
```

## Paso 2: Seleccionar columnas relevantes

```python
columnas = ['make', 'model', 'year', 'engine_hp', 'engine_cylinders',
            'transmission_type', 'vehicle_size', 'highway_mpg', 'city_mpg',
            'msrp']

df = df[columnas]
```

## Paso 3: Limpiar nombres de columnas

```python
# Normalizar nombres: minúsculas, sin espacios
df.columns = df.columns.str.lower().str.replace(' ', '_')
```

## Paso 4: Tratar valores faltantes

```python
# Ver proporción de nulos
print(df.isnull().mean().round(3))

# Estrategia: rellenar numéricos con 0 (o la mediana)
df['engine_hp'] = df['engine_hp'].fillna(0)
df['engine_cylinders'] = df['engine_cylinders'].fillna(0)
```

## Paso 5: Tratar el target

```python
# Distribución del precio
df['msrp'].describe()

# Aplicar log para normalizar distribución sesgada
df['log_price'] = np.log1p(df['msrp'])
```

¿Por qué `log`? Los precios suelen tener distribución sesgada a la derecha (muchos autos baratos, pocos caros). El log hace la distribución más simétrica, lo que ayuda a los modelos lineales.

## Paso 6: Dividir en train/val/test

```python
from sklearn.model_selection import train_test_split

# 60% train, 20% val, 20% test
df_train_full, df_test = train_test_split(df, test_size=0.2, random_state=42)
df_train, df_val = train_test_split(df_train_full, test_size=0.25, random_state=42)

print(f"Train: {len(df_train)}, Val: {len(df_val)}, Test: {len(df_test)}")

# Separar target
y_train = df_train['log_price'].values
y_val = df_val['log_price'].values
y_test = df_test['log_price'].values

# Eliminar target de features
del df_train['log_price'], df_train['msrp']
del df_val['log_price'], df_val['msrp']
del df_test['log_price'], df_test['msrp']
```

## Resumen del proceso

```text
Datos crudos
  → Seleccionar columnas
  → Limpiar nombres
  → Tratar nulos
  → Transformar target (log)
  → Dividir train/val/test
  → Listo para modelar
```

---

**Anterior**: [Problema de Regresión](01-problema-regresion.md) | **Siguiente**: [Regresión Lineal](03-regresion-lineal.md)
