from typing import Optional

from pydantic import BaseModel


class UserModelWithOptionalFieldsAbstract(BaseModel):
    username: Optional[str]

    class Config:
        orm_mode = True


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


class UserRequestModel(UserModelWithOptionalFieldsAbstract):
    id: Optional[int]

    class Config:
        orm_mode = True


class UserUpdateModel(UserModelWithOptionalFieldsAbstract):
    password: Optional[str]

    class Config:
        orm_mode = True
