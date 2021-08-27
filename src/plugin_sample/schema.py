from marshmallow import Schema, fields


class TodoSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    is_completed = fields.Bool()
    created_at = fields.DateTime()
