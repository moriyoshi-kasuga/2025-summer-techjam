from datetime import datetime
import base64

from flask import Blueprint, current_app, redirect, render_template, request
from flask_login import current_user, login_required

from app import db, socketio
from app.models import Post, User
from app.views.image import save_image

blueprint = Blueprint("create", __name__)


@blueprint.route("/", methods=["GET", "POST"])
@login_required
def create():
    user_id = current_user.id
    if request.method == "GET":
        username = User.query.get(user_id).name
        date = datetime.now()
        return render_template(
            "create.html", username=username, month=date.month, day=date.day
        )
    content = request.form.get("content")
    image_data_url = request.form.get("image")
    if content is None or len(content) == 0:
        return render_template("create.html")
    current_app.logger.info("hey")
    post = Post(content=content, author_id=user_id)
    db.session.add(post)
    db.session.commit()
    # Remove the "data:image/png;base64," prefix
    image_data = base64.b64decode(image_data_url.split(",")[1])
    save_image(post.id, image_data)
    socketio.emit("new_post")
    return redirect("/view")
