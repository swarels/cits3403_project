from flask import Flask, request, session, redirect, render_template, flash
from app import app, db
from flask_login import current_user, login_user, logout_user, login_required
from flask_socketio import join_room, leave_room, emit, send, SocketIO
from app.models import User, Trainer, Message
from app.forms import LoginForm, SignUpForm, GoalForm, MessageForm

# Setting up routes for all webpages 
@app.route("/", methods=["POST", "GET"])
@app.route("/index", methods=["POST", "GET"])
def home():
    if current_user.is_authenticated:
        return redirect('/chatroom')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('/')
        else:
            login_user(user, remember=form.remember.data)
            return redirect('/chatroom')
    return render_template("home.html", title='Sign In', form=form)

# Logout page route
@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')

# History page route
@app.route("/history", methods=['GET'])
@login_required
def history():
    messages = current_user.msg_history().all()
    return render_template("history.html", title='History', messages=messages, user=current_user)

# Signup page route
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect('/chatroom')
    form = SignUpForm()
    if form.validate_on_submit():
        if (form.professional.data == True):
            trainer = Trainer(username=form.username.data, name=form.name.data)
            trainer.set_password(form.password.data)
            db.session.add(trainer)
            db.session.commit()
            return redirect('/verify')
        else:
            user = User(username=form.username.data, name=form.name.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            return redirect('/talkingRat')
    return render_template("signup.html", title='Sign Up', form=form)

# Chatroom page route
@app.route('/chatroom')
@login_required
def chatroom():
    return render_template('chatroom.html')

""" Code for archived alternate room
@app.route('/room', methods=["GET", "POST"])
@login_required
def room():
    current_trainer = Trainer.query.get('timtrainer')
    form = MessageForm()
    if form.validate_on_submit():
        msg = Message(text=form.message.data, from_trainer=False, user_name=current_user, trainer_name=current_trainer)
        db.session.add(msg)
        db.session.commit()
    return render_template('room.html', form=form)
"""

# Verify page route
@app.route('/verify')
def verify():
    return render_template('verifytrainer.html')

# Talking rat page route
@app.route("/talkingRat")
def talkingRat():
    return render_template("talkingRat.html")

# Goal setting page route
@app.route("/goalSetting", methods=["GET", "POST"])
def goalSetting():
    form = GoalForm()
    if form.validate_on_submit():
        user = current_user
        user.fitness_goal = form.goal.data
        user.height = form.height.data
        user.weight = form.weight.data
        user.gender = form.gender.data
        user.current_excercise = form.pastexercise.data
        user.willing_excercise = form.willing.data
        user.allergies = form.allergies.data
        user.other_comments = form.comments.data
        db.session.add(user)
        db.session.commit()
        return redirect('/chatroom')
    return render_template("goalSetting.html", title="goals", form=form)