from typing import List

from sqlalchemy.orm import Session

from schemas import ProductModel
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
