from datetime import datetime
from typing import List

from flask import Blueprint, render_template
from flask_login import current_user, login_required

from app.models import Post, User

blueprint = Blueprint("mypage", __name__)


@blueprint.route("/")
@login_required
def mypage():
    user: User = current_user
    posts: List[Post] = (
        Post.query.filter(Post.author_id == user.id).order_by(Post.created_at).all()
    )
    formatted = []
    for post in posts:
        date: datetime = post.created_at
        formatted.append({"id": post.id, "date": f"{date.month}月{date.day}日"})
    return render_template("mypage.html", posts=formatted)
