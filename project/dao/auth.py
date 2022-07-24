from project.dao.base import BaseDAO
from project.dao.model.auth import UserCreateSchema
from project.dao.model.user import Users


class AuthDAO(BaseDAO):

    def create(self, email: str, password: str):
        new_user = Users(email=email, password=password)
        self.session.add(new_user)
        self.session.commit()
        return UserCreateSchema().dump(new_user)
