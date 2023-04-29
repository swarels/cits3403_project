# install following before beginning:
# pip install flask
# pip install flask-socketio

from flask import Flask, render_template, request, session, redirect
from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase

from forms import SignUpForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey123"
socketio = SocketIO(app)

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



if __name__ == "__main__":
    socketio.run(app, debug=True)
