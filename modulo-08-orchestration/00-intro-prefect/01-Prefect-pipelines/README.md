# NYC Taxi Duration Prediction Pipeline

Pipeline de ML end-to-end para predecir la duración de viajes en taxi de Nueva York, usando **Prefect** para orquestación, **Optuna** para optimización de hiperparámetros, y **MLflow** para tracking y registro de modelos.

---

## 📋 Arquitectura del Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│                    PREFECT FLOW                                  │
│           NYC Taxi Duration Prediction Pipeline                  │
└─────────────────────────────────────────────────────────────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        ▼                       ▼                       ▼
┌──────────────┐      ┌────────────────┐      ┌──────────────────┐
│   1. LOAD    │      │  2. VALIDATE   │      │  3. FEATURES     │
│   DATA       │ ───► │     DATA       │ ───► │   ENGINEERING    │
│              │      │                │      │                  │
│ • Descarga   │      │ • Limpieza     │      │ • PU_DO feature  │
│   parquet    │      │ • Filtros      │      │ • DictVectorizer │
│ • Calcula    │      │ • Validación   │      │                  │
│   duration   │      │   calidad      │      │                  │
└──────────────┘      └────────────────┘      └──────────────────┘
                                                       │
        ┌──────────────────────────────────────────────┼──────────────┐
        ▼                                              ▼              │
┌──────────────────┐                          ┌──────────────────┐   │
│ 4. OPTIMIZATION  │                          │  VALIDATION DATA │   │
│    (Optuna)     │                          │  (mes siguiente) │   │
│                  │                          └──────────────────┘   │
│ • 20 trials      │                                                   │
│ • XGBoost        │                                                   │
│ • Best RMSE: 6.0 │◄──────────────────────────────────────────────────┘
└──────────────────┘
         │
         ▼
┌──────────────────┐
│ 5. TRAIN MODEL   │
│   (XGBoost)      │
│                  │
│ • Best params    │
│ • 30 rounds      │
│ • Early stopping │
└──────────────────┘
         │
         ▼
┌──────────────────┐
│ 6. REGISTER      │
│    (MLflow)      │
│                  │
│ • Model Registry │
│ • Version 1      │
│ • Production     │
└──────────────────┘
```

---

## 🧩 Componentes Principales

### 1. **Orquestación - Prefect**

- **Flow principal**: `duration_prediction_flow()`
- **Tasks individuales**: Cada paso es un task con retry logic y caching
- **Observabilidad**: Todos los runs se ven en Prefect Cloud
- **Scheduling**: Soporta programación automática

### 2. **Optimización - Optuna**

```python
# Hiperparámetros optimizados automáticamente:
- learning_rate: 0.1 - 0.5
- max_depth: 3 - 12
- min_child_weight: 1 - 10
- subsample: 0.5 - 1.0
- colsample_bytree: 0.5 - 1.0
- reg_alpha: 0 - 1
- reg_lambda: 0 - 1
```

**Funcionamiento:**
1. Optuna prueba 20 combinaciones diferentes (trials)
2. Cada trial entrena un XGBoost y mide RMSE
3. Selecciona los mejores hiperparámetros
4. Guarda el trial ganador en MLflow

### 3. **Tracking - MLflow**

**Experiment**: `nyc-taxi-experiment-prefect`

**Información guardada:**
- ✅ Métricas: RMSE de cada trial y modelo final
- ✅ Parámetros: Hiperparámetros optimizados
- ✅ Artifacts: Modelo XGBoost + DictVectorizer (preprocessor)
- ✅ Model Registry: Versionado y stage management

### 4. **Feature Engineering**

**Columnas originales:**
- `PULocationID`: Zona de pickup
- `DOLocationID`: Zona de dropoff
- `trip_distance`: Distancia del viaje

**Feature creada:**
- `PU_DO`: Combinación `PULocationID_DOLocationID` (categórica)

**Preprocesamiento:**
- DictVectorizer convierte features categóricas a one-hot encoding

---

## 🚀 Cómo Ejecutar

### Requisitos

```bash
# Instalar dependencias
uv pip install prefect mlflow optuna xgboost pandas scikit-learn

# O si usas requirements.txt
pip install -r requirements.txt
```

### Ejecución Básica

```bash
# Ejecutar con defaults (2025-01)
uv run python pipeline.py

