from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api_routers.auth_routes import get_current_user
from middlewares import generate_session
from models import add_product_to_database, get_all_products_from_database, get_typed_products_from_database, \
    get_author_products_from_database, get_products_sorted_by_name, get_products_sorted_by_sex, \
    get_product_from_database, update_product_data, delete_product_from_database
from schemas import ProductModel, ProductRequestGetModel, ProductRequestModel
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


@product_router.get('/api/product/author/{author_id}')
def get_author_products(author_id: int, session: Session = Depends(generate_session)) -> List[Product]:
    return get_author_products_from_database(author_id=author_id, session=session)


@product_router.get('/api/product/name/{product_name}')
def get_products_by_name(product_name: str, session: Session = Depends(generate_session)) -> List[Product]:
    return get_products_sorted_by_name(product_name, session)


@product_router.get('/api/product/sex/{sex}')
def get_product_by_sex(sex: str, session: Session = Depends(generate_session)) -> List[Product]:
    return get_products_sorted_by_sex(sex, session)


@product_router.get('/api/product/id/{product_id}')
def get_product_by_id(product_id: int, session: Session = Depends(generate_session)) -> Product:
    return get_product_from_database(ProductRequestGetModel(id=product_id), session)


@product_router.put('/api/product')
def update_product(product_id: int, new_product_data: ProductRequestModel,
                   author: User = Depends(get_current_user),
                   session: Session = Depends(generate_session)) -> None:
    update_product_data(product_id=product_id, new_product_data=new_product_data,
                        author=author, session=session)


@product_router.delete('/api/product')
def delete_product(product_id: int, author: User = Depends(get_current_user),
                   session: Session = Depends(generate_session)) -> None:
    delete_product_from_database(product_id=product_id, author=author, session=session)
