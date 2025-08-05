from flask import Blueprint, render_template

blueprint = Blueprint("mypage", __name__)


@blueprint.route("/")
def mypage():
    return render_template("mypage.html")
