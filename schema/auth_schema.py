# from app import ma
import re
from marshmallow import fields
from schema.base_schema import BaseSchema
#
from utils.validate_email import validate_email
from utils.validate_password import validate_password
from utils.validate_fullname import validate_fullname


class LoginSchema(BaseSchema):
    email = fields.Str(validate=validate_email, required=True,
                       error_messages={
                           "required": "You have not provided a email."})
    password = fields.Str(validate=validate_password, required=True,
                          error_messages={
                              "required": "You have not provided a password."})


class SignUpSchema(LoginSchema):
    fullname = fields.Str(required=True, validate=validate_fullname,
                          error_messages={"required": "Enter your fullname."})
