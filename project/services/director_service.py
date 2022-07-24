from project.dao.director import DirectorDAO
from typing import Optional

from project.dao.base import BaseDAO
from project.dao.model.director import Directors

from project.exceptions import ItemNotFound


class DirectorService:
    def __init__(self, dao: BaseDAO):
        self.dao = dao

    def get_item(self, pk: int) -> Directors:
        if director := self.dao.get_by_id(pk):
            return director
        raise ItemNotFound(f'Director with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> list[Directors]:
        return self.dao.get_all(page=page)