# Ejecutar con parámetros específicos
uv run python pipeline.py --year 2024 --month 3

# Ejecutar para mes actual
uv run python pipeline.py --year 2026 --month 1
```

### Ver Resultados

```bash
# Iniciar MLflow UI
mlflow ui --backend-store-uri sqlite:///mlflow.db

# Abrir en navegador: http://localhost:5000
```

---

## 📊 Flujo de Datos Detallado

### Paso 1: Carga de Datos (`src/data/loaders.py`)

```python
@task(retries=3, retry_delay_seconds=[10, 30, 60])
def read_dataframe(year: int, month: int) -> pd.DataFrame:
    url = f'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_{year}-{month:02d}.parquet'
    df = pd.read_parquet(url)
    
    # Calcular duración en minutos
    df['duration'] = (df.lpep_dropoff_datetime - df.lpep_pickup_datetime).dt.total_seconds() / 60
    
    # Filtrar viajes de 1-60 minutos
    df = df[(df.duration >= 1) & (df.duration <= 60)]
    
    return df
```

**Features:**
- ✅ Retry automático (3 intentos con backoff exponencial)
- ✅ Caching (24 horas) - no descarga el mismo archivo repetido
- ✅ Artifact con resumen de datos

### Paso 2: Validación (`src/data/validators.py`)

- Verifica calidad mínima de datos
- Elimina outliers
- Valida que existan suficientes registros

### Paso 3: Feature Engineering (`src/features/engineering.py`)

```python
df_features['PU_DO'] = (
    df_features['PULocationID'].astype(str) + '_' + 
    df_features['DOLocationID'].astype(str)
)

# One-hot encoding con DictVectorizer
dicts = df_features[['PU_DO', 'trip_distance']].to_dict(orient='records')
X = DictVectorizer().fit_transform(dicts)
```

### Paso 4: Optimización (`src/models/optimization.py`)

```python
@task
def optimize_hyperparameters(X_train, y_train, X_val, y_val):
    def objective(trial):
        params = {
            'learning_rate': trial.suggest_float('learning_rate', 0.1, 0.5),
            'max_depth': trial.suggest_int('max_depth', 3, 12),
            # ... más parámetros
        }
        
        model = xgboost.train(params, dtrain)
        y_pred = model.predict(dval)
        return mean_squared_error(y_val, y_pred, squared=False)  # RMSE
    
    study = optuna.create_study(direction='minimize')
    study.optimize(objective, n_trials=20)
    
    return study.best_params  # Devuelve mejores hiperparámetros
```

### Paso 5: Entrenamiento Final

```python
model = xgboost.train(
    best_params,
    dtrain,
    num_boost_round=30,
    evals=[(dval, 'validation')],
    early_stopping_rounds=50
)
```

### Paso 6: Registro en MLflow (`src/models/model_registry.py`)

```python
@task
def register_best_model(run_id: str, rmse: float, model_name: str):
    # 1. Registrar modelo
    mlflow.register_model(f"runs:/{run_id}/models_mlflow", model_name)
    
    # 2. Agregar tags
    client.set_model_version_tag(name, version, "rmse", str(rmse))
    
    # 3. Promover a Production
    client.transition_model_version_stage(name, version, "Production")
    
    # 4. Guardar localmente
    download_model_artifacts(run_id, local_path)
```

---

## 🎯 Configuración

### Constantes Principales (`src/config/constants.py`)

```python
# Período por defecto
DEFAULT_YEAR = 2025
DEFAULT_MONTH = 1

# Calidad de datos
MIN_DURATION = 1          # mínimo 1 minuto
MAX_DURATION = 60         # máximo 60 minutos
MIN_RECORDS = 1000        # mínimo 1000 registros

# Optimización
OPTUNA_TRIALS = 20        # número de trials
NUM_BOOST_ROUNDS = 30     # iteraciones XGBoost
EARLY_STOPPING_ROUNDS = 50

