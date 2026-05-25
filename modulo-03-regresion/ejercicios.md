# Ejercicios - Módulo 3

## Ejercicio 1: Preparación de datos

Usando el dataset de precios de autos (`notebook.ipynb`):

1. Carga el dataset y muestra las primeras 5 filas
2. Identifica columnas con valores nulos y decide cómo tratarlos
3. Aplica transformación log al target (precio)
4. Divide en train (60%), validación (20%) y test (20%)

## Ejercicio 2: Regresión lineal

1. Entrena un modelo de regresión lineal con solo 2 features: `year` y `engine_hp`
2. Calcula el RMSE en validación
3. Agrega 3 features más y re-entrena. ¿Mejoró el RMSE?
4. Interpreta los 3 pesos más grandes del modelo

## Ejercicio 3: Feature engineering

1. Crea la variable `antiguedad = 2024 - year`
2. Aplica One-Hot Encoding a la columna `make` (marca)
3. Entrena un modelo con todas las features (numéricas + encoded)
4. Compara el RMSE con el modelo del ejercicio 2

## Ejercicio 4: Regularización

1. Entrena modelos Ridge con alpha = [0.001, 0.01, 0.1, 1, 10, 100]
2. Grafica alpha vs RMSE
3. ¿Cuál es el mejor alpha?
4. Entrena el modelo final (con el mejor alpha) usando train + val
5. Reporta el RMSE en test

## Ejercicio 5 (opcional): Comparación final

Crea una tabla resumen con todos tus modelos:

| Modelo | Features | RMSE val |
|--------|----------|----------|
| Baseline (media) | — | ? |
| Lineal (2 features) | year, hp | ? |
| Lineal (todas) | todas | ? |
| Ridge (mejor alpha) | todas | ? |
