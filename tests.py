import unittest, os
from app import app, db 
from app.models import User, Message

class TestDB(unittest.TestCase):
    
    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = \'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app_test_client()
        db.create_all()
        u1 = User(username="user1", name="Test Case", hashed_password="testpassword", messages="test message 1", is_pro="N")
        u2 = User(username="user2", name="Test Case2", hashed_password="testpassword2", messages="test message 2", is_pro="Y")
        m1 = Message(id=1, text="testmessage 1", time="IDK WHAT FORMAT THIS IS", userid="user1")
        m2 = Message(id=2, text="testmessage 2", time="IDK WHAT FORMAT THIS IS", userid="user2")
        db.session.add(u1)
        db.session.add(u2)
        db.session.add(m1)
        db.session.add(m2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()





