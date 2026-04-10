docker network create siec-product-dashboard

docker pull llesna/product-dashboard-backend:v1
docker pull llesna/product-dashboard-frontend:v2

docker run -d --name api-a --network siec-product-dashboard -e INSTANCE_ID=instancja-a llesna/product-dashboard-backend:v1
docker run -d --name api-b --network siec-product-dashboard -e INSTANCE_ID=instancja-b llesna/product-dashboard-backend:v1
docker run -d --name nginx-proxy --network siec-product-dashboard -p 80:80 llesna/product-dashboard-frontend:v2