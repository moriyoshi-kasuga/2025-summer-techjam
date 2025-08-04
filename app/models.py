from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

class Admin(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(512), nullable=True)
    content = db.Column(db.Text, nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class HiddenComment(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('comment.id'), primary_key=True)

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reason = db.Column(db.String(256), nullable=False)

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    reporter_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
