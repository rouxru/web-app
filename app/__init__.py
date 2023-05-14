"""Initialize app."""
from flask import Flask

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    """Construct the core app object."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    # Initialize Plugins
    db.init_app(app)

    with app.app_context():
        from .assets import compile_static_assets

        # Register Blueprints
        from app.home.home_blueprints import home_blueprints
        app.register_blueprint(home_blueprints)

        # Create Database Models
        db.create_all()
        db.session.commit()

        return app
