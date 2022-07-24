from marshmallow import Schema, fields


class UserCreateSchema(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)
