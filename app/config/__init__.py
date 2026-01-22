import os

from .development import DevelopmentConfig
from .production import ProductionConfig
from .testing import TestingConfig


def get_config():
    env = os.getenv("FLASK_ENV", "development")

    if env == "production":
        return ProductionConfig
    if env == "testing":
        return TestingConfig

    return DevelopmentConfig
