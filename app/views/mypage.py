from datetime import datetime
from typing import List

from flask import Blueprint, redirect, render_template
from flask_login import current_user

from app.models import Post, User

blueprint = Blueprint("mypage", __name__)


@blueprint.route("/")
def mypage():
    if current_user is None:
        return redirect("/login")
    user: User = current_user
    posts: List[Post] = (
        Post.query.filter(Post.author_id == user.id).order_by(Post.created_at).all()
    )
    formatted = []
    for post in posts:
        date: datetime = post.created_at
        formatted.append({"id": post.id, "date": f"{date.month}月{date.day}日"})
    return render_template("mypage.html", posts=formatted)
