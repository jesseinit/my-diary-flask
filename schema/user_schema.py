# from app import ma
from marshmallow import fields
from ..schema.base_schema import BaseSchema
from ..utils.validate_email import validate_email
from ..utils.validate_password import validate_password
from ..utils.validate_fullname import validate_fullname


class UserSchema(BaseSchema):
    id = fields.UUID()
    email = fields.Email(validate=validate_email)
    password = fields.Str(validate=validate_password)
    fullname = fields.Str(validate=validate_fullname)
    created_on = fields.DateTime(data_key='memberSince')
    push_sub = fields.Dict(data_key='pushSub')
    reminder = fields.Bool()
    postCount = fields.Function(
        lambda model_instance: model_instance.diaries.
        filter_by(deleted=False).count())
