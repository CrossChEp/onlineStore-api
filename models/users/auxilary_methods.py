from typing import List

from schemas import UserModel
from store import User


def generate_user_model_list(user: User) -> UserModel:
    user_model = UserModel(
        id=user.id,
        username=user.username
    )
    return user_model


def convert_to_user_model_list(users: List[User]) -> List[UserModel]:
    user_models_list = []
    for user in users:
        user_model = generate_user_model_list(user)
        user_models_list.append(user_model)
    return user_models_list
