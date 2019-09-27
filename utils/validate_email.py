import re
from marshmallow import ValidationError


def validate_email(email):
    email_patrn = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if not re.match(email_patrn, email):
        raise ValidationError('Kindly provide a valid email address')
