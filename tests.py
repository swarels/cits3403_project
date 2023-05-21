import unittest, os
from app import app, db 
from app.models import User, Message

class TestDB(unittest.TestCase):
    
    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = \
            'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app_test_client()
        db.create_all()
        u1 = User(username="user1", name="Test Case", hashed_password="testpassword", messages="test message 1", is_pro=False)
        u2 = User(username="user2", name="Test Case2", hashed_password="testpassword2", messages="test message 2", is_pro=True)
        u3 = User(username="user3", name="Test Case3", hashed_password="testpassword3", messages="test message 3", is_pro=False)

        m1 = Message(id=1, text="testmessage 1", time="now", userid="user1")
        m2 = Message(id=2, text="testmessage 2", time="now", userid="user2")
        m3 = Message(id=3, text="testmessage 3", time="now", userid="user3")

        db.session.add(u1)
        db.session.add(u2)
        db.session.add(u3)
        db.session.add(m1)
        db.session.add(m2)
        db.session.add(m3)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User.query.get("user1")
        u.set_password("test")
        self.assertFalse(u.check_password("case"))
        self.assertTrue(u.check_password("test"))

    def test_is_committed(self):
        u1 = User.query.get("user1")
        self.assertFalse(u1.is_committed())
        u2 = User.query.get("user2")
        m1 = Message.query.get(1)
        db.session.add()




