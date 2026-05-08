docker rm -f app
docker volume rm items-data
docker volume create items-data
docker run -d --name app --network back-net -e INSTANCE_ID=instancja-a -v items-data:/data llesna/product-dashboard-backend:v2