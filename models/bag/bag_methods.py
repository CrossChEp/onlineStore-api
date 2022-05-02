from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import get_product_from_database
from schemas import ProductRequestGetModel
from store import User
from store.db_model import Product


def add_product_to_user_bag(product_id: int, user: User, session: Session) -> None:
    product = get_product_from_database(ProductRequestGetModel(id=product_id), session)
    user.bag.append(product)
    session.commit()


def get_products_from_user_bag(user: User) -> List[Product]:
    products = user.bag
    return products


def delete_product_from_user_bag(product_id: int, user: User, session: Session) -> None:
    product = get_product_from_database(ProductRequestGetModel(id=product_id), session)
    if product not in user.products:
        raise HTTPException(status_code=403)
    user.bag.remove(product)
    session.commit()
