function loadProducts() {
    fetch("/api/items")
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            const container = document.getElementById("products-list");

            if (data.items.length === 0) {
                container.innerHTML = "<p>Brak produktów. Dodaj pierwszy!</p>";
                return;
            }

            let html = "<table class='product-table'>";
            html += "<tr><th>ID</th><th>Nazwa</th><th>Cena (PLN)</th></tr>";

            for (let i = 0; i < data.items.length; i++) {
                html += "<tr>";
                html += "<td>" + data.items[i].id + "</td>";
                html += "<td>" + data.items[i].name + "</td>";
                html += "<td>" + data.items[i].price + "</td>";
                html += "</tr>";
            }

            html += "</table>";
            container.innerHTML = html;
        });
}

document.getElementById("product-form").onsubmit = function (e) {
    e.preventDefault();

    const name = document.getElementById("name").value;
    const price = document.getElementById("price").value;

    fetch("/api/items", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: name, price: Number(price) })
    })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            const msg = document.getElementById("form-message");
            msg.style.color = "green";
            msg.textContent = "Dodano: " + data.item.name;

            document.getElementById("product-form").reset();
            loadProducts();
        });
};

loadProducts();