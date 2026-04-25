docker stop app nginx-proxy
docker rm app nginx-proxy

docker build -t product-dashboard-backend:v2 --build-arg IMAGE_VERSION=v2 ./backend/
docker build -t product-dashboard-frontend:v2 --build-arg IMAGE_VERSION=v2 ./frontend/

docker tag product-dashboard-backend:v2 llesna/product-dashboard-backend:v2
docker tag product-dashboard-backend:v2 llesna/product-dashboard-backend:latest
docker tag product-dashboard-frontend:v2 llesna/product-dashboard-frontend:v2
docker tag product-dashboard-frontend:v2 llesna/product-dashboard-frontend:latest

docker push llesna/product-dashboard-backend:v2
docker push llesna/product-dashboard-backend:latest
docker push llesna/product-dashboard-frontend:v2
docker push llesna/product-dashboard-frontend:latest
