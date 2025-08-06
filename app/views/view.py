import dataclasses
from datetime import date

from flask import Blueprint, render_template
from flask_login import current_user, login_required

from app import db
from app.models import Comment, Favorite, Post

blueprint = Blueprint("view", __name__, url_prefix="/view")


@dataclasses.dataclass
class View:
    post: Post
    is_favorite: bool
    comment: str | None


@blueprint.route("/")
@login_required
def view():
    today = date.today()
    posts_today = (
        Post.query.filter(db.func.date(Post.created_at) == today)
        .order_by(Post.created_at.desc())
        .all()
    )

    views = []
    for post in posts_today:
        is_favorite = (
            Favorite.query.filter_by(user_id=current_user.id, post_id=post.id).first()
            is not None
        )

        comment_obj = Comment.query.filter_by(
            post_id=post.id, author_id=current_user.id
        ).first()
        comment_content = comment_obj.content if comment_obj else None

        views.append(View(post=post, is_favorite=is_favorite, comment=comment_content))

    return render_template(
        "view.html",
        views=views,
    )
