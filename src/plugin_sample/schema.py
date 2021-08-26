from marshmallow import Schema, fields


class SampleObjectSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    message = fields.Str()
