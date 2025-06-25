from fastapi import FastAPI, Query
from vedastro import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow Tilda frontend to make calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For public access. Replace * with your Tilda domain for security.
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
    offset: float = Query(...),  # Timezone offset e.g. +5.5
    lat: float = Query(...),
    lon: float = Query(...)
):
    time = Time.from_ymd_hms(year, month, day, hour, minute, 0, offset)
    loc = GeoLocation(lat, lon, "Location")

    chart = Horoscope.make_natal(time, loc)
    planets = chart.get_planet_longitudes()

    return [
        {"name": p.planet.to_string(), "longitude": p.longitude}
        for p in planets
    ]
