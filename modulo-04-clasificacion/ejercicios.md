# Ejercicios - Módulo 4

## Ejercicio 1: Análisis de importancia

Usando el dataset de churn:

1. Calcula el risk ratio para la variable `internet_service`
2. Calcula la mutual information de las 5 variables categóricas principales
3. ¿Cuál es la variable numérica con mayor correlación con churn?
4. Basándote en tu análisis, ¿cuáles son las 5 variables más importantes?

## Ejercicio 2: Regresión logística básica

1. Entrena un modelo solo con variables numéricas
2. Calcula la accuracy en validación
3. ¿Supera al modelo dummy (predecir siempre "no churn")?

## Ejercicio 3: Modelo completo

1. Usa DictVectorizer para incluir variables categóricas y numéricas
2. Entrena regresión logística con todas las variables
3. Compara la accuracy con el modelo del ejercicio 2
4. ¿Cuántos features tiene el modelo después del encoding?

## Ejercicio 4: Interpretación

1. Lista los 10 coeficientes más grandes (positivos) del modelo
2. Lista los 10 coeficientes más negativos
3. ¿Qué tipo de contrato protege más contra el churn?
4. Elige un cliente del conjunto de validación y explica por qué el modelo lo clasifica como churn o no churn

## Ejercicio 5: Umbral

1. Calcula las predicciones con umbrales de 0.3, 0.4, 0.5, 0.6, 0.7
2. ¿Cómo cambia la accuracy con cada umbral?
3. ¿Qué umbral elegirías si el costo de perder un cliente es muy alto?
