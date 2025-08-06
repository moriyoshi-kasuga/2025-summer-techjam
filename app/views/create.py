from datetime import datetime

from flask import Blueprint, render_template
from flask_login import current_user, login_required

from app.models import User

blueprint = Blueprint("create", __name__)


@blueprint.route("/")
@login_required
def create():
    id = current_user.id
    username = User.query.get(id).name
    date = datetime.now()
    return render_template(
        "create.html", username=username, month=date.month, day=date.day
    )
