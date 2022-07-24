from project.dao.base import BaseDAO
from project.dao.model.movie import Movies

from typing import Generic, List, Optional, TypeVar
from project.dao.model.base import Base
T = TypeVar('T', bound=Base)


class MovieDAO(BaseDAO):
    __model__ = Movies

    def get_all_order_by(self, page: Optional[int] = None, filter=None) -> List[T]:
        stmt = self._db_session.query(self.__model__)

        if filter:
            stmt = stmt.order_by(desc(self.__model__.year))
        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        return stmt.all()


