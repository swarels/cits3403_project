# install following before beginning:
# pip install flask
# pip install flask-socketio

from flask import Flask, render_template, request, session, redirect
from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase

app = Flask(__name__)
app.config["secretKey"] = "secretkey123"
socketio = SocketIO(app)


@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("home.html")


@app.route("/createAccount.html")
def createAccount():
    return render_template("createAccount.html")


if __name__ == "__main__":
    socketio.run(app, debug=True)
