from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api_routers.auth_routes import get_current_user
from middlewares import generate_session
from models import add_product_to_database
from schemas import ProductModel
from store import User

product_router = APIRouter()


@product_router.post('/api/product')
def add_product(product_data: ProductModel,
                session: Session = Depends(generate_session),
                author: User = Depends(get_current_user)) -> None:
    add_product_to_database(author=author, product_data=product_data, session=session)

