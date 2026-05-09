docker compose build
docker push llesna/product-dashboard-backend:v3
docker push llesna/product-dashboard-frontend:v3
docker tag llesna/product-dashboard-backend:v3 llesna/product-dashboard-backend:latest
docker tag llesna/product-dashboard-frontend:v3 llesna/product-dashboard-frontend:latest
docker push llesna/product-dashboard-backend:latest
docker push llesna/product-dashboard-frontend:latest