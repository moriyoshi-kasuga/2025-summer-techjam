from flask import Blueprint, render_template

blueprint = Blueprint("admin", __name__)


@blueprint.route("/")
def admin():
    return render_template("admin.html")
