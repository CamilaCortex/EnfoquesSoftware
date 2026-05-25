# Ejercicios - Módulo 5

## Ejercicio 1: Matriz de confusión

Usando el modelo de churn del módulo anterior:

1. Calcula la matriz de confusión con umbral 0.5
2. ¿Cuántos falsos negativos hay? ¿Qué significa en contexto de negocio?
3. Cambia el umbral a 0.3 y recalcula. ¿Qué cambió?

## Ejercicio 2: Precision y Recall

1. Calcula precision, recall y F1 con umbral 0.5
2. Grafica precision y recall para umbrales de 0.1 a 0.9
3. ¿En qué umbral se cruzan precision y recall?
4. Si el costo de perder un cliente es 5x más que el de contactar uno innecesariamente, ¿qué umbral elegirías?

## Ejercicio 3: Curva ROC

1. Grafica la curva ROC de tu modelo
2. Calcula el AUC
3. Entrena un DecisionTreeClassifier y compara su ROC con la regresión logística
4. ¿Cuál modelo tiene mejor AUC?

## Ejercicio 4: Validación cruzada

1. Realiza 5-fold cross-validation con regresión logística
2. Reporta AUC medio ± desviación estándar
3. Compara con un árbol de decisión (max_depth=5)
4. Compara con un Random Forest (n_estimators=100)
5. ¿Cuál modelo elegirías y por qué?

## Ejercicio 5: Tabla resumen

Crea una tabla final comparando todos los modelos:

| Modelo | AUC (CV) | Precision | Recall | F1 |
|--------|----------|-----------|--------|-----|
| Logística | ? | ? | ? | ? |
| Árbol | ? | ? | ? | ? |
| Random Forest | ? | ? | ? | ? |
