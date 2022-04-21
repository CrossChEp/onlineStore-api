from typing import List

import bcrypt
from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.general_methods import clear_model
from schemas import UserPrivateModel, UserModel, UserRequestModel
from store import User


def add_user_to_database(user_data: UserPrivateModel, session: Session) -> None:
    user_data.password = bcrypt.hashpw(user_data.password.encode(), salt=bcrypt.gensalt())
    user = User(**user_data.dict())
    session.add(user)
    session.commit()


def get_all_users_from_database(session: Session) -> List[User]:
    users = session.query(User).all()
    return users


def get_concrete_user(user_data: UserRequestModel, session: Session) -> User:
    clean_user = clear_model(user_data)
    user = session.query(User).filter_by(**clean_user).first()
    if not user:
        raise HTTPException(status_code=404, detail='user not found')
    return user