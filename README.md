
como ejecutar local 
# crea un venv en tu $HOME
python3 -m venv ~/venvs/geolocation-api

# actívalo
source ~/venvs/geolocation-api/bin/activate

## construccion manual de la imagen 
docker buildx build   -t api-geolocation:0.0.1   -f docker/Dockerfile   .   --load

docker run -rmi --name api-geolocation -p 8000:8000 api-geolocation:0.0.1  