from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()


def init_extensions(app):
    engine_options = {
        "pool_pre_ping": True,
        "pool_recycle": 300,
    }
    
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = engine_options
    
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    
    with app.app_context():
        try:
            db.engine.connect()
            print("Successfully connected to the database.")
        except Exception as e:
            print(f"Error connecting to db: {e}")
            print(f"URL: {app.config.get('SQLALCHEMY_DATABASE_URI')}")
