from flask import Blueprint, render_template

blueprint = Blueprint("details", __name__)


@blueprint.route("/:<int:post_id>")
def details(post_id: int):
    # TODO: post_id からアクセスしようとしているのが投稿主かどうか。
    # 投稿主のidは current_user.id で取得できる。
    # そして投稿の内容と投稿にポストされてるコメントを確認する。
    # そして template にデータを渡す。
    return render_template("details.html")
