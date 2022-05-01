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
