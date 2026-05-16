import pytest
import json
import sys
import os

# Dodaj folder nadrzędny do ścieżki żeby zaimportować app
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.app import app


@pytest.fixture
def client():
    """Klient testowy Flask — nie wymaga bazy ani Redisa"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# ── Test 1: Walidacja — brak pól w POST /items ──
def test_add_item_missing_fields(client):
    """POST /items bez wymaganych pól zwraca 400"""
    response = client.post(
        "/items",
        data=json.dumps({}),
        content_type="application/json",
    )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert "error" in data


# ── Test 2: Walidacja — brak nazwy produktu ──
def test_add_item_missing_name(client):
    """POST /items bez nazwy zwraca 400"""
    response = client.post(
        "/items",
        data=json.dumps({"price": 99.99}),
        content_type="application/json",
    )
    assert response.status_code == 400


# ── Test 3: Walidacja — brak ceny produktu ──
def test_add_item_missing_price(client):
    """POST /items bez ceny zwraca 400"""
    response = client.post(
        "/items",
        data=json.dumps({"name": "Laptop"}),
        content_type="application/json",
    )
    assert response.status_code == 400


# ── Test 4: Endpoint /health zwraca status ok ──
def test_health_endpoint(client):
    """GET /health zwraca status ok"""
    response = client.get("/health")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["status"] == "ok"


# ── Test 5: Walidacja — pusty JSON ──
def test_add_item_empty_body(client):
    """POST /items z pustym body zwraca 400"""
    response = client.post(
        "/items",
        data="",
        content_type="application/json",
    )
    assert response.status_code == 400