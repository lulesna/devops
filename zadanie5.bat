docker stop nginx-proxy app
docker rm nginx-proxy app

docker network rm front-net back-net

docker rmi product-dashboard-backend:v2
docker rmi product-dashboard-frontend:v2
docker rmi llesna/product-dashboard-backend:v2
docker rmi llesna/product-dashboard-backend:latest
docker rmi llesna/product-dashboard-frontend:v2
docker rmi llesna/product-dashboard-frontend:latest

docker pull llesna/product-dashboard-backend:v2
docker pull llesna/product-dashboard-frontend:v2

docker network create front-net
docker network create back-net

docker run -d --name app --network back-net -v items-data:/data llesna/product-dashboard-backend:v2
docker run -d --name nginx-proxy --network front-net -p 80:80 llesna/product-dashboard-frontend:v2
docker network connect back-net nginx-proxy

curl.exe http://localhost/api/items
curl.exe http://localhost/api/stats
