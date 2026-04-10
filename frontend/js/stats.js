function loadStats() {
    fetch("/api/stats")
        .then(function (response) {
            const cache = response.headers.get("X-Cache-Status");
            document.getElementById("cache-status").textContent = cache || "brak";

            return response.json();
        })
        .then(function (data) {
            document.getElementById("product-count").textContent = data.total_products;
            document.getElementById("instance-id").textContent = data.instance_id;
        });
}

document.getElementById("refresh-btn").onclick = loadStats;

loadStats();
