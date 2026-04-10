docker stop nginx-proxy api-a api-b
docker rm nginx-proxy api-a api-b

docker network rm siec-product-dashboard

docker rmi product-dashboard-backend:v1
docker rmi product-dashboard-frontend:v2
docker rmi llesna/product-dashboard-backend:v1
docker rmi llesna/product-dashboard-backend:latest
docker rmi llesna/product-dashboard-frontend:v2
docker rmi llesna/product-dashboard-frontend:latest