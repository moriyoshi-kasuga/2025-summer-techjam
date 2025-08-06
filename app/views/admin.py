from functools import wraps

from flask import Blueprint, abort, render_template
from flask_login import current_user, login_required

from app.models import Admin, Post, Report, User

blueprint = Blueprint("admin", __name__, url_prefix="/admin")


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not Admin.query.get(current_user.id):
            abort(403)
        return f(*args, **kwargs)

    return decorated_function


@blueprint.route("/")
@login_required
@admin_required
def report_list():
    reports = Report.query.order_by(Report.created_at.desc()).all()

    report_data = []
    for report in reports:
        post = Post.query.get(report.post_id)
        reporter = User.query.get(report.reporter_id)

        if post and reporter:
            post_author = User.query.get(post.author_id)
            report_data.append(
                {
                    "post_id": post.id,
                    "post_content": post.content[:30] + "..."
                    if len(post.content) > 30
                    else post.content,
                    "post_author_name": post_author.name if post_author else "不明",
                    "reporter_name": reporter.name,
                    "report_reason": report.reason,
                    "reported_at": report.created_at.strftime("%Y-%m-%d %H:%M"),
                }
            )

    return render_template("admin.html", reports=report_data)
