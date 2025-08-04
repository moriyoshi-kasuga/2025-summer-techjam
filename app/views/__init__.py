from app import app

from . import home

app.register_blueprint(home.blueprint)
