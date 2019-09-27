from marshmallow import ValidationError


def validate_password(password):
    if not password:
        raise ValidationError('You have not entered a password')
    if len(password) < 8:
        raise ValidationError('Password cannot be less than 8 characters')
