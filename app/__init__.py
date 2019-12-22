from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from core import bp as core_bp
from config.development import DevelopmentConfig as Config


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    app.config.from_pyfile('config.py')

    app.register_blueprint(core_bp)

    db.init_app(app)
    migrate.init_app(app, db)

    return app
