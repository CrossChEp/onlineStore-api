from typing import Dict, List

from pydantic import BaseModel


class ProductModel(BaseModel):
    sex: str
    name: str
    type: str
    description: str
    sizes: dict[str, List[str]]
    price: float


class ProductGetModel(ProductModel):
    id: int
    author: int

