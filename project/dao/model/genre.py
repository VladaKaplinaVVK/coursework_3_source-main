from marshmallow import Schema, fields

from project.dao.model.base import Base
from setup_db import db


class Genres(Base):
    __tablename__ = 'genres'

    name = db.Column(db.String(100), unique=True, nullable=False)


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()

