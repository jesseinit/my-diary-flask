from marshmallow import ValidationError
import re


def validate_fullname(fullname):
    fullname = re.sub('\s+', ' ', fullname).strip()
    if not fullname:
        raise ValidationError('You have not entered a fullname')
    if len(fullname) < 2:
        raise ValidationError(
            'Your fullname must be atleast 2 characters long')
