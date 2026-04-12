docker stop nginx-proxy
docker rm nginx-proxy
docker build -t product-dashboard-frontend:v2 --build-arg ./frontend/
docker run -d --name nginx-proxy --network front-net -p 80:80 product-dashboard-frontend:v2
docker network connect back-net nginx-proxy