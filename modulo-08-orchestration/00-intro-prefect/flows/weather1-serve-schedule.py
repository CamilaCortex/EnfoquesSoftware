import httpx
from prefect import flow

# 2. serve with schedule
@flow()
def fetch_weather(lat: float = 38.9, lon: float = -77.0):
    base_url = "https://api.open-meteo.com/v1/forecast/"
    temps = httpx.get(
        base_url,
        params=dict(latitude=lat, longitude=lon, hourly="temperature_2m"),
    )
    forecasted_temp = float(temps.json()["hourly"]["temperature_2m"][0])
    print(f"Forecasted temp C: {forecasted_temp} degrees")
    return forecasted_temp


if __name__ == "__main__":
    fetch_weather.serve(name="deploy-scheduled", cron="* * * * *")

# usamos serve para programar la ejecución en local, corre siempre y cuando tu terminal esté abierta
# útil para testing rápido sin subir a la nube
# ideal para desarrollo antes de hacer el deploy
# si cierras la terminal se detiene 

# https://crontab.cronhub.io/

# * * * * *
# │ │ │ │ │
# │ │ │ │ └─── día de la semana (0-6, donde 0 = domingo)
# │ │ │ └───── mes (1-12)
# │ │ └─────── día del mes (1-31)
# │ └───────── hora (0-23)
# └─────────── minuto (0-59)