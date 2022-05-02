import datetime
from typing import Optional

from pydantic import BaseModel

from schemas import ProductGetModel


class OrderModel(BaseModel):
    author: Optional[int]
    content: dict[str, dict]
    date: Optional[datetime.date]
    status: Optional[str]
    address: str
    index: int
    price_sum: float
