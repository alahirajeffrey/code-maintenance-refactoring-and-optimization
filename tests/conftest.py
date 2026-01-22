import pytest
from flask import Flask

from app.api.user import users_bp
from app.api.health import health_bp
from app.config.testing import TestingConfig


@pytest.fixture
def app():
    app = Flask(__name__)
    app.config.from_object(TestingConfig)

    app.register_blueprint(users_bp)
    app.register_blueprint(health_bp)

    return app


@pytest.fixture
def client(app):
    return app.test_client()
