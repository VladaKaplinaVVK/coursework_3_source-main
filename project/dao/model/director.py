from marshmallow import Schema, fields

from project.dao.model.base import Base
from setup_db import db


class Directors(Base):
    __tablename__ = 'directors'

    name = db.Column(db.String(100), unique=True, nullable=False)


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
