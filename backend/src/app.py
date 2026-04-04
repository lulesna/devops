from flask import Flask, request, jsonify
import uuid
import os

app = Flask(__name__)

INSTANCE_ID = os.environ.get("INSTANCE_ID", str(uuid.uuid4())[:12])

products = []
next_id = 1


@app.route("/items", methods=["GET"])
def get_items():
    return jsonify({"items": products})


@app.route("/items", methods=["POST"])
def add_item():
    global next_id
    data = request.get_json(silent=True)

    if not data or not data.get("name") or data.get("price") is None:
        return jsonify({"error": "Wymagane pola: name, price"}), 400

    item = {
        "id": next_id,
        "name": data["name"],
        "price": float(data["price"]),
    }
    next_id += 1
    products.append(item)
    return jsonify({"item": item}), 201


@app.route("/stats", methods=["GET"])
def get_stats():
    return jsonify({
        "total_products": len(products),
        "instance_id": INSTANCE_ID,
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)