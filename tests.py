import unittest, os
from app import app, db 
from app.models import User, Message, Trainer

class TestDB(unittest.TestCase):
    
    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = \
            'sqlite:///' + os.path.join(basedir, 'app.db')
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

        u1 = User(username="user1", name="Test Case", hashed_password="testpassword", fitness_goal=1, height=175, weight=80, gender=1, current_excercise=2, willing_excercise=3, allergies="", other_comments="")
        u2 = User(username="user2", name="Test Case2", hashed_password="testpassword2", fitness_goal=2, height=155, weight=47, gender=1, current_excercise=1, willing_excercise=4, allergies="", other_comments="")
        db.session.add(u1)
        db.session.add(u2)

        #m1 = Message(id=1, text="testmessage 1", time="now", trainer_id="trainer1", user_id="user1")
        #b.session.add(m1)
        #u1.messages.append(m1)
        #m2 = Message(id=2, text="testmessage 2", time="now", trainer_id="trainer1", user_id="user1")
        #db.session.add(m2)
        #u1.messages.append(m2)
        #m3 = Message(id=3, text="testmessage 1", time="now", trainer_id="trainer2", user_id="user2")
        #db.session.add(m3)
        #u2.messages.append(m3)
        #m4 = Message(id=4, text="testmessage 2", time="now", trainer_id="trainer2", user_id="user2")
        #db.session.add(m4)
        #u2.messages.append(m4)

        t1 = Trainer(username="gymtrainer", name="Trainer1", hashed_password="trainerp")
        t2 = Trainer(username="gymtrainer2", name="Trainer2", hashed_password="trainerp2")

        #db.session.add(u1)
        #db.session.add(u2)
        db.session.add(t1)
        db.session.add(t2)
        db.session.commit()

        m1 = Message(text="testmessage 1", time="now", trainer_id=t1.id, user_id=u1.id)  # use the ids of the trainer and user
        m2 = Message(text="testmessage 2", time="now", trainer_id=t1.id, user_id=u1.id)
        m3 = Message(text="testmessage 1", time="now", trainer_id=t2.id, user_id=u2.id)
        m4 = Message(text="testmessage 2", time="now", trainer_id=t2.id, user_id=u2.id)

        db.session.add(m1)
        db.session.add(m2)
        db.session.add(m3)
        db.session.add(m4)

        u1.messages.append(m1)
        u1.messages.append(m2)
        u2.messages.append(m3)
        u2.messages.append(m4)

        t1.messages.append(m1)
        t1.messages.append(m2)
        t2.messages.append(m3)
        t2.messages.append(m4)

        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    # checking if password is correct 
    def test_password_hashing(self):
        u =  User.query.get("user1")
        self.assertFalse(u.hashed_password, "wrongpassword")
        self.assertTrue(u.hashed_password, "testpassword")

    # checking if the messages of a user and the corresponding message's text and user are correctly set
    def test_user_messages(self):
        u1 = User.query.get("user1")
        self.assertEqual(u1.messages, 1)
        
        m1 = Message.query.get(1)
        self.assertEqual(m1.text, "testmessage 1")
        self.assertEqual(m1.user_id, "user1")

    # checks if the time attribute of a message is correctly set
    def test_message_time(self):
        m1 = Message.query.get(1)
        self.assertEqual(m1.time, "now")

    # ensures that the user associated with a message is correctly set and can be accessed
    def test_message_user(self):
        m1 = Message.query.get(1)
        self.assertEqual(m1.user_id, "user1")
        
        u2 = User.query.get("user2")
        self.assertEqual(u2.messages[0].text, "testmessage 2")

    # checks if the fitness goal of a user is correctly set
    def test_user_fitness_goal(self):
        u1 = User.query.get("user1")
        self.assertEqual(u1.fitness_goal, 1)
        
        u2 = User.query.get("user2")
        self.assertEqual(u2.fitness_goal, 2)

    # verify if the height and weight attributes of a user are correctly set
    def test_user_height(self):
        u1 = User.query.get("user1")
        self.assertEqual(u1.height, 175)
        
        u2 = User.query.get("user2")
        self.assertEqual(u2.height, 155)

    def test_user_weight(self):
        u1 = User.query.get("user1")
        self.assertEqual(u1.weight, 80)
        
        u2 = User.query.get("user2")
        self.assertEqual(u2.weight, 47)

    # ensures that the trainer associated with a message is correctly set and can be accessed
    def test_message_trainer(self):
        m1 = Message.query.get(1)
        self.assertEqual(m1.trainer_id, "trainer1")
        
        t2 = Trainer.query.get("trainer2")
        self.assertEqual(t2.messages[0].text, "testmessage 2")



if __name__ == "__main__":
    unittest.main(verbosity=2) 



