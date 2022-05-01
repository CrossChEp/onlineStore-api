from typing import List

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from api_routers.auth_routes import get_current_user
from middlewares import generate_session
from models import add_user_to_database, get_all_users_from_database, get_concrete_user, delete_user_from_database, \
    update_user_in_database
from schemas import UserPrivateModel, UserModel, UserRequestModel, UserUpdateModel
from store import User

user_router = APIRouter()


@user_router.post('/api/register')
def register_user(user_data: UserPrivateModel,
                  session: Session = Depends(generate_session)) -> None:
    """register user using user's data

    :param user_data: UserPrivateModel
        (user's data)
    :param session: Session
    :return: None
    """
    add_user_to_database(user_data, session=session)


@user_router.get('/api/users', response_model=List[UserModel])
def get_users(session: Session = Depends(generate_session)) -> List[User]:
    """gets all users from database

    :param session: Session
    :return: List[User]
    """
    return get_all_users_from_database(session)


@user_router.get('/api/user/{id}', response_model=UserModel)
def get_user(user_id: int, session: Session = Depends(generate_session)) -> User:
    """gets one user using user_id

    :param user_id: int
        (user's id)
    :param session: Session
    :return: User
    """
    return get_concrete_user(UserRequestModel(id=user_id), session=session)


@user_router.delete('/api/user/{id}')
def delete_user(user: User = Depends(get_current_user),
                session: Session = Depends(generate_session)) -> None:
    """deletes user from database using user's token

    :param user: user's token
    :param session: Session
    :return: None
    """
    delete_user_from_database(user, session=session)


@user_router.put('/api/user')
def update_user(user_update_data: UserUpdateModel, user: User = Depends(get_current_user),
                session: Session = Depends(generate_session)) -> None:
    """updates user using user's token and user's update data

    :param user_update_data: UserUpdateModel
        (user's update data)
    :param user: User
        (current user)
    :param session: Session
    :return: None
    """
    update_user_in_database(user_update_data, user, session)
