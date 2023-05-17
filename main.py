# install following before beginning:
# pip install flask
# pip install flask-socketio
# pip install flask-wtf
# pip install flask-sqlalchemy
# pip install flask-migrate

from flask import Flask, request, session, redirect
from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase
import os
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import TextAreaField, StringField, SubmitField
from wtforms.validators import DataRequired, Email

#from app.forms import LoginForm
#from app.forms import SignUpForm

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


"""
Initialize flask object and database
"""
app = Flask(__name__)
#app.config['SECRET_KEY'] = SECRET_KEY
#app.secret_key = "secretkey123"
#csrf = CSRFProtect(app)
#csrf.init_app(app)
#app.config['WTF_CSRF_SECRET_KEY'] = "verysecretKEY"
#app.config['SESSION_TYPE'] = "filesystem"

#socketio = SocketIO(app)
#app.config.from_object(Config)
#db = SQLAlchemy(app)
#migrate = Migrate(app, db)

from app import app

"""
Main homepage
"""

"""
Signup page
"""
#@app.route("/signup", methods = ["GET", "POST"])
#def signup():
#    form = SignUpForm()
#    # if form.is_submitted():
#    #     result = request.form
#    #     return 
#    return render_template("signup.html", form = form)

if __name__ == "__main__":
    socketio.run(app, debug=True)