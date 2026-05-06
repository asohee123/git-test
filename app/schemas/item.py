from pydantic import BaseModel
from datetime import datetime


class ItemCreate(BaseModel):
    name: str
    description: str
    price: float


class ItemUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None


class ItemResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    created_at: datetime
