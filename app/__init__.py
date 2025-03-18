import os

from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

from app.config.config import config
from app.extensions import init_extensions
from app.routes import user_bp


def create_app(config_name=None):
    """Application factory for creating Flask app."""
    
    if config_name is None:
        config_name = os.environ.get("FLASK_CONFIG", "default")
    
    # Create app
    app = Flask(__name__, instance_relative_config=True)
    
    # Configure app
    app.config.from_object(config[config_name])
    
    # Ensure instance folder exists
    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        pass
    
    # Initialize extensions
    init_extensions(app)
    
    # Register Blueprints
    app.register_blueprint(user_bp)
    
    # Setup Swagger UI
    swagger_blueprint = get_swaggerui_blueprint(
        app.config["SWAGGER_URL"],
        app.config["API_URL"],
        config={"app_name": "Flask Users API"}
    )
    app.register_blueprint(swagger_blueprint, url_prefix=app.config["SWAGGER_URL"])
    
    @app.route("/health")
    def health_check():
        return {"status": "healthy"}, 200
    
    return app 