from marshmallow import Schema, fields


class TodoSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    is_completed = fields.Bool(default=False)
