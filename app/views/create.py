from flask import Blueprint, redirect, render_template, request
from flask_login import current_user, login_required

from app import db
from app.models import Post, User
from app.views.image import save_image

blueprint = Blueprint("create", __name__)


@blueprint.route("/", methods=["GET", "POST"])
@login_required
def create():
    user: User = current_user
    if request.method == "GET":
        return render_template("create.html")
    content = request.form.get("content")
    image = request.files.get("image")
    if content is None or len(content) == 0:
        return render_template("create.html")
    post = Post(content=content, author_id=user.id)
    db.session.add(post)
    db.session.commit()
    save_image(post.id, image)
    return redirect("/view")
