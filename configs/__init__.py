from fastapi import HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED

SECRET_KEY = '.AvbsFG1Ro5hx,k2DMdSg307z!uTJ9NqViOjEWny?lUaCtrYIX4-KLHw_Bc6mfpe8QZP'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
credetials_exception = HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )