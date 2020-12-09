from app import flask_bcrypt as BCrypt
from flask_jwt_extended import create_access_token
from flask_restful import Resource
from flask import request

from models.user_model import User as UserModel
from schema.user_schema import UserSchema
from helpers.validations import (validate_login, validate_signup,
                                   validate_json_request)
from utils.handle_response import success_response, error_response


class LoginUser(Resource):
    @validate_json_request(request)
    @validate_login(request)
    def post(self):
        user_info = request.get_json(force=True)
        exact_user = UserModel.query.filter_by(
            email=user_info['email']).first()
        if not exact_user:
            return error_response(message="No associated account " +
                                  "with this email. 😩", status=404)
        is_valid_password = BCrypt.check_password_hash(
            exact_user.password, user_info['password'])
        if not is_valid_password:
            return error_response(message="Email or Password " +
                                  "is not correct 😕", status=401)
        user_schema = UserSchema(exclude=['password', 'push_sub'])
        user_info = user_schema.dump(exact_user)
        token = create_access_token(identity={"id": exact_user.id})
        return success_response(message='Logged in successfuly',
                                data=dict(token=token, user=user_info),
                                status=200)


class SignupUser(Resource):
    """User registration resource"""
    @validate_json_request(request)
    @validate_signup(request)
    def post(self):
        user_info = request.get_json(force=True)
        existing_user = UserModel.query.filter_by(
            email=user_info['email']).first()
        if existing_user:
            return error_response(message="This email address" +
                                  " has been taken", status=409)
        new_user = UserModel(**user_info)
        new_user.save()

        return success_response(
            message="Your account has been created successfully",
            data=UserSchema(exclude=['password']).dump(new_user), status=201)
