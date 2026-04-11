docker network create siec-product-dashboard

docker build -t product-dashboard-backend:v1 --build-arg IMAGE_VERSION=v1 ./backend/
docker build -t product-dashboard-frontend:v2 ./frontend/

docker tag product-dashboard-backend:v1 llesna/product-dashboard-backend:v1
docker tag product-dashboard-backend:v1 llesna/product-dashboard-backend:latest
docker tag product-dashboard-frontend:v2 llesna/product-dashboard-frontend:v2
docker tag product-dashboard-frontend:v2 llesna/product-dashboard-frontend:latest
