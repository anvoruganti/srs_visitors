from flask import Flask # type: ignore
from backend.config import Config
from backend.routes import init_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    init_routes(app)
    
    return app