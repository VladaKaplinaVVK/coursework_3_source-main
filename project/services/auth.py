import calendar
import datetime
import jwt
from constants import JWT_SECRET, JWT_ALG
from project.dao.auth import AuthDAO
from project.services.base import BaseService
from project.services.user_service import UserService
import base64
import hashlib
from flask import current_app


class AuthService(BaseService(AuthDAO)):
    @staticmethod
    def __get_hash(self, password: str):
        hashed = hashlib.pbkdf2_hmac(
            hash_name=current_app.config['HASH_NAME'],
            hash_salt=current_app.config['HASH_SALT'].encode('utf-8'),
            hash_iterations=current_app.config['HASH_ITERATIONS'],
            password=password.encode('utf-8')
        )
        return base64.b64encode(hashed).decode('utf-8')

    def register(self, email: str, password: str):
        # "пароль"
        password = self.__get_hash(password=password)
        #"пользователь"
        return self.dao.create(email=email, password=password)


    def generate_token(self, username, password, is_refresh=False):
        user = self.user_service.get_one(username)
        if not user:
            return False

        if not is_refresh:
            if not self.user_service.compare_password(user.password, password):
                return False

        data = {
            "username": user.username,
            "role": user.role
        }

        mi30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(mi30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALG)

        mi30 = datetime.datetime.utcnow() + datetime.timedelta(days=30)
        data["exp"] = calendar.timegm(mi30.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALG)
        return {"access_token": access_token, "refresh_token": refresh_token}

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(refresh_token, JWT_SECRET, algorithms=[JWT_ALG])
        username = data['username']
        user = self. user_service.get_by_username(username)

        if not user:
            return False

        return self.generate_tokens(username. user.password, is_refresh=True)
