import re
from functools import wraps

# Third-Party Imports
from flask_restful import abort
from flask import jsonify

# Schemas
from schema.auth_schema import LoginSchema, SignUpSchema
from schema.diary_schema import DiarySchema

# Utils
from utils.validate_password import validate_password
from utils.validate_email import validate_email


class ValidationError(Exception):
    """Base Validation class for handling validation errors"""

    def __init__(self, error, status_code=None):
        Exception.__init__(self)
        self.status_code = 400
        self.error = error
        self.error['status'] = 'error'
        self.error['message'] = error['message']

        if status_code:
            self.status_code = status_code

    def to_dict(self):
        return self.error


def validate_signup(request):
    def decorator(func):
        @wraps(func)
        def wrapper_function(*args, **kwargs):
            signup_details = request.get_json(force=True)
            SignUpSchema().load_object_into_schema(signup_details)
            return func(*args, **kwargs)
        return wrapper_function
    return decorator


def validate_login(request):
    def decorator(func):
        @wraps(func)
        def wrapper_function(*args, **kwargs):
            login_details = request.get_json(force=True)
            LoginSchema().load_object_into_schema(login_details)
            return func(*args, **kwargs)
        return wrapper_function
    return decorator


def validate_json_request(request):
    """Decorator function to check for json content type in request"""

    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if (not request.data.decode('utf-8') or not request.is_json or
                    not request.get_json(force=True).keys()):
                raise ValidationError(
                    {
                        'status': 'error',
                        'message': 'Empty JSON Request'
                    }, 400)
            return func(*args, **kwargs)
        return decorated_function
    return decorator


def validate_payload(request, type_name):
    """
        Payload validator for different schemas
        Args:
            request(object): Flask request object
            type_name(string): Name of the entity for which the validation
            should be carried on its schema
        Returns:
            An error in the case of a failed schema validation or calls the
            wrapped/decorated function.
    """
    def decorator(func):
        @wraps(func)
        def wrapper_function(*args, **kwargs):
            entity_details = request.get_json(force=True)
            entity_schema = {
                'sign_up': SignUpSchema(),
                'login': LoginSchema(),
                'create_diary': DiarySchema()
            }
            entity_schema[type_name].load_object_into_schema(entity_details)
            return func(*args, **kwargs)
        return wrapper_function
    return decorator


def no_auth_header_handler(error_message):
    """
        Unauthorized token handler that is called when user has not
        set authorization header or passed a token.

        Args:
        error_message(string): A string with the default error message
    """
    return jsonify({
        'status': 401,
        'message': error_message
    }), 401


def unsigned_token_handler(error_message):
    """
        Invalid token handler that is called when user passed a token not
        signed by the application.

        Args:
            error_message(string): A string with the default error message
    """
    return jsonify({
        'status': 400,
        'message': 'Cannot verify the provided token'
    }), 400


def my_expired_token_handler(expired_token):
    """
        Expired token handler that is called when user passed a token has
        expired.

        Args:
            expired_token(dict): A dict containing expired token details
    """
    return jsonify({
        'status': 400,
        'message': 'The provided token has expired'
    }), 401


def validate_uuid(uuid_string):
    """ Helper function to validate a uuid string """
    from uuid import UUID
    try:
        UUID(uuid_string, version=4)
    except ValueError:
        raise ValidationError(
            {
                'status': 'error',
                'message': 'Diary ID was badly formed - UUID Expected'
            }, 400)
