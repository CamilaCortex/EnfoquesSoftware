# Módulo 8: Proyecto Integrador

> **Objetivo**: Aplicar todo lo aprendido en el curso en un proyecto completo de Machine Learning, desde la definición del problema hasta el despliegue como servicio dockerizado.

---

## Descripción

El proyecto integrador es tu oportunidad de demostrar que dominas el flujo completo de ML. Elegirás un dataset, construirás un modelo y lo desplegarás como un servicio funcional.

## Entregables

1. **Notebook de análisis** (`notebook.ipynb`)
   - EDA completo
   - Preparación de datos
   - Entrenamiento y comparación de modelos
   - Selección del modelo final

2. **Servicio de predicción** (`servicio/`)
   - `main.py` con la API en FastAPI
   - Modelo serializado
   - `Dockerfile` funcional
   - Script de pruebas

3. **Documentación** (`README.md`)
   - Descripción del problema
   - Dataset utilizado
   - Resultados obtenidos
   - Instrucciones para ejecutar

## Estructura esperada

```text
proyecto/
├── README.md
├── notebook.ipynb
├── servicio/
│   ├── main.py
│   ├── modelo.joblib
│   ├── vectorizer.joblib
│   ├── Dockerfile
│   ├── pyproject.toml
│   └── test_api.py
└── data/
    └── dataset.csv (o instrucciones para descargarlo)
```

---

## Guía paso a paso

### Paso 1: Elegir un problema y dataset

Elige un dataset de clasificación binaria. Sugerencias:

- Predicción de diabetes
- Detección de fraude en tarjetas
- Aprobación de préstamos
- Predicción de satisfacción del cliente
- Detección de spam

Fuentes: [Kaggle](https://www.kaggle.com/datasets), [UCI ML Repository](https://archive.ics.uci.edu/ml/index.php)

### Paso 2: EDA y preparación (Módulos 2-3)

- Explorar el dataset (dimensiones, tipos, nulos)
- Visualizar distribuciones y correlaciones
- Limpiar y preparar datos
- Dividir en train/val/test

### Paso 3: Modelado (Módulos 3-6)

- Establecer un baseline
- Entrenar al menos 3 modelos diferentes
- Hacer feature engineering
- Tuning de hiperparámetros
- Seleccionar el mejor modelo

### Paso 4: Evaluación (Módulo 5)

- Reportar métricas completas (AUC, precision, recall, F1)
- Mostrar matriz de confusión
- Validación cruzada
- Evaluar en test

### Paso 5: Despliegue (Módulo 7)

- Serializar el modelo final
- Crear la API con FastAPI
- Dockerizar el servicio
- Probar que funciona

---

## Rúbrica de evaluación

| Criterio | Peso | Excelente | Aceptable | Insuficiente |
|----------|------|-----------|-----------|--------------|
| EDA | 15% | Análisis completo con insights | EDA básico | Sin EDA |
| Preparación | 15% | Datos bien tratados, feature eng. | Limpieza básica | Datos crudos |
| Modelado | 25% | 3+ modelos, tuning, comparación | 2 modelos | Solo 1 modelo |
| Evaluación | 15% | Múltiples métricas, CV, análisis | Métricas básicas | Solo accuracy |
| Despliegue | 20% | Docker + FastAPI funcionando | API sin Docker | Sin despliegue |
| Documentación | 10% | README claro, reproducible | README parcial | Sin README |

## Fecha de entrega

Definida por el docente. El proyecto se presenta funcionando (demo del servicio dockerizado).

---

## Ideas de proyecto

### Nivel básico

- Predicción de supervivencia en Titanic
- Clasificación de flores (Iris multiclase)

### Nivel intermedio

- Predicción de churn en telecomunicaciones (diferente al del curso)
- Aprobación de crédito
- Predicción de diabetes

### Nivel avanzado

- Detección de fraude (dataset desbalanceado)
- Predicción de abandono universitario
- Scoring de riesgo con datos financieros
