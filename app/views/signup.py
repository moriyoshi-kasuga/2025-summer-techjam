from flask import Blueprint, redirect, render_template, request
from flask_login import login_user

from app import db
from app.models import User

blueprint = Blueprint("signup", __name__)


@blueprint.route("/", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")
    if password is None:
        return render_template("signup.html", error="パスワードを入力してください")
    confirm_password = request.form.get("confirm_password")
    if password != confirm_password:
        return render_template("signup.html", error="パスワードが一致しません")
    user: User | None = User.query.filter(User.email == email).first()
    if user:
        return render_template("signup.html", error="入力されたemailは既に登録済みです")

    user = User(name=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()

    login_user(user)

    return redirect("/create")

