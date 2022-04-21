from typing import Optional

from pydantic import BaseModel


class UserModelAbstract(BaseModel):
    username: str

    class Config:
        orm_mode = True


class UserPrivateModel(UserModelAbstract):
    password: str

    class Config:
        orm_mode = True


class UserModel(UserModelAbstract):
    id: int

    class Config:
        orm_mode = True


class UserRequestModel(BaseModel):
    id: Optional[int]
    username: Optional[str]