# Features
CATEGORICAL_FEATURES = ['PULocationID', 'DOLocationID']
TARGET_COLUMN = 'duration'
```

---

## 📈 Métricas y Resultados

### Métricas de Éxito

| Métrica | Valor Objetivo | Descripción |
|---------|----------------|-------------|
| **RMSE** | < 6.5 minutos | Error promedio en predicción de duración |
| **R²** | > 0.7 | Qué tan bien explica el modelo la varianza |

### Resultado Típico

```
Best trial: trial_7
Best RMSE: 6.0039
Best parameters:
  - learning_rate: 0.296
  - max_depth: 10
  - min_child_weight: 2.527
  - subsample: 0.631
  - colsample_bytree: 0.747

Final model RMSE: 6.08
Model registered: nyc-taxi-duration-predictor v1 (Production)
```

---

## 🛠️ Estructura de Archivos

```
01-Prefect-pipelines/
├── pipeline.py                     # Entry point - Flow principal
├── README.md                       # Este documento
├── README_MODEL_REGISTRY.md        # Docs específicas del Model Registry
├── mlflow.db                       # Base de datos SQLite de MLflow
├── data/                           # Datos descargados (CSV backups)
├── models/                         # Modelos guardados localmente
│   └── registered/
│       └── v1_20260602_174853/     # Versión 1 del modelo
├── src/
│   ├── config/
│   │   ├── constants.py            # Configuración y constantes
│   │   ├── mlflow_setup.py         # Inicialización de MLflow
│   │   └── __init__.py
│   ├── data/
│   │   ├── loaders.py              # Descarga y carga de datos
│   │   ├── validators.py           # Validación de calidad
│   │   ├── utils.py                # Utilidades (calculate_next_period)
│   │   └── __init__.py
│   ├── features/
│   │   ├── engineering.py          # Feature engineering (PU_DO)
│   │   └── __init__.py
│   └── models/
│       ├── optimization.py         # Optuna hyperparameter tuning
│       ├── model_registry.py       # MLflow Model Registry integration
│       └── __init__.py
```

---

## 🔍 Debugging Común

### Error: `KeyError("['PU_DO'] not in index")`

**Causa**: La columna `PU_DO` no existe en los datos originales, se crea en feature engineering.

**Fix**: Asegurar que `CATEGORICAL_FEATURES` en `constants.py` use las columnas originales:
```python
CATEGORICAL_FEATURES = ['PULocationID', 'DOLocationID']  # ✅ Correcto
# NO: ['PU_DO', ...]  ❌ Incorrecto
```

### Error: Datos no disponibles para fecha futura

**Causa**: NYC Taxi publica datos con ~2 meses de delay.

**Fix**: Usar fechas históricas disponibles:
```bash
# Fechas seguras
--year 2024 --month 3
--year 2025 --month 1
```

---

## 🚀 Siguientes Pasos

### 1. Promover Modelo a Production
```bash
# Automático - el pipeline ya lo hace
# Ver en MLflow UI: http://localhost:5000
```

### 2. Hacer Predicciones
```python
import mlflow
import pandas as pd

# Cargar modelo desde Production
model = mlflow.xgboost.load_model("models:/nyc-taxi-duration-predictor/Production")

# Preparar datos nuevos
data = pd.DataFrame({
    'PULocationID': ['132'],
    'DOLocationID': ['138'],
    'trip_distance': [2.5]
})

# Predecir
prediction = model.predict(data)
print(f"Duración estimada: {prediction[0]:.2f} minutos")
```

### 3. Programar Ejecución Automática
```python
# En pipeline.py o prefect.yaml
fetch_weather.deploy(
    name="monthly-training",
    cron="0 0 1 * *",  # Primer día de cada mes
)
```

---

## 📚 Referencias

- **Prefect**: https://docs.prefect.io/
- **MLflow**: https://mlflow.org/docs/latest/index.html
- **Optuna**: https://optuna.readthedocs.io/
- **XGBoost**: https://xgboost.readthedocs.io/
- **NYC Taxi Data**: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

---

## 👨‍💻 Autor

Pipeline desarrollado para el curso **Machine Learning con enfoques de Software Engineering** - Módulo 8: Orchestration

---

## 📝 Changelog

- **v1.0** (2026-06-02): Pipeline funcional con Prefect + Optuna + MLflow Model Registry
- **Fix**: Corregido bug de `PU_DO` en constantes
- **Feature**: Auto-promoción a Production después de registro
