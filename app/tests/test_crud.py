import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..database import Base
from ..crud import create_wallet_query

SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/trondb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.rollback()
    Base.metadata.drop_all(bind=engine)


def test_create_wallet_query(db):
    wallet_data = {
        "wallet_address": "TX123...",
        "bandwidth": 1000,
        "energy": 500,
        "trx_balance": 1000000,
    }
    query = create_wallet_query(db, wallet_data)
    assert query.id is not None
    assert query.wallet_address == "TX123..."
