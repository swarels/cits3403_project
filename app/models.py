from datetime import datetime
from app import db
from app import login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login.user_loader
def load_user(username):
    return User.query.get(username)

class User(UserMixin, db.Model):
    username = db.Column(db.String(30), primary_key=True)
    name = db.Column(db.String(64), index=True)
    hashed_password = db.Column(db.String(128))
    messages = db.relationship('Message', backref='user_name', lazy='dynamic')
    fitness_goal = db.Column(db.Integer)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    gender = db.Column(db.Integer)
    current_excercise = db.Column(db.Integer)
    willing_excercise = db.Column(db.Integer)
    allergies = db.Column(db.String(128))
    other_comments = db.Column(db.String(256))

    def get_id(self):
        return (self.username)

    def msg_history(self):
        return Message.query.filter_by(user_id=self.username).order_by(Message.time.asc()).limit(12)

    def __repr__(self):
        value = "User({})".format(self.username)
        return value
    
    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
    
class Trainer(db.Model):
    username = db.Column(db.String(30), primary_key=True)
    name = db.Column(db.String(64), index=True)
    hashed_password = db.Column(db.String(128))
    messages = db.relationship('Message', backref='trainer_name', lazy='dynamic')

    def msg_history(self):
        return Message.query.filter_by(trainer_id=self.username).order_by(Message.time.asc()).limit(12)

    def __repr__(self):
        value = "Trainer({})".format(self.username)
        return value
    
    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
    
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(288))
    time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    trainer_id = db.Column(db.String(30), db.ForeignKey('trainer.username'))
    user_id = db.Column(db.String(30), db.ForeignKey('user.username'))
    from_trainer = db.Column(db.Boolean)
    """^ This variable is a boolean which determines whether a message was sent from a trainer or a user.
    Since trainers can only chat to users and vice versa, it was much more memory-efficient to store messages like this.
    """

    def __repr__(self):
        value = "Message({})".format(self.id)
        return value