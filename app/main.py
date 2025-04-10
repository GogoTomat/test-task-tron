from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import WalletInfoRequest, WalletInfoResponse, PaginatedResponse
from app.crud import create_wallet_query, get_query_history
from app.tron_utils import get_tron_wallet_info

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/wallet-info/", response_model=WalletInfoResponse)
async def get_wallet_info(request: WalletInfoRequest, db: Session = Depends(get_db)):
    try:
        wallet_data = await get_tron_wallet_info(request.wallet_address)
        db_wallet = create_wallet_query(db, wallet_data)
        return db_wallet
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/query-history/", response_model=PaginatedResponse)
async def read_query_history(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    history = get_query_history(db, page=page, limit=limit)
    return history
