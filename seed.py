from models import User, db
from app import app

# Create all tables

with app.app_context():
    db.drop_all()  # Drops all the tables
    db.create_all() 

    # If table isn't empty, empty it
    User.query.delete()

    # Add pets
    user1 = User(first_name='Jack', second_name='Thomas', img_url='https://tinyurl.com/2p9yh95t')
    user2 = User(first_name='Roddy', second_name='Doyle', img_url='https://tinyurl.com/2p9yh95t')
    user3 = User(first_name='Daisy', second_name='Doodles', img_url='https://tinyurl.com/2p9yh95t')

    # Add new objects to session, so they'll persist
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)

    # Commit--otherwise, this never gets saved!
    db.session.commit()