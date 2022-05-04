from typing import Dict, List, Optional

from pydantic import BaseModel


class ProductModel(BaseModel):
    sex: str
    name: str
    type: str
    description: str
    sizes: dict[str, List[str]]
    image: Optional[str]
    price: float

    class Config:
        orm_mode = True


class ProductGetModel(ProductModel):
    id: int
    author: int

    class Config:
        orm_mode = True


class ProductRequestModel(BaseModel):
    sex: Optional[str]
    name: Optional[str]
    type: Optional[str]
    description: Optional[str]
    sizes: Optional[dict[str, List[str]]]
    price: Optional[float]

    class Config:
        orm_mode = True


class ProductRequestGetModel(ProductRequestModel):
    id: Optional[int]

    class Config:
        orm_mode = True
