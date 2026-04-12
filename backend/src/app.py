from flask import Flask, request, jsonify
import uuid
import os
import json

app = Flask(__name__)

INSTANCE_ID = os.environ.get("INSTANCE_ID", str(uuid.uuid4())[:12])

DATA_FILE = "/data/items.json"


def load_items():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_items(items):
    with open(DATA_FILE, "w") as f:
        json.dump(items, f)


@app.route("/items", methods=["GET"])
def get_items():
    items = load_items()
    return jsonify({"items": items})


@app.route("/items", methods=["POST"])
def add_item():
    data = request.get_json(silent=True)

    if not data or not data.get("name") or data.get("price") is None:
        return jsonify({"error": "Wymagane pola: name, price"}), 400

    items = load_items()

    next_id = max([i["id"] for i in items], default=0) + 1

    item = {
        "id": next_id,
        "name": data["name"],
        "price": float(data["price"]),
    }
    items.append(item)
    save_items(items)

    return jsonify({"item": item}), 201


@app.route("/stats", methods=["GET"])
def get_stats():
    items = load_items()
    return jsonify({
        "total_products": len(items),
        "instance_id": INSTANCE_ID,
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "instance_id": INSTANCE_ID})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)