from flask import Blueprint, jsonify, redirect, render_template
from flask_login import current_user, login_required

from app import db
from app.models import Comment, HiddenComment, Post

blueprint = Blueprint("details", __name__, url_prefix="/details")


@blueprint.route("/<int:post_id>")
@login_required
def details(post_id: int):
    post = Post.query.filter_by(id=post_id, author_id=current_user.id).one_or_none()
    if post is None:
        return redirect("/mypage")

    comments_raw = (
        Comment.query.filter_by(post_id=post.id).order_by(Comment.created_at).all()
    )
    hidden_comment_ids = {hc.comment_id for hc in HiddenComment.query.all()}

    comments_data = []
    for c in comments_raw:
        comments_data.append({"comment": c, "is_hidden": c.id in hidden_comment_ids})

    return render_template(
        "details.html",
        post=post,
        comments_data=comments_data,
    )


@blueprint.route("/comment/<int:comment_id>/hide", methods=["POST"])
@login_required
def hide_comment(comment_id: int):
    comment = Comment.query.get_or_404(comment_id)
    post = Post.query.get_or_404(comment.post_id)

    if post.author_id != current_user.id:
        return jsonify({"success": False, "error": "権限がありません"}), 403

    is_already_hidden = HiddenComment.query.get(comment_id) is not None
    if is_already_hidden:
        return jsonify({"success": False, "error": "既に非表示です"})

    hidden_comment = HiddenComment(comment_id=comment_id)
    db.session.add(hidden_comment)
    db.session.commit()

    return jsonify({"success": True})

