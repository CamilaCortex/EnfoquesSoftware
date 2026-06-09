"""
Métricas de Prometheus para monitoreo de la API.
"""

from prometheus_client import Counter, Histogram, Gauge, Info


# --- Info del modelo ---
model_info = Info(
    'model',
    'Información del modelo cargado'
)

# --- Contadores ---
predictions_total = Counter(
    'predictions_total',
    'Número total de predicciones realizadas',
    ['endpoint', 'status']
)

requests_total = Counter(
    'http_requests_total',
    'Número total de requests HTTP',
    ['method', 'endpoint', 'status_code']
)

# --- Histogramas ---
prediction_duration_seconds = Histogram(
    'prediction_duration_seconds',
    'Tiempo de inferencia del modelo en segundos',
    ['endpoint'],
    buckets=[0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5]
)

predicted_trip_duration_minutes = Histogram(
    'predicted_trip_duration_minutes',
    'Distribución de duraciones predichas (minutos)',
    buckets=[5, 10, 15, 20, 25, 30, 40, 50, 60, 90, 120]
)

trip_distance_histogram = Histogram(
    'trip_distance_miles',
    'Distribución de distancias de viajes recibidos (millas)',
    buckets=[0.5, 1, 2, 3, 5, 7, 10, 15, 20, 30, 50]
)

# --- Gauges ---
predictions_in_progress = Gauge(
    'predictions_in_progress',
    'Número de predicciones en proceso actualmente'
)

last_prediction_duration = Gauge(
    'last_prediction_duration_minutes',
    'Última duración predicha (minutos)'
)

batch_size_histogram = Histogram(
    'batch_size',
    'Tamaño de los batches recibidos',
    buckets=[1, 5, 10, 25, 50, 100, 250, 500, 1000]
)
