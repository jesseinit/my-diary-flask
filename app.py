import os
from config import config
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager, jwt_required, get_current_user, get_jwt_identity,
    verify_jwt_in_request, get_jwt_claims)
from flask_bcrypt import Bcrypt
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from dotenv import load_dotenv


load_dotenv()
db = SQLAlchemy()
flask_bcrypt = Bcrypt()
jwt = JWTManager()


def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    api = Api(app, prefix='/api/v1/')
    app.config.from_object(config[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)
    jwt.init_app(app)

    # Imports to prevent cyclic imports
    from helpers.validations import (
        ValidationError, no_auth_header_handler, unsigned_token_handler,
        my_expired_token_handler)
    from resources.auth_resource import LoginUser, SignupUser
    from resources.user_resource import UserProfile
    from resources.diary_resource import DairyResource, SingleDiaryResource

    # Endpoints
    api.add_resource(LoginUser, "auth/login")
    api.add_resource(SignupUser, "auth/signup")
    api.add_resource(UserProfile, "user/profile")
    api.add_resource(DairyResource, "user/diaries")
    api.add_resource(SingleDiaryResource, "user/diary/<diary_id>")

    @app.errorhandler(ValidationError)
    def handle_exception(error):
        """Error handler called when a ValidationError Exception is raised"""

        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    jwt.unauthorized_loader(no_auth_header_handler)
    jwt.invalid_token_loader(unsigned_token_handler)
    jwt.expired_token_loader(my_expired_token_handler)

    return app


# app = create_app(os.getenv("FLASK_ENV") or "dev")
# app.app_context().push()
