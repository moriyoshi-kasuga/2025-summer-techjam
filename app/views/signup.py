from flask import Blueprint, render_template

blueprint = Blueprint("signup", __name__)


@blueprint.route("/")
def signup():
    return render_template("signup.html")
