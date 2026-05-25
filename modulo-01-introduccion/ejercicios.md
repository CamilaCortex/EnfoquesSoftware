# Ejercicios - Módulo 1

## Ejercicio 1: Identificar problemas de ML

Para cada escenario, indica si usarías ML o un sistema basado en reglas. Justifica tu respuesta.

1. Calcular el IVA de una factura
2. Detectar transacciones fraudulentas en tarjetas de crédito
3. Clasificar emails como urgentes o no urgentes
4. Convertir temperaturas de Celsius a Fahrenheit
5. Predecir qué productos comprará un cliente

## Ejercicio 2: Clasificar problemas supervisados

Indica si cada problema es de **regresión** o **clasificación** (binaria/multiclase):

1. Predecir el salario de un empleado según su experiencia
2. Determinar si un paciente tiene diabetes o no
3. Estimar el tiempo de entrega de un paquete
4. Clasificar imágenes de frutas (manzana, banana, naranja)
5. Predecir la nota final de un estudiante (0-100)

## Ejercicio 3: CRISP-DM aplicado

Elige un problema de ML que te interese (ej: predecir cancelaciones de suscripción) y describe brevemente qué harías en cada fase de CRISP-DM:

1. Comprensión del negocio
2. Comprensión de los datos
3. Preparación de los datos
4. Modelado
5. Evaluación
6. Despliegue

## Ejercicio 4: Configuración del entorno

1. Instala `uv` en tu sistema
2. Ejecuta `uv sync` en la raíz del repositorio
3. Abre un notebook de Jupyter y ejecuta:

```python
import numpy as np
import pandas as pd
import sklearn

print(f"NumPy: {np.__version__}")
print(f"Pandas: {pd.__version__}")
print(f"Scikit-learn: {sklearn.__version__}")
print("¡Entorno configurado correctamente!")
```

4. Toma una captura de pantalla del resultado como evidencia.
