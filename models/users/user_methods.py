from typing import List

import bcrypt
from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.general_methods import clear_model
from models.users.auxilary_methods import hash_password
from schemas import UserPrivateModel, UserModel, UserRequestModel, UserUpdateModel
from store import User


def add_user_to_database(user_data: UserPrivateModel, session: Session) -> None:
    """adds user to database

    :param user_data: UserPrivateModel
    :param session: Session
    :return: None
    """
    user_data.password = bcrypt.hashpw(user_data.password.encode(), salt=bcrypt.gensalt())
    user = User(**user_data.dict())
    session.add(user)
    session.commit()


def get_all_users_from_database(session: Session) -> List[User]:
    """gets all users from database

    :param session: Session
    :return: List[User]
    """
    users = session.query(User).all()
    return users


def get_concrete_user(user_data: UserRequestModel, session: Session) -> User:
    """gets only one user with special parameters

    :param user_data: UserRequestModel
        (user's data that will be used in search of user)
    :param session: Session
    :return: User
    """
    clean_user = clear_model(user_data)
    user = session.query(User).filter_by(**clean_user).first()
    if not user:
        raise HTTPException(status_code=404, detail='user not found')
    return user


def delete_user_from_database(user: User, session: Session) -> None:
    """deletes user from database

    :param user: User
    :param session: Session
    :return: None
    """
    session.delete(user)
    session.commit()


def update_user_in_database(user_update_data: UserUpdateModel, user: User, session: Session) -> None:
    """updates user's data

    :param user_update_data: UserUpdateModel
    :param user: User
    :param session: Session
    :return: None
    """
    user_query = session.query(User).filter_by(id=user.id)
    if user_update_data.password:
        user_update_data.password = hash_password(user_update_data.password)
    user_clean_model = clear_model(user_update_data)
    user_query.update(user_clean_model)
    session.commit()
