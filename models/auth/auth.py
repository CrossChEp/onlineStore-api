from jose import jwt, JWTError
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from configs import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM, credetials_exception
from models import get_concrete_user
from schemas import UserRequestModel, TokenData
from store import User
from datetime import timedelta, datetime


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_password(password, hashed_password) -> bool:
    return pwd_context.verify(password, hashed_password)


def authenticate_user(username: str, password: str, session: Session) -> User:
    """Returns user if user in db and has the same password, or False,
    if something went wrong

    :param username: str
    :param password: str
    :param session: Session
    :return: User, bool
    """
    user = get_concrete_user(user_data=UserRequestModel(username=username), session=session)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(user_id: int) -> str:
    """creates access token

    :param user_id: int
    :return: str
    """
    to_encode = {'id': user_id}
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt



