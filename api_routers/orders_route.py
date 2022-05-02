from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api_routers.auth_routes import get_current_user
from middlewares import generate_session
from models import add_order_to_database, get_user_orders_from_database, get_order_from_database, cancel_user_order
from schemas import OrderModel
from store import User, Order

orders_router = APIRouter()


@orders_router.post('/api/order')
def add_order(order_data: OrderModel, author: User = Depends(get_current_user),
              session: Session = Depends(generate_session)) -> None:
    add_order_to_database(order_data=order_data, author=author, session=session)


@orders_router.get('/api/order')
def get_user_orders(user: User = Depends(get_current_user)) -> List[Order]:
    return get_user_orders_from_database(user)


@orders_router.get('/api/order/{order_id}')
def get_order(order_id: int, user: User = Depends(get_current_user),
              session: Session = Depends(generate_session)) -> Order:
    return get_order_from_database(order_id, user, session)


@orders_router.delete('/api/order/{order_id}')
def cancel_order(order_id: int, user: User = Depends(get_current_user),
                 session: Session = Depends(generate_session)) -> None:
    cancel_user_order(order_id, user, session)
