from typing import Optional

from project.dao.base import BaseDAO
from project.dao.model.movie import Movies
from project.dao.movie import MovieDAO
from project.exceptions import ItemNotFound


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_item(self, pk: int) -> Movies:
        if movie := self.dao.get_by_id(pk):
            return movie
        raise ItemNotFound(f'Genre with pk={pk} not exists.')

    def get_all(self, filter=None, page: Optional[int] = None) -> list[Movies]:
        return self.dao.get_all_order_by(page=page, filter=filter)



