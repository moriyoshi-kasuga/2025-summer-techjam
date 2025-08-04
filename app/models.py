from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False, index=True)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

class Admin(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    description = db.Column(db.String(512), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class HiddenComment(db.Model):
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'), primary_key=True)

    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

class Report(db.Model):
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), primary_key=True)
    reporter_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    reason = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
