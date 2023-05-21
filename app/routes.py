from flask import Flask, request, session, redirect, render_template, flash
from app import app, db
from flask_login import current_user, login_user, logout_user
from flask_socketio import join_room, leave_room, emit, send, SocketIO
from app.models import User, Trainer, Message
from app.forms import LoginForm, SignUpForm, GoalForm

@app.route("/", methods=["POST", "GET"])
@app.route("/index", methods=["POST", "GET"])
def home():
    if current_user.is_authenticated:
        return redirect('/chatroom')
    form = LoginForm()
    if form.validate_on_submit():
        print("right!")
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('/index')
        login_user(user, remember=form.remember.data)
        return redirect('/talkingRat')
    return render_template("home.html", title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/index')

@app.route("/history", methods=['GET'])
def history():
    try:
        current_user.is_authenticated()
    except UnboundLocalError:
        current_user = User.query.get('testUser123')
    messages = current_user.msg_history().all()
    return render_template("history.html", title='History', messages=messages, user=current_user)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect('/chatroom')
    form = SignUpForm()
    if form.validate_on_submit():
        if (form.professional == True):
            trainer = Trainer(username=form.username.data, name=form.name.data)
            trainer.set_password(form.password.data)
            db.session.add(trainer)
            db.session.commit()
            return redirect('/chatroom')
        else:
            user = User(username=form.username.data, name=form.name.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect('/talkingRat')
    return render_template("signup.html", title='Sign Up', form=form)

@app.route('/chatroom')
#@login_required
#uncomment above when logging in works
def chatroom():
    return render_template('chatroom.html')

@app.route('/preferredname')
def preferred_name():
    return render_template('preferredname.html')

@app.route("/talkingRat")
def talkingRat():
    return render_template("talkingRat.html")

@app.route("/goalSetting", methods=["GET", "POST"])
def goalSetting():
    try:
        current_user.is_authenticated()
    except UnboundLocalError:
        current_user = User.query.get('testUser123')
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