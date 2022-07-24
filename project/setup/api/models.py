from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссеры', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Тарантино'),
})


movie: Model = api.model('Фильмы', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Криминально чтиво'),
    'description': fields.String(required=True, max_length=100, example='много слов'),
    'trailer': fields.String(required=True, max_length=100, example='много слов'),
    'year': fields.Integer(required=True, max_length=100, example='1997'),
    'rating': fields.Float(required=True, max_length=100, example='9'),
    'genre_id': fields.Nested(genre),
    'director_id': fields.Nested(director),
})


user: Model = api.model('Пользователи', {
    'id': fields.Integer(required=True, example=1),
    'email ': fields.String(required=True, max_length=100, example='gbf_dhfvkb@fhgof'),
    'password ': fields.String(required=True, max_length=100, example='hgjtldhs'),
    'name ': fields.String(required=True, max_length=100, example='VOVA'),
    'surname  ': fields.String(required=True, max_length=100, example='VLADIMOV'),
    'genre  ': fields.Nested(genre),
})
