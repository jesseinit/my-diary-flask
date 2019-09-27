import pytest
from app import create_app, db
from models.diary_model import *
from models.user_model import *

pytest_plugins = [
    "test.entities.test_user_resource"
]


@pytest.fixture(scope='module')
def client():
    app = create_app('test')
    testing_client = app.test_client()

    with app.app_context():
        db.create_all()
        yield testing_client
        db.session.close()
        db.drop_all()
