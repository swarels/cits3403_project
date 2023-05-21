# FitTrack

Website for users to work with fitness guiders

# Description

FitTrack is a website designed for anyone wanting to accelerate their fitness goals, whether they're an avid gym-goer or just getting started in their personal adventure. They're able to to do this by answering a few questions that will highlight what that user wants to accomplish in their personal goals. The user will then be connected to a personal trainer, able to communicate in real time. This trainer will receive the specific user's information, and be able to deliver tips and information tailored to their user's wants and needs.

# Functionality
A user will be able either sign in, or create an account once opening the website.  
When creating an account, users will enter their fitness information, as well as indicating whether they are a personal trainer, or a regular user.
After signing in, first time users will be met with our mascot, Gymrat. Gymrat will ask them various questions that will help the personal trainer tailor their information to the specific user.  
First time trainers will be verified as professionals outside of the website and then given a one-time verification code which allows them to sign up.
If they are not first time users, they will immediately be connected to a trainer.  
Personal trainers, after signing in, will be connected to a user wanting to chat.  
Once a user and a trainer are connected, they will be able to communicate in real time.  
Users will also be able to view their chat history and their answers to Gymrat's questions.  

# Installation
1. Activate your virtual environment  
2. Install all of the following:  
    pip install flask  
    pip install flask-socketio  
    pip install flask-wtf  
    pip install flask-sqlalchemy  
    pip install flask-migrate  
    pip install flask-login  
3. Change *self.id* to *self.username* in mixins.py *inside venv/lib/python3.10/site-packages/flask_login*
4. Then to run the server, do this:  
    flask run  
5. Then click on the URL provided.  


# Database Scheme

SQLite based database. Contains tables User, Trainer and Message.  
The schemas are as follows:  
* User(username, name, hashed_password, messages, fitness_goal, height, weight, gender, current_excercise, willing_excercise, allergies, other_comments)
* Trainer(username, name, hashed_password, messages)
* Message(id, text, time, trainer_id, user_id, from_trainer[^1])

[^1]: This variable is a boolean which determines whether a message was sent from a trainer or a user.
    Since trainers can only chat to users and vice versa, it was much more memory-efficient to store messages like this.
