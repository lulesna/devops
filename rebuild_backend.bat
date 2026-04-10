docker stop api-a api-b
docker rm api-a api-b
docker build -t product-dashboard-backend:v1 --build-arg IMAGE_VERSION=v1 ./backend/
docker run -d --name api-a --network siec-product-dashboard -e INSTANCE_ID=instancja-A product-dashboard-backend:v1
docker run -d --name api-b --network siec-product-dashboard -e INSTANCE_ID=instancja-B product-dashboard-backend:v1