# Guía: Levantar API con Docker + Monitoreo (Prometheus + Grafana)

---

## 1. Clonar y posicionarse

```bash
cd modulo-08-despliegue/deploy/web-service
```

---

## 2. Copiar el modelo

```bash
uv run python copy_model.py
```

---

## 3. Levantar los 3 servicios (API + Prometheus + Grafana)

```bash
docker-compose up -d --build
```

---

## 4. Verificar que todo está corriendo

```bash
docker ps
```

Deben ver 3 contenedores:

| Contenedor | Puerto | URL |
|---|---|---|
| `nyc-taxi-api` | 8000 | http://localhost:8000 |
| `taxi-prometheus` | 9090 | http://localhost:9090 |
| `taxi-grafana` | 3000 | http://localhost:3000 |

---

## 5. Verificar la API

```bash
curl http://localhost:8000/health
```

---

## 6. Hacer algunas predicciones (para generar datos)

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"PULocationID": 161, "DOLocationID": 236, "trip_distance": 5.2}'

curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"PULocationID": 237, "DOLocationID": 100, "trip_distance": 12.0}'

curl -X POST http://localhost:8000/predict/batch \
  -H "Content-Type: application/json" \
  -d '{"trips": [{"PULocationID": 161, "DOLocationID": 236, "trip_distance": 5.2}, {"PULocationID": 100, "DOLocationID": 200, "trip_distance": 15.0}, {"PULocationID": 50, "DOLocationID": 75, "trip_distance": 2.3}]}'
```

---

## 7. Ver métricas crudas

```bash
curl http://localhost:8000/metrics
```

O en el navegador: http://localhost:8000/metrics

---

## Configurar Grafana

### 8. Abrir Grafana

Ir a: http://localhost:3000

- **Usuario:** `admin`
- **Contraseña:** `admin`
- (Skip cambio de contraseña)

---

### 9. Conectar Prometheus como Data Source

1. Menú lateral → **Connections** → **Data sources**
2. Click **Add data source**
3. Seleccionar **Prometheus**
4. En **Prometheus server URL** escribir: `http://prometheus:9090`
5. Scroll abajo → Click **Save & Test**
6. Debe decir "Successfully queried the Prometheus API"

---

### 10. Crear Dashboard

1. Menú lateral → **Dashboards** → **New** → **New Dashboard**
2. Click **Add visualization**
3. Seleccionar datasource **Prometheus**

---

### 11. Agregar las 5 métricas (un panel por cada una)

#### Panel 1: Total de predicciones

- **Query:** `predictions_total`
- **Tipo de panel:** Stat
- **Título:** "Total Predicciones"

#### Panel 2: Predicciones por segundo

- **Query:** `rate(predictions_total[5m])`
- **Tipo de panel:** Time series
- **Título:** "Predicciones/seg"

#### Panel 3: Latencia promedio del modelo

- **Query:** `rate(prediction_duration_seconds_sum[5m]) / rate(prediction_duration_seconds_count[5m])`
- **Tipo de panel:** Time series
- **Título:** "Latencia Inferencia (seg)"

#### Panel 4: Duración promedio predicha

- **Query:** `rate(predicted_trip_duration_minutes_sum[5m]) / rate(predicted_trip_duration_minutes_count[5m])`
- **Tipo de panel:** Time series
- **Título:** "Duración Predicha (min)"

#### Panel 5: Predicciones en progreso

- **Query:** `predictions_in_progress`
- **Tipo de panel:** Gauge
- **Título:** "Concurrencia Actual"

---

### 12. Guardar el dashboard

- Click **Save** → Nombre: "NYC Taxi API Monitoring"

---

## Detener todo

```bash
docker-compose down
```

---

## Limpiar imágenes (opcional)

```bash
docker-compose down --rmi all
```

---

## Resumen de URLs

| Servicio | URL | Descripción |
|---|---|---|
| API - Interfaz web | http://localhost:8000 | Formulario para predicciones |
| API - Health | http://localhost:8000/health | Estado de la API |
| API - Métricas | http://localhost:8000/metrics | Métricas Prometheus |
| API - Docs | http://localhost:8000/docs | Swagger UI |
| Prometheus | http://localhost:9090 | Consultas PromQL |
| Grafana | http://localhost:3000 | Dashboards (admin/admin) |

---
