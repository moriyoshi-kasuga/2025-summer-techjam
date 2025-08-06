import dataclasses
from datetime import datetime

from flask import Blueprint, render_template

from app.models import Post

blueprint = Blueprint("view", __name__)


@dataclasses.dataclass
class View:
    post: Post
    is_favorite: bool
    comment: str | None


@blueprint.route("/")
def view():
    post1 = Post(id="test", content="サンプル内容", created_at=datetime.now())
    view1 = View(post1, True, "良い内容!")

    post2 = Post(
        id="test2", content="サンプル内容素晴らしい夏", created_at=datetime.now()
    )
    view2 = View(post2, False, "良い夏やな")

    post3 = Post(id="test3", content="バカ暑い", created_at=datetime.now())
    view3 = View(post3, True, "せやな")

    views = [view1, view2, view3]
    return render_template(
        "view.html",
        views=views,
    )
