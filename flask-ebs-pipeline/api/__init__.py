from .blueprints.default.views import default
from .helpers import set_flask_environment
from .blueprints.extensions import db
from .extensions import migrate
from flask import Flask
from dotenv import load_dotenv

load_dotenv()


def create_app():

    """Create the Flask app."""
    application = Flask(__name__)

    set_flask_environment(application)

    application.register_blueprint(default)

    db.init_app(app=application)
    migrate.init_app(application, db)

    # shell context for flask cli
    application.shell_context_processor({'application': application, 'db':db})

    return application
