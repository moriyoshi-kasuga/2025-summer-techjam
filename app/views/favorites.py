from datetime import datetime
from typing import List

from flask import Blueprint, render_template
from flask_login import current_user, login_required

from app.models import Favorite, Post, User

blueprint = Blueprint("favorites", __name__, url_prefix="/favorites")


@blueprint.route("/")
@login_required
def favorites():
    user: User = current_user
    favorites: List[Favorite] = (
        Favorite.query.filter(Favorite.user_id == user.id)
        .order_by(Favorite.created_at.desc())
        .all()
    )

    post_ids = [fav.post_id for fav in favorites]

    posts: List[Post] = Post.query.filter(Post.id.in_(post_ids)).all()
    users: List[User] = User.query.filter(
        User.id.in_([post.author_id for post in posts])
    ).all()
    dict_usernames = {user.id: user.name for user in users}

    formatted_posts = []
    for post in posts:
        date: datetime = post.created_at
        formatted_posts.append(
            {
                "id": post.id,
                "date": f"{date.month}月{date.day}日",
                "author_name": dict_usernames.get(post.author_id, "Unknown Author"),
            }
        )

    return render_template("favorites.html", username=user.name, posts=formatted_posts)
