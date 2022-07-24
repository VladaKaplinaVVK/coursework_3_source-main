import base64
import hashlib
import calendar
import datetime
import jwt
# from project.config import JWT_SECRET, JWT_ALG
from project.config import BaseConfig
from flask import current_app


def __generate_password_digest(password: str) -> bytes:
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=current_app.config["PWD_HASH_SALT"],
        iterations=current_app.config["PWD_HASH_ITERATIONS"],
    )


def generate_password_hash(password: str) -> str:
    return base64.b64encode(__generate_password_digest(password)).decode('utf-8')


def compare_password(other_password, password_hash):
    return password_hash == generate_password_hash(other_password)


def generate_token(email,  password, password_hash=None, is_refresh=False):

    if email is None:
        return False

    if not is_refresh:
        if not compare_password(other_password=password, password_hash=password_hash):
            return False

    data = {
        "email": email,
        "password": password,
        "id": id
    }

    mi30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    data["exp"] = calendar.timegm(mi30.timetuple())
    access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALG)

    mi30 = datetime.datetime.utcnow() + datetime.timedelta(days=30)
    data["exp"] = calendar.timegm(mi30.timetuple())
    refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALG)
    return {"access_token": access_token, "refresh_token": refresh_token}


def approve_refresh_token(refresh_token):
    data = jwt.decode(refresh_token, JWT_SECRET, algorithms=[JWT_ALG])
    email = data.get("email")
    password = data.get("password")

    return generate_tokens(email, password, is_refresh=True)


def get_data_from_token(refresh_token):
    try:
        data = jwt.decode(refresh_token, JWT_SECRET, algorithms=[JWT_ALG])
        return data
    except Exception:
        return None
