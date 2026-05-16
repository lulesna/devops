from flask import Flask, request, jsonify
import psycopg2
import redis
import json
import uuid
import os

app = Flask(__name__)

INSTANCE_ID = os.environ.get("INSTANCE_ID", str(uuid.uuid4())[:12])

cache_hits = 0


def get_db():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        port=int(os.environ.get("DB_PORT", 5432)),
        dbname=os.environ.get("POSTGRES_DB", "products"),
        user=os.environ.get("POSTGRES_USER", "products"),
        password=os.environ.get("POSTGRES_PASSWORD", "postgres"),
    )


def get_cache():
    return redis.Redis(
        host=os.environ.get("REDIS_HOST", "cache"),
        port=int(os.environ.get("REDIS_PORT", 6379)),
        decode_responses=True,
    )


def init_db():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id    SERIAL PRIMARY KEY,
                name  TEXT NOT NULL,
                price NUMERIC(10,2) NOT NULL DEFAULT 0
            );
        """)
        conn.commit()
        cur.close()
        conn.close()
    except Exception:
        print("DB not available — skipping init (ok in testing)")


if not app.config.get("TESTING"):
    init_db()


@app.route("/items", methods=["GET"])
def get_items():
    global cache_hits

    r = get_cache()
    cached = r.get("items")
    if cached:
        cache_hits += 1
        return jsonify({"items": json.loads(cached)})

    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, name, price FROM products ORDER BY id")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    items = [{"id": row[0], "name": row[1], "price": float(row[2])} for row in rows]

    r.setex("items", 30, json.dumps(items))

    return jsonify({"items": items})


@app.route("/items", methods=["POST"])
def add_item():
    data = request.get_json(silent=True)

    if not data or not data.get("name") or data.get("price") is None:
        return jsonify({"error": "Wymagane pola: name, price"}), 400

    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO products (name, price) VALUES (%s, %s) RETURNING id, name, price",
        (data["name"], float(data["price"])),
    )
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    item = {"id": row[0], "name": row[1], "price": float(row[2])}

    r = get_cache()
    r.delete("items")

    return jsonify({"item": item}), 201


@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM products WHERE id = %s RETURNING id", (item_id,))
    deleted = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    if not deleted:
        return jsonify({"error": "Nie znaleziono produktu"}), 404

    r = get_cache()
    r.delete("items")
    return jsonify({"deleted": item_id})


@app.route("/stats", methods=["GET"])
def get_stats():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM products")
    count = cur.fetchone()[0]
    cur.close()
    conn.close()

    return jsonify({
        "total_products": count,
        "instance_id": INSTANCE_ID,
        "cache_hits": cache_hits,
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
