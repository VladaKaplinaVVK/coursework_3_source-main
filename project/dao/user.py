from project.dao.base import BaseDAO
from project.dao.model.user import Users
from project.tools.security import generate_password_hash


class UserDAO(BaseDAO[Users]):
    __model__ = Users

    def create(self, email, password):
        try:
            self.db_session.add(
                Users(
                    email=email,
                    password=generate_password_hash(password)
                )
            )
            self.db_session.commit()
        except Exception as e:
            print(e)
            self.db_session.rollback()

    def get_user_by_email (self, email):
        try:
            stmt = self.db_session.query(self.__model__).filter(self.__model__.email==email).one()
            return stmt
        except Exception as e:
            print(e)
            self.db_session.rollback()

    def update(self, email, data):
        try:
            self.db_session.query(self.__model__).filter(self.__model__.email == email).update(
                data
            )
            self.db_session.commit()
        except Exception as e:
            print(e)
            self.db_session.rollback()
