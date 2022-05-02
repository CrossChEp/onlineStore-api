from sqlalchemy.orm import Session

from models import get_product_from_database
from schemas import ProductRequestGetModel
from store import User


def add_product_to_user_bag(product_id: int, user: User, session: Session) -> None:
    product = get_product_from_database(ProductRequestGetModel(id=product_id), session)
    user.bag.append(product)
    session.commit()
