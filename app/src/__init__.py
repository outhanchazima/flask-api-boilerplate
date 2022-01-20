from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.src.config import config_by_name
from flask_cors import CORS
import os
from app.src.config import Config

from flask_sse import sse


db = SQLAlchemy()

def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.config["REDIS_URL"] = Config.REDIS_URL
    app.register_blueprint(sse, url_prefix='/stream')
    app.config['MONGODB_SETTINGS'] = {
        'host':'mongodb://localhost:27017/apibitsgap'
    }
    CORS(app)
    db.init_app(app)
    return app

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')