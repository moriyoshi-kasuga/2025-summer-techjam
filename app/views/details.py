from datetime import datetime

from flask import Blueprint, render_template
from flask_login import login_required

from app.models import Post

blueprint = Blueprint("details", __name__)


@blueprint.route("/<int:post_id>")
@login_required
def details(post_id: int):
    post = Post(id="test", content="サンプル内容", created_at=datetime.now())
    comments = ["サンプル1", "サンプル2"]
    # user_id = current_user.id
    # post: Post | None = Post.query.filter(
    #     Post.id == post_id, Post.author_id == user_id
    # ).one_or_none()
    # if post is None:
    #     return redirect("/mypage")
    #
    # object_comments: List[Comment] = Comment.query.filter(
    #     Comment.post_id == post.id
    # ).order_by(Comment.created_at)
    #
    # comments: List[str] = []
    # for v in object_comments:
    #     comments.append(v.content)

    return render_template(
        "details.html",
        post=post,
        comments=comments,
    )
