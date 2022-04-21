from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

from middlewares import generate_session
from models import authenticate_user, create_access_token
from models.auth.auth import get_current_user
from schemas import Token, UserModel

auth_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@auth_router.post('/token', response_model=Token)
def login_for_token(form_data: OAuth2PasswordRequestForm = Depends(),
                    session: Session = Depends(generate_session)) -> Token:
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
def read_user_me(token: str = Depends(oauth2_scheme), session: Session = Depends(generate_session)):
    current_user = get_current_user(session, token)
    return current_user
