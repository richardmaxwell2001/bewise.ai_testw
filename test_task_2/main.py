from flask import Flask, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


username: str = "task_2"
password: str = "a41a9ASc363d4G6Q1027F2a50eH867"

app = Flask(__name__)

connection_string: str = f'postgresql://{username}:{password}@db:5432/task_2_database'
engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)
session = Session()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

@app.route('/create_user', methods=['POST'])
def create_user():
    username = request.form['username']
    email = request.form['email']

    new_user = User(username, email)
    session.add(new_user)
    session.commit()

    return 'User created successfully!'

if __name__ == '__main__':
    app.run()
