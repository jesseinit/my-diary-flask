import datetime as dt
from marshmallow import fields, ValidationError, validates, validates_schema
from schema.base_schema import BaseSchema
from schema.user_schema import UserSchema


class DiarySchema(BaseSchema):
    id = fields.UUID()
    title = fields.Str(required=True, error_messages={
                       "required": "You have not provided a title."})
    content = fields.Str(required=True, error_messages={
        "required": "You have not provided a diary content."})
    created_on = fields.DateTime()
    updated_on = fields.DateTime(default=dt.datetime.now())
    user = fields.Nested(UserSchema, exclude=(
        'password', 'push_sub', 'reminder', 'postCount',))

    @validates('title')
    def validate_title(self, title):
        if len(title) < 2 or len(title) > 100:
            raise ValidationError(
                'Your diary title should contain between 2 to 100 characters')

    @validates('content')
    def validate_content(self, content):
        # Todo: Validation to run when user enters diary body
        pass
