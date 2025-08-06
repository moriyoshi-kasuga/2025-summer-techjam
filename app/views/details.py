from flask import Blueprint, redirect, render_template
from flask_login import current_user, login_required

from app.models import Comment, Post

blueprint = Blueprint("details", __name__, url_prefix="/details")


@blueprint.route("/<int:post_id>")
@login_required
def details(post_id: int):
    # ログインユーザーの投稿のみを取得
    post = Post.query.filter_by(id=post_id, author_id=current_user.id).one_or_none()
    if post is None:
        return redirect("/mypage")

    comments = Comment.query.filter_by(post_id=post.id).order_by(Comment.created_at).all()

    return render_template(
        "details.html",
        post=post,
        comments=comments,
    )
