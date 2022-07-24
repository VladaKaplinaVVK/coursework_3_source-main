from project.dao.base import BaseDAO
from project.dao.model.director import Directors


class DirectorDAO(BaseDAO):
    __model__ = Directors

