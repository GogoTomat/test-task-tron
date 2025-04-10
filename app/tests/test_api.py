from fastapi.testclient import TestClient
from ..main import app
from ..database import Base, engine

client = TestClient(app)


def setup_module():
    Base.metadata.create_all(bind=engine)


def teardown_module():
    Base.metadata.drop_all(bind=engine)


def test_get_wallet_info():
    response = client.post(
        "/wallet-info/",
        json={"wallet_address": "TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL"},
    )
    assert response.status_code == 200


def test_query_history():
    response = client.get("/query-history/?page=1&limit=10")
    assert response.status_code == 200
    assert "results" in response.json()
