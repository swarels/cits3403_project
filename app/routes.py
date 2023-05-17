from flask import Flask, request, session, redirect, render_template, flash
from app import app
from app.forms import LoginForm
#from app.forms import SignUpForm

@app.route("/", methods=["POST", "GET"])
@app.route("/index", methods=["POST", "GET"])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user (), remember=()'.format(
            form.username.data, form.remember.data))
        return redirect('/room')
    return render_template("home.html", title='Sign In', form=form)

@app.route("/room")
def room():
    return render_template("room.html")