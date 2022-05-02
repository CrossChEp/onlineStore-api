import datetime
from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session

from configs import PROCESSING_STATUS
from models.general_methods import clear_model
from schemas import OrderModel
from store import User, Order


def add_order_to_database(order_data: OrderModel, author: User, session: Session) -> None:
    order_data.date = datetime.date.today()
    order_data.status = PROCESSING_STATUS
    clean_order_data = clear_model(order_data)
    order = Order(**clean_order_data)
    session.add(order)
    author.orders.append(order)
    session.commit()


def get_user_orders_from_database(user: User) -> List[Order]:
    orders = user.orders
    return orders


def get_order_from_database(order_id: int, user: User, session: Session) -> Order:
    order = session.query(Order).filter_by(id=order_id).first()
    if order not in user.orders:
        raise HTTPException(status_code=403)
    return order


def cancel_user_order(order_id: int, user: User, session: Session) -> None:
    order = get_order_from_database(order_id, user, session)
    session.delete(order)
    session.commit()