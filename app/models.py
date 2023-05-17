from datetime import datetime
from app import db

class User(db.Model):
    username = db.Column(db.String(30), primary_key=True)
    name = db.Column(db.String(64), index=True)
    hashed_password = db.Column(db.String(128), nullable=False)
    messages_sent = db.relationship('Message', backref='author', lazy='dynamic')
    messages_got = db.relationship('Message', backref='recipient', lazy='dynamic')
    is_pro = db.Column(db.Boolean)

    def __repr__(self):
        value = "User({})".format(self.username)
        return value
    
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(288))
    time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    userid_from = db.Column(db.String(30), db.ForeignKey('user.username'))
    userid_to = db.Column(db.String(30), db.ForeignKey('user.username'))

    # Relationships
    user_from = db.relationship('User', foreign_keys=[userid_from], backref=db.backref('author'))
    user_to = db.relationship('User', foreign_keys=[userid_to])

    def __repr__(self):
        value = "Message({})".format(self.id)
        return value