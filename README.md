# FitTrack

Website for users to work with fitness guiders

# Description

FitTrack is a website designed for anyone wanting to accelerate their fitness goals, whether they're an avid gym-goer or just getting started in their fitness adventure. They're able to to do this by completing a short form that will highlight what that user wants to accomplish in their fitness goals. The user will then be connected to a fitness pro, able to communicate in real time. This pro will receive the specific user's information, and be able to deliver tips and information tailored to their user's wants and needs.

# Functionality

A user will be able either sign in, or create an account once opening the website.
When creating an account, users, will enter their personal information, as well as indicating whether they are a fitness pro, or a regular user. Then users are taken to our mascot, Gymrat. Gymrat will ask them various questions in regards to the outcome they want to achieve with FitTrack.
If they are not first time users, they will be able to connect to a pro.
Fitness pros after signing in will be connected to a user wanting to chat.
Users pressing "connect" will be met with a "loading" screen until another user has been found to connect with.
Once a user and a pro are connected, they will be able to communicate in real time.
Users will also be able to view their chat history as well as the information they filled out in the goal setting page.

# Installation

Install all necessary modules (commented at the top of main.py)
Run main.py

# Database Scheme

SQLite based database. Contains tables User, Trainer and Message.
The schemas are as follows:
User(username, name, hashed_password, messages, fitness_goal, height, weight, gender, current_excercise, willing_excercise, allergies, other_comments)
Trainer(username, name, hashed_password, messages)
Message(id, text, time, trainer_id, user_id)
