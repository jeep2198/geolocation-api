# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Geolocation API",
    description="API para registrar y consultar ubicaciones de dispositivos GPS",
    version="1.0.0"
)

# --- MODELOS ---
class Location(BaseModel):
    device_id: str
    latitude: float
    longitude: float
    timestamp: str

# Base temporal en memoria
locations: List[Location] = []


@app.get("/health")
def health():
    return {"status": "ok"}

# --- ENDPOINTS ---
@app.get("/", tags=["Health"])
def root():
    return {"message": "Geolocation API is running 🚀"}

@app.post("/locations", tags=["Locations"])
def add_location(location: Location):
    locations.append(location)
    return {"message": "Location added", "total": len(locations)}

@app.get("/locations", response_model=List[Location], tags=["Locations"])
def get_locations():
    return locations
