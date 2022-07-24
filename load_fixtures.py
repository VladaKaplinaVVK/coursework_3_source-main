from contextlib import suppress
from typing import Any, Dict, List, Type

from sqlalchemy.exc import IntegrityError

from project.config import config
from project.dao import base
from project.dao.model.director import Directors
from project.dao.model.genre import Genres
from project.dao.model.movie import Movies

from project.server import create_app
from setup_db import db
from project.utils import read_json


def load_data(data: List[Dict[str, Any]], model: Type[base.Base]) -> None:
    for item in data:
        item['id'] = item.pop('pk')
        db.session.add(model(**item))


if __name__ == '__main__':
    fixtures: Dict[str, List[Dict[str, Any]]] = read_json("fixtures.json")

    app = create_app(config)

    with app.app_context():
        # TODO: [fixtures] Добавить модели Directors и Movies
        load_data(fixtures['genres'], Genres)
        load_data(fixtures['directors'], Directors)
        load_data(fixtures['movies'], Movies)

        with suppress(IntegrityError):
            db.session.commit()
