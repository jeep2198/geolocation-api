from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"].startswith("Geolocation API")


def test_add_location():
    payload = {
        "device_id": "gps123",
        "latitude": 7.123,
        "longitude": -72.543,
        "timestamp": "2025-09-19T18:00:00Z",
    }
    response = client.post("/locations", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Location added"
    assert data["total"] >= 1


def test_add_location_invalid():
    payload = {
        "device_id": "gps456",
        "latitude": "not-a-float",  # inválido
        "longitude": -72.543,
        "timestamp": "2025-09-19T18:05:00Z",
    }
    response = client.post("/locations", json=payload)
    assert response.status_code == 422


def test_get_locations():
    response = client.get("/locations")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:  # si ya se agregaron ubicaciones
        assert "device_id" in data[0]
        assert "latitude" in data[0]
