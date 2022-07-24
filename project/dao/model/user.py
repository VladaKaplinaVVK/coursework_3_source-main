from marshmallow import Schema, fields

from project.dao.model.base import Base
from project.dao.model.genre import Genres
from setup_db import db


class Users(Base):
    __tablename__ = 'users'

    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    favourite_genre = db.Column(db.Integer, db.ForeignKey(Genres.id), nullable=False)
    genre = db.relationship("Genres")




class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Str()

