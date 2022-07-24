from typing import Optional

from project.dao.base import BaseDAO
from project.dao.model.genre import Genres
from project.exceptions import ItemNotFound


class GenreService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Genres:
        if genre := self.dao.get_by_id(pk):
            return genre
        raise ItemNotFound(f'Genre with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> list[Genres]:
        return self.dao.get_all_sortid(page=page)
