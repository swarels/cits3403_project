#adapted from lecture 9
from flask_wtf import FlaskForm
from wtforms import RadioField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, ValidationError, EqualTo, InputRequired, NumberRange, Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class SignUpForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    passwordagain = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    professional = BooleanField('Are you a professional?')
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username is already in use')

class GoalForm(FlaskForm):
    #goal = SelectField('Fitness Goal', [ InputRequired()],
     #   choices=[ (-1, 'Choose a goal'), (0, 'Lose weight'),
     #   (1, 'Build Muscle'),
      #  (2, 'Get in shape'),
       # (3, 'Other') ], coerce=int)
    goal = RadioField('Fitness Goal', [InputRequired()],
                  choices=[(0, 'Lose weight'),
                           (1, 'Build Muscle'), (2, 'Get in shape'),
                           (3, 'Other')],
                  coerce=int)
    height = IntegerField('Height', [ InputRequired(),
        NumberRange(min=50, max=250, message="You are too tall/short")
        ])
    weight = IntegerField('Weight', [ InputRequired(),
        NumberRange(min=20, max=400, message="You are too heavy/thin")
        ])
    gender = SelectField('Gender', [ InputRequired()],
        choices=[ (-1, 'Choose a gender'), (0, 'Male'),
        (1, 'Female'),
        (2, 'Other')], coerce=int)
    pastexercise = SelectField('Past Exercise', [ InputRequired()],
        choices=[ (-1, 'Choose a frequency of exercise'), (0, 'Multiple times a week'),
        (1, 'Once a Week or so'),
        (2, 'On the off occasion'),
        (3, 'Never') ], coerce=int)
    willing = IntegerField('Willing', [ InputRequired(),
        NumberRange(min=1, max=7, message="Invalid amount of days per week")
        ])
    allergies = StringField('Allergies', [ Length(min=1, max=128, message="Too much information")
        ])
    comments = StringField('Extra Info', [ Length(min=1, max=256, message="Too much information")
        ])
    submit = SubmitField('Submit')