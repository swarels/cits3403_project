from flask import Flask, request, session, redirect, render_template, flash
from app import app
from flask_login import current_user, login_user, logout_user
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