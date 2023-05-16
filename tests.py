import unittest, os
from app import app, db 
from app.models import User, Message

class TestDB(unittest.TestCase):
    
    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = \'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app_test_client()
        db.create_all()
        





