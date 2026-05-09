docker stop app
docker rm app
docker build -t product-dashboard-backend:v2 --build-arg IMAGE_VERSION=v2 ./backend/
docker tag product-dashboard-backend:v2 llesna/product-dashboard-backend:v2
docker push llesna/product-dashboard-backend:v2