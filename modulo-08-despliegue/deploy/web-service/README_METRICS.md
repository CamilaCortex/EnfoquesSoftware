# Métricas de Prometheus - NYC Taxi API

## Tabla de Contenidos
1. [Tipos de Métricas en Prometheus](#tipos-de-métricas-en-prometheus)
2. [Métricas de la API](#métricas-de-la-api)
3. [Métricas Automáticas de Python](#métricas-automáticas-de-python)
4. [Cómo Acceder](#cómo-acceder)
5. [Ejemplos de Consultas PromQL](#ejemplos-de-consultas-promql)

---

## Tipos de Métricas en Prometheus

Prometheus define 4 tipos de métricas. Cada una sirve para un propósito diferente:

### Counter (Contador)

- **Solo sube**, nunca baja (o se resetea a 0 al reiniciar)
- Ideal para contar eventos acumulados
- Ejemplo: "total de predicciones realizadas"

```
predictions_total{endpoint="/predict", status="success"} 150.0
```

**Analogía:** El odómetro de un carro. Solo sube. Si quieres saber "cuántas predicciones por minuto", Prometheus calcula la **tasa de cambio** (`rate()`).

---

### Gauge (Indicador)

- **Sube y baja** libremente
- Ideal para valores instantáneos que fluctúan
- Ejemplo: "predicciones en proceso ahora mismo"

```
predictions_in_progress 3.0
```

**Analogía:** El velocímetro de un carro. Puede subir o bajar en cualquier momento.

---

### Histogram (Histograma)

- Mide la **distribución** de valores en rangos (buckets)
- Cada bucket cuenta cuántas observaciones cayeron en ese rango o menos (`le` = less or equal)
- Incluye automáticamente `_count` (total observaciones) y `_sum` (suma total)
- Ideal para latencias, duraciones, tamaños

```
prediction_duration_seconds_bucket{le="0.01"} 45.0   ← 45 predicciones tardaron ≤10ms
prediction_duration_seconds_bucket{le="0.05"} 48.0   ← 48 tardaron ≤50ms
prediction_duration_seconds_bucket{le="0.1"}  50.0   ← 50 tardaron ≤100ms
prediction_duration_seconds_bucket{le="+Inf"} 50.0   ← total (siempre = count)
prediction_duration_seconds_count 50.0               ← 50 observaciones
prediction_duration_seconds_sum 1.25                 ← suma total = 1.25 seg
```

**Analogía:** Un formulario donde marcas en qué rango de edad estás. Prometheus sabe cuántos cayeron en cada "cajón".

**Promedio:** `sum / count` = 1.25 / 50 = 0.025 seg promedio por predicción.

---

### Info

- Metadata estática que no cambia (a menos que redespliegues)
- Expone labels con información del sistema

```
model_info{name="nyc-taxi-duration-predictor", version="2", rmse="5.8866"} 1.0
```

---

### Resumen de Tipos

| Tipo | ¿Sube y baja? | Uso típico | Ejemplo |
|------|--------------|------------|---------|
| **Counter** | Solo sube | Contar eventos | Requests, errores, predicciones |
| **Gauge** | Sube y baja | Valores instantáneos | Temperatura, concurrencia, último valor |
| **Histogram** | Acumula en buckets | Distribuciones | Latencia, duración, tamaño |
| **Info** | Estático | Metadata | Versión del modelo, nombre |

---

## Métricas de la API

### `model_info` (Info)

```
model_info{name="nyc-taxi-duration-predictor", rmse="5.8866", version="2"} 1.0
```

**¿Qué mide?** Información del modelo desplegado.

**¿Para qué sirve?** Saber en todo momento qué versión del modelo está en producción. Si despliegas un modelo nuevo, esta métrica cambia y puedes correlacionar con cambios en rendimiento.

---

### `predictions_total` (Counter)

```
predictions_total{endpoint="/predict", status="success"} 150.0
predictions_total{endpoint="/predict", status="error"} 2.0
predictions_total{endpoint="/predict/batch", status="success"} 500.0
```

**¿Qué mide?** Número acumulado de predicciones realizadas.

**Labels:**
- `endpoint`: `/predict` (individual) o `/predict/batch`
- `status`: `success` o `error`

**¿Para qué sirve?**
- Saber el volumen de uso de la API
- Calcular tasa de predicciones por segundo: `rate(predictions_total[5m])`
- Detectar errores: si `status="error"` sube, algo está mal

---

### `http_requests_total` (Counter)

```
http_requests_total{method="POST", endpoint="/predict", status_code="200"} 150.0
http_requests_total{method="POST", endpoint="/predict", status_code="500"} 2.0
```

**¿Qué mide?** Número total de requests HTTP recibidos.

**Labels:**
- `method`: GET, POST
- `endpoint`: ruta del endpoint
- `status_code`: código HTTP de respuesta

**¿Para qué sirve?**
- Monitorear tráfico HTTP
- Alertar si hay muchos 500 (errores de servidor)
- Diferencia con `predictions_total`: un request batch = 1 HTTP request, pero N predicciones

---

### `prediction_duration_seconds` (Histogram)

```
prediction_duration_seconds_bucket{endpoint="/predict", le="0.01"} 95.0
prediction_duration_seconds_bucket{endpoint="/predict", le="0.025"} 98.0
prediction_duration_seconds_bucket{endpoint="/predict", le="0.05"} 100.0
prediction_duration_seconds_sum{endpoint="/predict"} 0.85
prediction_duration_seconds_count{endpoint="/predict"} 100.0
```

**¿Qué mide?** Tiempo que tarda el modelo en hacer la inferencia (en segundos).

**Buckets:** 10ms, 25ms, 50ms, 100ms, 250ms, 500ms, 1s, 2.5s

**¿Para qué sirve?**
- Detectar degradación de rendimiento
- Saber el percentil 95 de latencia
- Alertar si las predicciones tardan más de X segundos

---

### `predicted_trip_duration_minutes` (Histogram)

```
predicted_trip_duration_minutes_bucket{le="10.0"} 20.0
predicted_trip_duration_minutes_bucket{le="20.0"} 65.0
predicted_trip_duration_minutes_bucket{le="30.0"} 90.0
predicted_trip_duration_minutes_bucket{le="60.0"} 98.0
```

**¿Qué mide?** Distribución de las duraciones que el modelo predice (en minutos).

**Buckets:** 5, 10, 15, 20, 25, 30, 40, 50, 60, 90, 120 min

**¿Para qué sirve?**
- Detectar data drift: si de repente el modelo predice tiempos muy diferentes a lo usual
- Entender el perfil de los viajes que llegan
- Alertar si hay predicciones anómalas (>120 min)

---

### `trip_distance_miles` (Histogram)

```
trip_distance_miles_bucket{le="3.0"} 40.0
trip_distance_miles_bucket{le="5.0"} 70.0
trip_distance_miles_bucket{le="10.0"} 90.0
```

**¿Qué mide?** Distribución de las distancias de viaje que llegan como input.

**Buckets:** 0.5, 1, 2, 3, 5, 7, 10, 15, 20, 30, 50 millas

**¿Para qué sirve?**
- Detectar data drift en los inputs
- Si de repente llegan muchos viajes de 50 millas (inusual para NYC), algo cambió
- Comparar con la distribución de entrenamiento

---

### `predictions_in_progress` (Gauge)

```
predictions_in_progress 0.0
```

**¿Qué mide?** Número de predicciones que se están procesando en este instante.

**¿Para qué sirve?**
- Monitorear concurrencia
- Si este número se mantiene alto, el modelo está saturado
- Útil para decidir cuándo escalar (más contenedores)

---

### `last_prediction_duration_minutes` (Gauge)

```
last_prediction_duration_minutes 26.23
```

**¿Qué mide?** La duración predicha en la última llamada a `/predict`.

**¿Para qué sirve?**
- Dashboard rápido del último valor predicho
- Debugging en tiempo real

---

### `batch_size` (Histogram)

```
batch_size_bucket{le="5.0"} 8.0
batch_size_bucket{le="10.0"} 10.0
batch_size_bucket{le="100.0"} 12.0
batch_size_sum 156.0
batch_size_count 12.0
```

**¿Qué mide?** Tamaño de los batches que recibe `/predict/batch`.

**Buckets:** 1, 5, 10, 25, 50, 100, 250, 500, 1000

**¿Para qué sirve?**
- Entender cómo usan los clientes el endpoint batch
- Optimizar si la mayoría manda batches pequeños (¿vale la pena el endpoint batch?)
- Alertar si alguien manda batches de 1000 que podrían saturar

---

## Métricas Automáticas de Python

Estas vienen incluidas automáticamente por `prometheus-client`:

| Métrica | Tipo | Significado |
|---------|------|-------------|
| `python_gc_objects_collected_total` | Counter | Objetos de memoria liberados por garbage collector |
| `python_gc_objects_uncollectable_total` | Counter | Objetos que no se pudieron liberar (si sube = memory leak) |
| `python_gc_collections_total` | Counter | Veces que se ejecutó el garbage collector |
| `python_info` | Gauge | Versión de Python en ejecución |

---

## Cómo Acceder

### Ver métricas crudas (formato Prometheus)
```bash
curl http://localhost:8000/metrics
```

### Ver en el navegador
```
http://localhost:8000/metrics
```

### Con Prometheus corriendo (docker-compose)
```
http://localhost:9090        → Prometheus UI
http://localhost:3000        → Grafana (admin/admin)
```

---

## Ejemplos de Consultas PromQL

Estas consultas se usan en Prometheus o Grafana:

### Predicciones por segundo (últimos 5 min)
```promql
rate(predictions_total[5m])
```

### Latencia promedio de inferencia
```promql
rate(prediction_duration_seconds_sum[5m]) / rate(prediction_duration_seconds_count[5m])
```

### Percentil 95 de latencia
```promql
histogram_quantile(0.95, rate(prediction_duration_seconds_bucket[5m]))
```

### Tasa de errores
```promql
rate(predictions_total{status="error"}[5m]) / rate(predictions_total[5m])
```

### Duración promedio predicha
```promql
rate(predicted_trip_duration_minutes_sum[5m]) / rate(predicted_trip_duration_minutes_count[5m])
```

### Distancia promedio de input
```promql
rate(trip_distance_miles_sum[5m]) / rate(trip_distance_miles_count[5m])
```

---

## Arquitectura del Monitoreo

```
┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│   Taxi API  │ ──────► │ Prometheus  │ ──────► │   Grafana   │
│  :8000      │ scrape  │  :9090      │  query  │  :3000      │
│  /metrics   │ cada 15s│  almacena   │         │  dashboards │
└─────────────┘         └─────────────┘         └─────────────┘
```

1. **API** expone `/metrics` en formato Prometheus
2. **Prometheus** hace scrape cada 15 segundos y almacena las series de tiempo
3. **Grafana** consulta Prometheus y muestra dashboards visuales

---
