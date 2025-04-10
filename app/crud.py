from sqlalchemy.orm import Session
from app.database import WalletQuery


def create_wallet_query(db: Session, wallet_data: dict):
    db_query = WalletQuery(**wallet_data)
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    return db_query


def get_query_history(db: Session, page: int = 1, limit: int = 10):
    offset = (page - 1) * limit
    queries = db.query(WalletQuery).offset(offset).limit(limit).all()
    total = db.query(WalletQuery).count()
    return {
        "results": queries,
        "total": total,
        "page": page,
        "limit": limit,
    }
