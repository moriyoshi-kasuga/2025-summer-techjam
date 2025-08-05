from app import app

from . import home, image

app.register_blueprint(home.blueprint)
app.register_blueprint(image.blueprint, url_prefix="/image")
