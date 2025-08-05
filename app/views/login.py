from flask import Blueprint, render_template

blueprint = Blueprint("login", __name__)


@blueprint.route("/")
def login():
    return render_template("login.html")
