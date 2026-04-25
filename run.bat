docker run -d --name app --network back-net -v items-data:/data llesna/product-dashboard-backend:v2
docker run -d --name nginx-proxy --network front-net -p 80:80 llesna/product-dashboard-frontend:v2

docker network connect back-net nginx-proxy