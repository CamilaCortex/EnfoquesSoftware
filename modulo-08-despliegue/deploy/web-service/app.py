"""
API REST con FastAPI para predicción de duración de viajes de taxi.
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, Response
from fastapi.templating import Jinja2Templates
import logging
import time

from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

from src.schemas import (
    TripRequest,
    BatchTripRequest,
    PredictionResponse,
    BatchPredictionResponse,
    HealthResponse
)
from src.model_loader import model_loader
from src.metrics import (
    model_info,
    predictions_total,
    requests_total,
    prediction_duration_seconds,
    predicted_trip_duration_minutes,
    trip_distance_histogram,
    predictions_in_progress,
    last_prediction_duration,
    batch_size_histogram,
)

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Crear app
app = FastAPI(
    title="NYC Taxi Duration Prediction API",
    description="API para predecir la duración de viajes de taxi en NYC",
    version="1.0.0"
)

# Templates
templates = Jinja2Templates(directory="templates")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    """Carga el modelo al iniciar la aplicación"""
    logging.info("Iniciando API...")
    try:
        model_loader.load()
        model_info.info({
            'name': model_loader.metadata['model_name'],
            'version': str(model_loader.metadata['version']),
            'rmse': str(model_loader.metadata['rmse'])
        })
        logging.info("API lista para recibir requests")
    except Exception as e:
        logging.error("Error al cargar modelo: %s", e)
        raise


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """Interfaz web para hacer predicciones"""
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint.
    Verifica que el modelo esté cargado y funcionando.
    """
    try:
        is_loaded = model_loader.is_loaded()
        
        if not is_loaded:
            raise HTTPException(
                status_code=503,
                detail="Modelo no cargado"
            )
        
        return HealthResponse(
            status="healthy",
            model_loaded=True,
            model_name=model_loader.metadata['model_name'],
            model_version=str(model_loader.metadata['version']),
            model_rmse=model_loader.metadata['rmse']
        )
    
    except Exception as e:
        logging.error("Error en health check: %s", e)
        raise HTTPException(
            status_code=503,
            detail=f"Error en health check: {str(e)}"
        ) from e


@app.post("/predict", response_model=PredictionResponse)
async def predict(trip: TripRequest):
    """
    Predice la duración de un viaje de taxi.
    
    Args:
        trip: Datos del viaje (PULocationID, DOLocationID, trip_distance)
        
    Returns:
        Predicción de duración en minutos
    """
    predictions_in_progress.inc()
    start_time = time.time()
    try:
        # Registrar distancia recibida
        trip_distance_histogram.observe(trip.trip_distance)
        
        # Preparar features (PU_DO combinado)
        feature = {
            'PU_DO': f"{trip.PULocationID}_{trip.DOLocationID}",
            'trip_distance': trip.trip_distance
        }
        
        # Predecir
        predictions = model_loader.predict([feature])
        duration = round(predictions[0], 2)
        
        # Registrar métricas
        prediction_duration_seconds.labels(endpoint='/predict').observe(time.time() - start_time)
        predicted_trip_duration_minutes.observe(duration)
        last_prediction_duration.set(duration)
        predictions_total.labels(endpoint='/predict', status='success').inc()
        requests_total.labels(method='POST', endpoint='/predict', status_code='200').inc()
        
        return PredictionResponse(
            PULocationID=trip.PULocationID,
            DOLocationID=trip.DOLocationID,
            trip_distance=trip.trip_distance,
            predicted_duration_minutes=duration,
            model_name=model_loader.metadata['model_name'],
            model_version=str(model_loader.metadata['version'])
        )
    
    except Exception as e:
        predictions_total.labels(endpoint='/predict', status='error').inc()
        requests_total.labels(method='POST', endpoint='/predict', status_code='500').inc()
        logging.error("Error en predicción: %s", e)
        raise HTTPException(
            status_code=500,
            detail=f"Error al hacer predicción: {str(e)}"
        ) from e
    finally:
        predictions_in_progress.dec()


@app.post("/predict/batch", response_model=BatchPredictionResponse)
async def predict_batch(batch: BatchTripRequest):
    """
    Predice la duración de múltiples viajes de taxi.
    
    Args:
        batch: Lista de viajes
        
    Returns:
        Lista de predicciones
    """
    predictions_in_progress.inc()
    start_time = time.time()
    try:
        # Registrar tamaño del batch
        batch_size_histogram.observe(len(batch.trips))
        
        # Registrar distancias recibidas
        for trip in batch.trips:
            trip_distance_histogram.observe(trip.trip_distance)
        
        # Preparar features (PU_DO combinado)
        features = [
            {
                'PU_DO': f"{trip.PULocationID}_{trip.DOLocationID}",
                'trip_distance': trip.trip_distance
            }
            for trip in batch.trips
        ]
        
        # Predecir
        predictions = model_loader.predict(features)
        
        # Registrar métricas de predicción
        prediction_duration_seconds.labels(endpoint='/predict/batch').observe(time.time() - start_time)
        for pred in predictions:
            predicted_trip_duration_minutes.observe(round(pred, 2))
        predictions_total.labels(endpoint='/predict/batch', status='success').inc(len(batch.trips))
        requests_total.labels(method='POST', endpoint='/predict/batch', status_code='200').inc()
        
        # Crear respuestas
        prediction_responses = [
            PredictionResponse(
                PULocationID=trip.PULocationID,
                DOLocationID=trip.DOLocationID,
                trip_distance=trip.trip_distance,
                predicted_duration_minutes=round(pred, 2),
                model_name=model_loader.metadata['model_name'],
                model_version=str(model_loader.metadata['version'])
            )
            for trip, pred in zip(batch.trips, predictions)
        ]
        
        return BatchPredictionResponse(
            predictions=prediction_responses,
            total=len(prediction_responses),
            model_name=model_loader.metadata['model_name'],
            model_version=str(model_loader.metadata['version'])
        )
    
    except Exception as e:
        predictions_total.labels(endpoint='/predict/batch', status='error').inc()
        requests_total.labels(method='POST', endpoint='/predict/batch', status_code='500').inc()
        logging.error("Error en predicción batch: %s", e)
        raise HTTPException(
            status_code=500,
            detail=f"Error al hacer predicción batch: {str(e)}"
        ) from e
    finally:
        predictions_in_progress.dec()


@app.get("/metrics")
async def metrics():
    """Endpoint de métricas para Prometheus"""
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


# lsof -ti:8000 | xargs kill -9
# uv run uvicorn app:app --reload --host 0.0.0.0 --port 8000  


# curl -X POST http://localhost:8000/predict/batch \
#   -H "Content-Type: application/json" \
#   -d '{
#     "trips": [
#       {
#         "PULocationID": 161,
#         "DOLocationID": 236,
#         "trip_distance": 5.2
#       },
#       {
#         "PULocationID": 237,
#         "DOLocationID": 238,
#         "trip_distance": 3.8
#       },
#       {
#         "PULocationID": 100,
#         "DOLocationID": 200,
#         "trip_distance": 15.0
#       }
#     ]
#   }'

# curl -X POST http://localhost:8000/predict \
#   -H "Content-Type: application/json" \
#   -d '{"PULocationID": 161, "DOLocationID": 236, "trip_distance": 1.5}'

# http://localhost:8000/metrics