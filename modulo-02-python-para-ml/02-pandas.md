# 2.2 Pandas: Manipulación de Datos

## ¿Qué es Pandas?

Pandas es la librería principal para manipular datos tabulares en Python. Trabaja con **DataFrames** (tablas) y **Series** (columnas).

## Cargar datos

```python
import pandas as pd

# Desde CSV
df = pd.read_csv('datos.csv')

# Desde URL
url = 'https://raw.githubusercontent.com/..../data.csv'
df = pd.read_csv(url)

# Exploración rápida
df.head()          # Primeras 5 filas
df.shape           # (filas, columnas)
df.dtypes          # Tipos de cada columna
df.describe()      # Estadísticas básicas
df.info()          # Resumen del DataFrame
```

## Seleccionar datos

```python
# Una columna (devuelve Series)
df['precio']

# Varias columnas (devuelve DataFrame)
df[['precio', 'marca']]

# Filtrar filas
df[df['precio'] > 10000]
df[df['marca'] == 'Toyota']

# Combinar filtros
df[(df['precio'] > 10000) & (df['año'] >= 2020)]
```

## Valores faltantes

```python
# Detectar
df.isnull().sum()          # Cuenta nulos por columna

# Eliminar filas con nulos
df.dropna()

# Rellenar con un valor
df['columna'].fillna(0)
df['columna'].fillna(df['columna'].mean())
```

## Transformaciones comunes

```python
# Crear columna nueva
df['precio_miles'] = df['precio'] / 1000

# Aplicar función
df['marca_lower'] = df['marca'].str.lower()

# Renombrar columnas
df = df.rename(columns={'old_name': 'new_name'})

# Eliminar columnas
df = df.drop(columns=['columna_innecesaria'])
```

## Agrupaciones

```python
# Precio promedio por marca
df.groupby('marca')['precio'].mean()

# Múltiples agregaciones
df.groupby('marca').agg({
    'precio': ['mean', 'median', 'count'],
    'kilometraje': 'mean'
})
```

## Ordenar

```python
# Por una columna
df.sort_values('precio', ascending=False)

# Por múltiples columnas
df.sort_values(['marca', 'precio'])
```

## Exportar

```python
df.to_csv('resultado.csv', index=False)
```

---

**Anterior**: [NumPy](01-numpy.md) | **Siguiente**: [EDA](03-eda.md)
