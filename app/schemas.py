from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class WalletInfoRequest(BaseModel):
    wallet_address: str


class WalletInfoResponse(BaseModel):
    wallet_address: str
    bandwidth: int
    energy: int
    trx_balance: int


class QueryHistoryResponse(BaseModel):
    id: int
    wallet_address: str
    bandwidth: int
    energy: int
    trx_balance: int
    query_time: datetime


class PaginatedResponse(BaseModel):
    results: list[QueryHistoryResponse]
    total: int
    page: int
    limit: int
