from fastapi import FastAPI, Query
from vedastro import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/natal-chart")
def get_chart(
    year: int = Query(...),
    month: int = Query(...),
    day: int = Query(...),
    hour: int = Query(...),
    minute: int = Query(...),
    offset: float = Query(...),
    lat: float = Query(...),
    lon: float = Query(...)
):
    time = Time(
        year=int(year),
        month=int(month),
        day=int(day),
        hour=int(hour),
        minute=int(minute),
        second=0,
        offset=float(offset)
    )
    location = GeoLocation(latitude=lat, longitude=lon, name="User Input")

    chart = Horoscope.make_natal(time, location)
    planets = chart.get_planet_longitudes()

    return [
        {"name": p.planet.to_string(), "longitude": p.longitude}
        for p in planets
    ]
