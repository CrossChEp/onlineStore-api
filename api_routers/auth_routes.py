from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from starlette import status

from configs import ALGORITHM, SECRET_KEY, credetials_exception
from middlewares import generate_session
from models import authenticate_user, create_access_token, get_concrete_user
from schemas import Token, UserModel, TokenData, UserRequestModel
from store import User

auth_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(session: Session = Depends(generate_session),
                     token: str = Depends(oauth2_scheme)) -> User:
    """gets current user using token

    :param session: Session
    :param token: str
        (jwt token of user)
    :return: User
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get('id')
        if not user_id:
            raise credetials_exception
        token = TokenData(id=user_id)
    except JWTError:
        raise credetials_exception
    user = get_concrete_user(UserRequestModel(id=token.id), session)
    if not user:
        raise credetials_exception
    return user


@auth_router.post('/token', response_model=Token)
def login_for_token(form_data: OAuth2PasswordRequestForm = Depends(),
                    session: Session = Depends(generate_session)) -> Token:
    """

    :param form_data: OAuth2PasswordRequestForm
        (oauth2 form)
    :param session: Session
    :return: Token
    """
    user = authenticate_user(
        username=form_data.username,
        password=form_data.password,
        session=session
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(user.id)
    return Token(access_token=access_token, token_type='bearer')


@auth_router.get('/user/me', response_model=UserModel)
def read_user_me(current_user: User = Depends(get_current_user)) -> User:
    """gets current user

    :param current_user: User
        (current user)
    :return: User
    """
    return current_user
