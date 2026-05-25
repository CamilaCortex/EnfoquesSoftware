# Ejercicios - Módulo 6

## Ejercicio 1: Árbol de decisión

1. Entrena un árbol con max_depth=3 y visualízalo
2. Entrena árboles con max_depth de 2 a 15
3. Grafica train AUC vs val AUC por profundidad
4. ¿A partir de qué profundidad hay overfitting?

## Ejercicio 2: Random Forest

1. Entrena un Random Forest con 100 árboles y max_depth=6
2. Compara su AUC con el mejor árbol individual
3. Prueba con 50, 100, 200 y 500 árboles. ¿Cuántos son suficientes?
4. Muestra los 10 features más importantes

## Ejercicio 3: XGBoost

1. Entrena un modelo XGBoost con parámetros por defecto
2. Usa early stopping con 20 rondas de paciencia
3. Prueba learning_rate de 0.01, 0.05, 0.1 y 0.3
4. ¿Cuál es la mejor combinación de depth y learning_rate?

## Ejercicio 4: Comparación final

1. Compara todos los modelos (logística, árbol, RF, XGBoost)
2. Usa cross-validation de 5 folds para cada uno
3. Crea una tabla con AUC medio ± std
4. Elige el modelo final y evalúa en test
5. ¿Cuánto mejoró vs. la regresión logística del módulo 4?
