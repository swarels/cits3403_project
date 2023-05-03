# install following before beginning:
# pip install flask
# pip install flask-socketio

from flask import Flask, render_template, request, session, redirect
from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase

from forms import LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey123"
socketio = SocketIO(app)

@app.route("/", methods=["POST", "GET"])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user (), remember=()'.format(
            form.username.data, form.remember.data))
        return redirect('/room')
    return render_template("home.html", title='Sign In', form=form)

if __name__ == "__main__":
    socketio.run(app, debug=True)