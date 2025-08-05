from flask import Blueprint, render_template

blueprint = Blueprint("view", __name__)


@blueprint.route("/")
def view():
    return render_template("view.html")
