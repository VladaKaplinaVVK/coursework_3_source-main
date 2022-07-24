import base64
import hashlib
import hmac
from project.dao.user import UserDAO
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from typing import Optional
from project.dao.base import BaseDAO
from project.dao.model.user import Users
from project.exceptions import ItemNotFound
from project.tools.security import generate_password_hash, generate_token, approve_refresh_token, get_data_from_token


class UserService:

    def __init__(self, dao: UserDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Users:
        if user := self.dao.get_by_id(pk):
            return user
        raise ItemNotFound(f'User with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> list[Users]:
        return self.dao.get_all_sortid(page=page)

    def create_user(self, email, password):
        return self.dao.create(email, password)

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def check(self, email, password):
        user = get_by_email(email)
        return generate_token(email=user.email, password=password, password_hash=user.password)

    def update_token(self, refresh_token):
        return approve_refresh_token(refresh_token)

    def get_user_by_token(self, refresh_token):
        data = get_data_from_token(refresh_token)
        if data:
            return self.dao.get_by_email(data.get('email'))

    def update_user(self, data: dict, refresh_token):
        user = self.get_user_by_token(refresh_token)
        if user:
            self.dao.update(email=user.email, data=data)
            return self.get_user_by_token(refresh_token)

    def update_password(self, data, refresh_token):
        user = self.get_user_by_token(refresh_token)
        if user:
            self.dao.update(email=user.email, data={"password": generate_password_hash(data.get('password_2'))})
            return self.check(email=user.email, password=data.get('password_2'))
