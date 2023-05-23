from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, request
import uuid

username: str = "task_2"
password: str = "a41a9ASc363d4G6Q1027F2a50eH867"


app = Flask(__name__)

connection_string = f'postgresql://{username}:{password}@db:5432/task_2_database'
engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    access_token = Column(String, nullable=False, unique=True, default=lambda: str(uuid.uuid4()))

@app.route('/task_2/new_user', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')

    new_user = User(username=username)
    session.add(new_user)
    session.commit()

    return 'User created successfully!\n'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

