docker stop nginx-proxy app
docker rm nginx-proxy app

docker network rm front-net back-net

docker rmi product-dashboard-backend:v2
docker rmi product-dashboard-frontend:v2
docker rmi llesna/product-dashboard-backend:v2
docker rmi llesna/product-dashboard-backend:latest
docker rmi llesna/product-dashboard-frontend:v2
docker rmi llesna/product-dashboard-frontend:latest