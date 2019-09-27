from app import db
from helpers.database_helpers import Utility
from sqlalchemy import func, ForeignKey, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class Diary(db.Model, Utility):
    """ Diary model for storing user's diary information """

    __tablename__ = "diaries"
    id = db.Column(UUID(as_uuid=True), unique=True,
                   nullable=False, default=lambda: uuid4().hex,
                   primary_key=True)
    user_id = db.Column(UUID(as_uuid=True), ForeignKey("users.id"))
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_on = db.Column(db.DateTime, server_default=func.now())
    updated_on = db.Column(db.DateTime, onupdate=func.now())
    deleted = db.Column(db.Boolean, default=False, nullable=False)
    user = relationship("User", back_populates="diaries", lazy=True)

    def __init__(self, **kwargs):
        for field in list(kwargs.keys()):
            self.__dict__[field] = kwargs[field]

    def __repr__(self):
        return f"<Diary >>> {self.__dict__}>"
