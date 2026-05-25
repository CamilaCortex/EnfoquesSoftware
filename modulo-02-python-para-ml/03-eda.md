# 2.3 Análisis Exploratorio de Datos (EDA)

## ¿Qué es EDA?

El Análisis Exploratorio de Datos es el primer paso práctico en cualquier proyecto de ML. Consiste en entender los datos antes de modelar: su distribución, relaciones y posibles problemas.

## Paso 1: Vista general

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('datos.csv')

# Dimensiones
print(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}")

# Tipos de datos
print(df.dtypes)

# Estadísticas básicas
df.describe()

# Valores faltantes
df.isnull().sum()
```

## Paso 2: Distribución de variables numéricas

```python
# Histograma de una variable
df['precio'].hist(bins=30)
plt.xlabel('Precio')
plt.ylabel('Frecuencia')
plt.title('Distribución de precios')
plt.show()

# Histogramas de todas las numéricas
df.hist(figsize=(12, 8), bins=30)
plt.tight_layout()
plt.show()
```

## Paso 3: Variables categóricas

```python
# Conteo de categorías
df['marca'].value_counts()

# Gráfico de barras
df['marca'].value_counts().head(10).plot(kind='bar')
plt.title('Top 10 marcas')
plt.show()
```

## Paso 4: Relaciones entre variables

```python
# Correlación entre numéricas
correlacion = df.select_dtypes(include='number').corr()

# Mapa de calor
plt.figure(figsize=(10, 8))
sns.heatmap(correlacion, annot=True, cmap='coolwarm', center=0)
plt.title('Matriz de correlación')
plt.show()

# Scatter plot
plt.scatter(df['kilometraje'], df['precio'], alpha=0.5)
plt.xlabel('Kilometraje')
plt.ylabel('Precio')
plt.show()
```

## Paso 5: Relación feature vs target

```python
# Boxplot: variable categórica vs numérica
sns.boxplot(x='marca', y='precio', data=df)
plt.xticks(rotation=45)
plt.show()

# Precio promedio por categoría
df.groupby('marca')['precio'].mean().sort_values().plot(kind='barh')
plt.show()
```

## Checklist de EDA

- [ ] ¿Cuántas filas y columnas hay?
- [ ] ¿Qué tipos de datos tiene cada columna?
- [ ] ¿Hay valores faltantes? ¿En qué proporción?
- [ ] ¿Cómo se distribuye el target?
- [ ] ¿Hay outliers evidentes?
- [ ] ¿Qué variables están más correlacionadas con el target?
- [ ] ¿Hay variables redundantes (alta correlación entre sí)?

## Decisiones que tomamos después del EDA

- Qué features usar
- Cómo tratar valores faltantes
- Si necesitamos transformar variables (log, normalización)
- Si hay categorías con muy pocos datos que se pueden agrupar

---

**Anterior**: [Pandas](02-pandas.md) | **Siguiente**: [Álgebra Lineal](04-algebra-lineal.md)
