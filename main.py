# install following before beginning:
# pip install flask
# pip install flask-socketio
# pip install flask-wtf
# pip install pymysql
# pip install mysql-connector-python

from flask import Flask, render_template, request, session, redirect
from flask_socketio import join_room, leave_room, emit, send, SocketIO
import random
from string import ascii_uppercase

from forms import LoginForm

from forms import LoginForm
from forms import SignUpForm

import mysql.connector


"""
Initialize flask object
"""
app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey123"
socketio = SocketIO(app)

# """
# Initialize the database
# """
# mydb = mysql.connector.connect(
#     host = "localhost",
#     user="root",
#     password="23073177"
# )
# # print(mydb) # tests the connection
# mycurser = mydb.cursor()
# mycurser.execute("CREATE DATABASE GymUsers")


"""
Main homepage
"""


@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("home.html")


"""
Signup page
"""
@app.route("/signup", methods=["GET", "POST"])
def signup():
    username = None
    password = None
    form = SignUpForm()
    # Validate form
    if form.validate_on_submit():
        username = form.username.data
        form.username.data = ""

    # if form.is_submitted():
    #     result = request.form
    #     return
    return render_template("signup.html", username=username, password=password, form=form)

@app.route('/chatroom')
def chatroom():
    return render_template('chatroom.html')

@app.route('/preferredname')
def preferred_name():
    return render_template('preferredname.html')

@app.route("/talkingRat")
def talkingRat():
    return render_template("talkingRat.html")

@app.route("/goalSetting")
def goalSetting():
    return render_template("goalSetting.html")

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
