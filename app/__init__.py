import os

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder="static", template_folder="templates")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or "dev-secret-key"

db = SQLAlchemy(app)
migrate = Migrate(app, db)
socketio = SocketIO(app, async_mode="gevent", cors_allowed_origins="*")

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = "login.login"


@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))


from app import models, views  # noqa: E402, F401
