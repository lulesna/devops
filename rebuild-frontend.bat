@echo off
docker stop nginx-proxy
docker rm nginx-proxy
docker build -t product-dashboard-frontend:v1 ./frontend
docker run -d --name nginx-proxy --network siec-product-dashboard -p 80:80 product-dashboard-frontend:v1