import datetime

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
