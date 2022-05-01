from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api_routers.auth_routes import get_current_user
from middlewares import generate_session
from models import add_product_to_database, get_all_products_from_database, get_typed_products_from_database
from schemas import ProductModel, ProductGetModel
from store import User
from store.db_model import Product

product_router = APIRouter()


@product_router.post('/api/product')
def add_product(product_data: ProductModel,
                session: Session = Depends(generate_session),
                author: User = Depends(get_current_user)) -> None:
    add_product_to_database(author=author, product_data=product_data, session=session)


@product_router.get('/api/products')
def get_all_products(session: Session = Depends(generate_session)) -> List[Product]:
    return get_all_products_from_database(session)


@product_router.get('/api/product/type/{product_type}')
def get_typed_product(product_type: str,
                      session: Session = Depends(generate_session)) -> List[Product]:
    return get_typed_products_from_database(product_type=product_type, session=session)
