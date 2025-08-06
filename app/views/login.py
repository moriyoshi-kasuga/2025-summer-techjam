from flask import Blueprint, redirect, render_template, request
from flask_login import login_user

from app.models import User

blueprint = Blueprint("login", __name__)


@blueprint.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    email = request.form.get("email")
    password = request.form.get("password")
    user: User | None = User.query.filter(User.email == email).first()
    if user is None:
        return render_template("login.html", error="入力されたemailはアカウント登録されていません")

    if user.password != password:
        return render_template("login.html",error="パスワードが間違っています。再度ご入力ください。")

    login_user(user)

    return redirect("/mypage")
