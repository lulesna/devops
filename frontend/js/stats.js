async function loadStats() {
    try {
        const res = await fetch('/api/stats');
        const data = await res.json();

        document.getElementById('product-count').textContent = data.total_products;
        document.getElementById('instance-id').textContent = data.instance_id;

        const cacheStatus = res.headers.get('X-Cache-Status') || 'brak nagłówka';
        document.getElementById('cache-status').textContent = cacheStatus;
    } catch (err) {
        document.getElementById('product-count').textContent = 'Błąd';
        document.getElementById('instance-id').textContent = err.message;
    }
}

document.getElementById('refresh-btn').addEventListener('click', loadStats);

loadStats();