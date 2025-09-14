# Imagen base ligera de Python
FROM python:3.11-slim

# Evitar prompts en instalaciones
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Crear usuario no root
RUN addgroup --system appgroup && adduser --system appuser --ingroup appgroup

# Directorio de trabajo
WORKDIR /app

# Instalar dependencias
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY app/ .

# Cambiar permisos
RUN chown -R appuser:appgroup /app
USER appuser

# Exponer el puerto
EXPOSE 8000

# Comando de arranque
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
