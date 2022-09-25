from .blueprints.default.views import default
from .helpers import set_flask_environment
from .blueprints.extensions import db
from .extensions import migrate
from flask import Flask
from dotenv import load_dotenv

load_dotenv()


def create_app():

    """Create the Flask app."""
    app = Flask(__name__)

    set_flask_environment(app)

    app.register_blueprint(default)

    db.init_app(app=app)
    migrate.init_app(app, db)

    # shell context for flask cli
    app.shell_context_processor({'app': app, 'db':db})

    return app
