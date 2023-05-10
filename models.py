from datetime import datetime
import db

class User(db.Model):
    username = db.Column(db.String(30), primary_key=True)
    name = db.Column(db.String(64), index=True)
    hashed_password = db.Column(db.String(128), nullable=False)
    messages = db.relationship('Post', backref='author', lazy='dynamic')
    is_pro = db.Column(db.Boolean)

    def __repr__(self):
        return '<User ()>'.format(self.name)
    
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(288))
    time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    userid = db.Column(db.String(30), db.ForeignKey('user.username'))

    def __repr__(self):
        return '<Post ()>'.format(self.body)