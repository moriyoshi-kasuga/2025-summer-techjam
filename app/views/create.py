from flask import Blueprint, render_template

blueprint = Blueprint("create", __name__)


@blueprint.route("/")
def create():
    return render_template("create.html")
