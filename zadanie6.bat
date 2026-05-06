rename compose.override.yml compose.override.yml.bak
docker compose down
docker compose up -d --build

curl.exe http://localhost/api/stats
curl.exe http://localhost/api/items
curl.exe http://localhost/api/items
curl.exe http://localhost/api/stats
