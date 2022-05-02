from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api_routers.auth_routes import get_current_user
from middlewares import generate_session
from models import add_product_to_user_bag
from store import User

bag_router = APIRouter()


@bag_router.post('/api/bag/{product_id}')
def add_product_to_bag(product_id: int, user: User = Depends(get_current_user),
                       session: Session = Depends(generate_session)) -> None:
    add_product_to_user_bag(product_id=product_id, user=user, session=session)
