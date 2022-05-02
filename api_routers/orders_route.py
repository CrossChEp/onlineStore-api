from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api_routers.auth_routes import get_current_user
from middlewares import generate_session
from models import add_order_to_database
from schemas import OrderModel
from store import User

orders_router = APIRouter()


@orders_router.post('/api/order')
def add_order(order_data: OrderModel, author: User = Depends(get_current_user),
              session: Session = Depends(generate_session)) -> None:
    add_order_to_database(order_data=order_data, author=author, session=session)
