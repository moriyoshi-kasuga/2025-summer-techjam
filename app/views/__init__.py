from app import app

from . import (
    admin,
    create,
    details,
    favorites,
    home,
    image,
    login,
    mypage,
    signup,
    view,
)

app.register_blueprint(home.blueprint)
app.register_blueprint(image.blueprint, url_prefix="/image")
app.register_blueprint(login.blueprint, url_prefix="/login")
app.register_blueprint(mypage.blueprint, url_prefix="/mypage")
app.register_blueprint(signup.blueprint, url_prefix="/signup")
app.register_blueprint(view.blueprint, url_prefix="/view")
app.register_blueprint(create.blueprint, url_prefix="/create")
app.register_blueprint(admin.blueprint, url_prefix="/admin")
app.register_blueprint(details.blueprint, url_prefix="/details")
app.register_blueprint(favorites.blueprint, url_prefix="/favorites")
