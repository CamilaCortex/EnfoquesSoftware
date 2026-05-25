# 4.2 Preparación de Datos

## Carga y exploración

```python
import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')

# Normalizar nombres de columnas
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Ver tipos de datos
df.dtypes
```

## Limpiar el target

```python
# Convertir target a numérico (0/1)
df['churn'] = (df['churn'] == 'Yes').astype(int)

print(f"Tasa de churn: {df['churn'].mean():.2%}")
```

## Identificar tipos de variables

```python
# Numéricas
numericas = df.select_dtypes(include='number').columns.tolist()
numericas.remove('churn')  # Excluir target
print(f"Numéricas ({len(numericas)}): {numericas}")

# Categóricas
categoricas = df.select_dtypes(include='object').columns.tolist()
print(f"Categóricas ({len(categoricas)}): {categoricas}")
```

## Tratar variables problemáticas

```python
# A veces columnas numéricas vienen como texto
df['total_charges'] = pd.to_numeric(df['total_charges'], errors='coerce')

# Rellenar nulos
df['total_charges'] = df['total_charges'].fillna(0)
```

## Dividir en conjuntos

```python
from sklearn.model_selection import train_test_split

# 60% train, 20% val, 20% test
df_train_full, df_test = train_test_split(df, test_size=0.2, random_state=42)
df_train, df_val = train_test_split(df_train_full, test_size=0.25, random_state=42)

# Separar target
y_train = df_train['churn'].values
y_val = df_val['churn'].values
y_test = df_test['churn'].values

# Eliminar target de features
df_train = df_train.drop(columns=['churn'])
df_val = df_val.drop(columns=['churn'])
df_test = df_test.drop(columns=['churn'])

print(f"Train: {len(df_train)}, Val: {len(df_val)}, Test: {len(df_test)}")
```

## Verificar la distribución del target

Es importante que la proporción de churn sea similar en los tres conjuntos:

```python
print(f"Churn en train: {y_train.mean():.2%}")
print(f"Churn en val:   {y_val.mean():.2%}")
print(f"Churn en test:  {y_test.mean():.2%}")
```

---

**Anterior**: [Problema de Clasificación](01-problema-clasificacion.md) | **Siguiente**: [Importancia de Features](03-importancia-features.md)
