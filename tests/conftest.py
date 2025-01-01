import pytest
from app import create_app
from app import db
from app.models import User
from flask_jwt_extended import create_access_token

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": 'sqlite:///app.db',
    })
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def create_test_user():
    user = User(username="testuser", password=User.hash_password("password"))
    db.session.add(user)
    db.session.commit()
    return user


@pytest.fixture(scope="function")
def general_token(app):
    from flask_jwt_extended import create_access_token
    from app.models import User
    test_user = User.query.filter_by(username="testuser").first()
    return create_access_token(identity=str(test_user.id))

