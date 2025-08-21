import dataclasses
from datetime import date, timedelta

from flask import Blueprint, jsonify, render_template, request
from flask_login import current_user, login_required

from app import db
from app.models import Comment, Favorite, Post, User

blueprint = Blueprint("view", __name__, url_prefix="/view")


@dataclasses.dataclass
class View:
    author_name: str
    post: Post
    is_favorite: bool
    comment: str | None


@blueprint.route("/")
@login_required
def view():
    recently = date.today() - timedelta(days=5)
    posts_today = (
        Post.query.filter(db.func.date(Post.created_at) > recently)
        .order_by(Post.created_at.desc())
        .all()
    )

    views = []
    for post in posts_today:
        author = User.query.get(post.author_id)
        is_favorite = (
            Favorite.query.filter_by(user_id=current_user.id, post_id=post.id).first()
            is not None
        )
        comment_obj = Comment.query.filter_by(
            post_id=post.id, author_id=current_user.id
        ).first()
        comment_content = comment_obj.content if comment_obj else None

        views.append(
            View(
                author_name=author.name,
                post=post,
                is_favorite=is_favorite,
                comment=comment_content,
            )
        )

    return render_template("view.html", views=views)


@blueprint.route("/post/<int:post_id>/favorite", methods=["POST"])
@login_required
def toggle_favorite(post_id: int):
    """お気に入りの状態をトグルするAPIエンドポイント"""
    existing_favorite = Favorite.query.filter_by(
        user_id=current_user.id, post_id=post_id
    ).first()

    if existing_favorite:
        db.session.delete(existing_favorite)
        is_favorite = False
    else:
        new_favorite = Favorite(user_id=current_user.id, post_id=post_id)
        db.session.add(new_favorite)
        is_favorite = True

    db.session.commit()
    return jsonify({"success": True, "is_favorite": is_favorite})


@blueprint.route("/post/<int:post_id>/comment", methods=["POST"])
@login_required
def add_comment(post_id: int):
    """コメントを追加/更新するAPIエンドポイント"""
    data = request.get_json()
    content = data.get("content")

    if not content:
        return jsonify({"success": False, "error": "コメント内容がありません"}), 400

    comment = Comment.query.filter_by(
        author_id=current_user.id, post_id=post_id
    ).first()
    if comment:
        comment.content = content
    else:
        comment = Comment(content=content, author_id=current_user.id, post_id=post_id)
        db.session.add(comment)

    db.session.commit()
    return jsonify({"success": True, "comment": content})
