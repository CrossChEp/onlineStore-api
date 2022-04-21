from typing import List

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from middlewares import generate_session
from models import add_user_to_database
from schemas import UserPrivateModel, UserModel

user_router = APIRouter()


@user_router.post('/api/register')
def register_user(user_data: UserPrivateModel,
                  session: Session = Depends(generate_session)):
    add_user_to_database(user_data, session=session)


@user_router.get('/api/users', response_model=UserModel)
def get_users(session: Session = Depends(generate_session)) -> List[UserModel]:
    pass
