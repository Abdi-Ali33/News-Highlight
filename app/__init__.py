from flask import Flask
from config import config_options
from .main import main as main_blueprint
from .requests import configure_request


def create_app(config_name):
    """
    Function to create an app instance
    """

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # register blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    configure_request(app)
    # Will add the views and forms

    return app
