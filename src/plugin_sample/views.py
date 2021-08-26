from flask import request
from .schema import SampleObjectSchema


def home():
    # Validate input with marshmallow
    if request.method == 'POST':
        schema = SampleObjectSchema().load(request.data)
    return 'Hello World'
