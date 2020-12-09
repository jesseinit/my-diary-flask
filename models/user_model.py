from ..app import db, flask_bcrypt as BCrypt
from .model_operations import Utility
from sqlalchemy import func, event, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class User(db.Model, Utility):
    """ User model for storing user related information """

    __tablename__ = "Users"
    id = db.Column(UUID(as_uuid=True), unique=True,
                   nullable=False, default=lambda: uuid4().hex,
                   primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    fullname = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime, server_default=func.now())
    push_sub = db.Column(db.JSON, default={}, nullable=False)
    reminder = db.Column(db.Boolean, default=False, nullable=False)
    diaries = relationship("Diary", back_populates="user", lazy='dynamic')

    def __init__(self, **kwargs):
        for field in list(kwargs.keys()):
            self.__dict__[field] = kwargs[field]

    def __repr__(self):
        return f"<User >>> {self.__dict__}>"


@event.listens_for(User, "before_insert")
def hash_user_password(mapper, connection, self):
    self.password = BCrypt.generate_password_hash(
        self.password).decode('utf-8')
