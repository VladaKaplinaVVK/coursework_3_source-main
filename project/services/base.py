from typing import TypeVar, Generic

from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound


T = TypeVar('T', bound=BaseDAO)


class BaseService(Generic[T]):
    def __init__(self, dao: T, *args, **kwargs):
        self.dao = dao
