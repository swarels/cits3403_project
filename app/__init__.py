from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object(Config)
print(app.secret_key)
# app.config['SQLALCHEMY_DATABASE_URI'] =\
#        'sqlite:///' + os.path.join(basedir, 'app.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)
login = LoginManager(app)
#login.login_view = 'login'
#uncomment above line when we have logging in working
#db.init_app(app)

#from .main import *
#from .models import *
from app import routes, models