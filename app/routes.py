from flask import Flask, request, session, redirect, render_template, flash
from app import app
from flask_login import current_user, login_user, logout_user
from flask_socketio import join_room, leave_room, emit, send, SocketIO
from app.models import User
from app.forms import LoginForm
#from app.forms import SignUpForm

@app.route("/", methods=["POST", "GET"])
@app.route("/index", methods=["POST", "GET"])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('/index')
        login_user(user, remember=form.remember.data)
        return redirect('/room')
    return render_template("home.html", title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/index')

@app.route("/room")
def room():
    return render_template("room.html")

#@app.route("/signup", methods=["GET", "POST"])
#def signup():
#    username = None
#    password = None
#    form = SignUpForm()
#    # Validate form
#    if form.validate_on_submit():
#        username = form.username.data
#        form.username.data = ""

    # if form.is_submitted():
    #     result = request.form
    #     return
#    return render_template("signup.html", username=username, password=password, form=form)

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