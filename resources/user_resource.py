from flask_restful import Resource, abort
from flask import request
from app import (jwt_required, get_jwt_identity,
                 flask_bcrypt as BCrypt)
from schema.user_schema import UserSchema
from models.user_model import User as UserModel
from utils.handle_response import success_response, error_response
from helpers.validations import validate_json_request


class UserProfile(Resource):
    @jwt_required
    def get(self):
        """Method to handle user data retrieval"""
        exact_user = UserModel.query.filter_by(
            id=get_jwt_identity().get('id')).first()
        if not exact_user:
            return error_response(message="No associated account " +
                                  "with this email. 😩", status=404)
        user_data = UserSchema(exclude=['password']).dump(exact_user)
        return success_response(data=user_data)

    @jwt_required
    @validate_json_request(request)
    def put(self):
        """Method to handle user data update"""
        user_update_data = request.get_json(force=True)
        user_data = UserSchema(
            dump_only=['id']).load_object_into_schema(user_update_data)
        if user_data.get('password'):
            hashed_password = BCrypt.generate_password_hash(
                user_data.get('password')).decode('utf-8')
            user_data.update(password=hashed_password)
        exact_user = UserModel.query.filter_by(
            id=get_jwt_identity().get('id')).first()
        updated_user_object = exact_user.update(**user_data)
        return success_response(
            data=UserSchema(exclude=['password']).dump(
                updated_user_object),
            message='Profile Updated Successfully')
