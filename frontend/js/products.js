const API_BASE = '/api';

async function loadProducts() {
    const container = document.getElementById('products-list');
    try {
        const res = await fetch(`${API_BASE}/items`);
        const data = await res.json();

        if (!data.items || data.items.length === 0) {
            container.innerHTML = '<p>Brak produktów. Dodaj pierwszy!</p>';
            return;
        }

        let html = `
            <table class="product-table">
                <thead>
                    <tr><th>ID</th><th>Nazwa</th><th>Cena (PLN)</th></tr>
                </thead>
                <tbody>`;

        data.items.forEach(item => {
            html += `<tr>
                <td>${item.id}</td>
                <td>${item.name}</td>
                <td>${Number(item.price).toFixed(2)}</td>
            </tr>`;
        });

        html += '</tbody></table>';
        container.innerHTML = html;
    } catch (err) {
        container.innerHTML = `<p style="color:red;">Błąd ładowania: ${err.message}</p>`;
    }
}

document.getElementById('product-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const msg = document.getElementById('form-message');
    const name = document.getElementById('name').value.trim();
    const price = parseFloat(document.getElementById('price').value);

    try {
        const res = await fetch(`${API_BASE}/items`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, price }),
        });
        const data = await res.json();

        if (res.ok) {
            msg.style.color = 'green';
            msg.textContent = `Dodano produkt: ${data.item.name}`;
            document.getElementById('product-form').reset();
            loadProducts();
        } else {
            msg.style.color = 'red';
            msg.textContent = data.error || 'Błąd dodawania produktu';
        }
    } catch (err) {
        msg.style.color = 'red';
        msg.textContent = `Błąd sieci: ${err.message}`;
    }
});

loadProducts();