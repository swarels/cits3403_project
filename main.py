# install following before beginning:
# pip install flask
# pip install flask-socketio
# pip install flask-wtf
# pip install flask-sqlalchemy
# pip install flask-migrate
# pip install flask-login

from flask import Flask, request, session, redirect
from flask_socketio import join_room, leave_room, emit, send, SocketIO
import random
from string import ascii_uppercase
import os
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import TextAreaField, StringField, SubmitField
from wtforms.validators import DataRequired, Email

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

from app import app, db
from app.models import User, Message

socketio = SocketIO(app)

@app.shell_context_processor
def make_shell_context():
     return {'db': db, 'User': User, 'Message': Message}

@socketio.on("connect")
def handle_connect(preferred_name):
    print("Client connected!")

@socketio.on("join_user")
def connect_user(preferred_name):
    print(f"User {preferred_name} joined")
    socketio.emit("join_user", preferred_name)

@socketio.on("chat")
def new_message(data):
    socketio.emit("chat", data)

if __name__ == "__main__":
    socketio.run(app, debug=True)