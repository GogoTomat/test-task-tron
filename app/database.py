from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/trondb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class WalletQuery(Base):
    __tablename__ = "wallet_queries"

    id = Column(Integer, primary_key=True, index=True)
    wallet_address = Column(String, index=True)
    bandwidth = Column(Integer)
    energy = Column(Integer)
    trx_balance = Column(Integer)
    query_time = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(bind=engine)
