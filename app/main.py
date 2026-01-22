from flask import Flask

from app.config import get_config
from app.api.health import health_bp
from app.api.user import users_bp
from app.dependencies.container import container


def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())

    app.register_blueprint(health_bp)
    app.register_blueprint(users_bp)

    container.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app()

    app.run(host="0.0.0.0", port=5000)
