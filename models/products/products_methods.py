from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.general_methods import clear_model
from schemas import ProductModel, ProductRequestGetModel
from store import User
from store.db_model import Product


def add_product_to_database(author: User,
                            product_data: ProductModel, session: Session) -> None:
    product = Product(**product_data.dict())
    session.add(product)
    author.products.append(product)
    session.commit()


def get_all_products_from_database(session: Session) -> List[Product]:
    products = session.query(Product).all()
    return products


def get_typed_products_from_database(product_type: str, session: Session) -> List[Product]:
    products = session.query(Product).filter_by(type=product_type).all()
    return products


def get_author_products_from_database(author_id: int, session: Session) -> List[Product]:
    products = session.query(Product).filter_by(author=author_id).first()
    return products


def get_products_sorted_by_name(product_name: str, session: Session) -> List[Product]:
    products = session.query(Product).filter_by(name=product_name).all()
    return products


def get_products_sorted_by_sex(sex: str, session: Session) -> List[Product]:
    products = session.query(Product).filter_by(sex=sex).all()
    return products


def get_product_from_database(product_data: ProductRequestGetModel, session: Session) -> Product:
    clean_product_data = clear_model(product_data)
    product = session.query(Product).filter_by(**clean_product_data).first()
    if not product:
        raise HTTPException(status_code=404, detail='not found')
    return product

