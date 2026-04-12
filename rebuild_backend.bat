docker stop app
docker rm app
docker build -t product-dashboard-backend:v2 --build-arg IMAGE_VERSION=v2 ./backend/
docker run -d --name app --network back-net -e INSTANCE_ID=instancja-a -v items-data:/data product-dashboard-backend:v2