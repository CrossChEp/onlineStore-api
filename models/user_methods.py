import bcrypt
from sqlalchemy.orm import Session

from schemas import UserPrivateModel
from store import User


def add_user_to_database(user_data: UserPrivateModel, session: Session) -> None:
    user_data.password = bcrypt.hashpw(user_data.password.encode(), salt=bcrypt.gensalt())
    user = User(**user_data.dict())
    session.add(user)
    session.commit()
