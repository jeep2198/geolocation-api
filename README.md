# 🌍 Geolocation API

A simple **FastAPI** application to expose geolocation services.  
Includes support for deployment with **Docker**, **Docker Compose**, and is ready for **Kubernetes**.

---

## 🚀 Prerequisites

- [Python 3.10+](https://www.python.org/)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## 🛠️ Run locally with Python

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv ~/venvs/geolocation-api
   source ~/venvs/geolocation-api/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r app/requirements.txt
   ```

3. Start the API:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

4. Test health endpoint:
   ```bash
   curl http://localhost:8000/health
   ```

---

## 🐳 Build Docker image manually

1. Build the image:
   ```bash
   docker buildx build      -t api-geolocation:0.0.1      -f docker/Dockerfile      .      --load
   ```

2. Run the container:
   ```bash
   docker run --rm --name api-geolocation -p 8000:8000 api-geolocation:0.0.1
   ```

---

## ⚡ Run with Docker Compose

### Development
Run with hot-reload (`docker-compose.override.yml` is loaded by default):
```bash
docker compose up --build
```

### Production
Run without override:
```bash
docker compose -f docker-compose.yml up -d --build
```

---

## 📖 Interactive documentation

Once the API is running, you can access automatically generated documentation:

- Swagger UI → [http://localhost:8000/docs](http://localhost:8000/docs)  
- Redoc → [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🔍 Endpoints

- `GET /health` → Service health check.  
- (More geolocation endpoints coming soon)

