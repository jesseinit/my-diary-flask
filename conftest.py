import pytest
from app import create_app, db


@pytest.fixture(scope='module')
def init_db():
    # Create the database and the database table
    db.create_all()
    print("setup DB>>>>>>>")
    yield db
    print("teardown DB>>>>>>>")
#   db.drop_all()


@pytest.fixture(scope='module')
def client():
    app = create_app('test')
    with app.test_client() as client:
        yield client
