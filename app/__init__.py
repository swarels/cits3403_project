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
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://qbpemtufvtzwyj:3d4ff0519b654838ab6dbac389b8069ea140efedcdcb3a24780ceb5028ee36a8@ec2-3-232-103-50.compute-1.amazonaws.com:5432/d6t5qch2v7f9uh'
#\
#        'sqlite:///' + os.path.join(basedir, 'app.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)
login = LoginManager(app)
#db.init_app(app)

#from .main import *
#from .models import *
from app import routes, models