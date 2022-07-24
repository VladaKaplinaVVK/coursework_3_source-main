from marshmallow import Schema, fields

from project.dao.model.base import Base
from setup_db import db


class Movies(Base):
    __tablename__ = 'movies'

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    trailer = db.Column(db.String(100),  nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"), nullable=False)
    genre = db.relationship("Genres")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"), nullable=False)
    director = db.relationship("Directors")


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
