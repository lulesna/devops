docker stop nginx-proxy app
docker rm nginx-proxy app
docker network rm front-net back-net
docker volume rm items-data
docker compose up -d