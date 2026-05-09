docker stop app
docker rm app
docker build -t product-dashboard-backend:v2 --build-arg IMAGE_VERSION=v2 ./backend/
docker push llesna/product-dashboard-backend:v2
docker push llesna/product-dashboard-frontend:v2
docker tag llesna/product-dashboard-backend:v2 llesna/product-dashboard-backend:latest
docker tag llesna/product-dashboard-frontend:v2 llesna/product-dashboard-frontend:latest
docker push llesna/product-dashboard-backend:latest
docker push llesna/product-dashboard-frontend:latest