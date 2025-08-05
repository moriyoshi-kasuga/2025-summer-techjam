from flask import Blueprint, render_template
import random

blueprint = Blueprint("home", __name__)


@blueprint.route("/")
def home():
    words = ["きょうは、はなび大会にいきました。","きょうは、おばあちゃんちにいきました。","きょうは、カブトムシをつかまえました。","きょうは、プールにいきました。","きょうは、ながしそうめんをしました。"]
    return render_template("index.html",word=random.choice(words))
