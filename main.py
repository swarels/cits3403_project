# install following before beginning:
# pip install flask
# pip install flask-socketio

from flask import Flask, render_template, request, session, redirect
from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase

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
@app.route("/signup", methods = ["GET", "POST"])
def signup():
    form = SignUpForm()
    # if form.is_submitted():
    #     result = request.form
    #     return 
    return render_template("signup.html", form = form)

@app.route('/chatroom')
def chatroom():
    return render_template('chatroom.html')

if __name__ == "__main__":
    socketio.run(app, debug=True)
