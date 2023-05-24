from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, LargeBinary
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, request, jsonify
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
    #audio_records = relationship("AudioRecord", back_populates="user")


class AudioRecord(Base):
    __tablename__ = 'audiorecords'

    record_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    record_uuid = Column(String, nullable=False, unique=True, default=lambda: str(uuid.uuid4()))
    #user = relationship("User", back_populates="audio_records")


class AudioFile(Base):
    __tablename__ = 'audiofiles'

    record_id = Column(Integer, ForeignKey('audioRecords.record_id'), primary_key=True)
    file_data = Column(LargeBinary, nullable=False)


@app.route('/task_2/new_user', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    
    print(f"new user: {username}")
    
    new_user = User(username=username)
    session.add(new_user)
    session.commit()

    return jsonify({
        'user_id': new_user.user_id,
        'access_token': new_user.access_token
    })


@app.route('/task_2/upload_audio', methods=['POST'])
def upload_audio():
    access_token = request.headers.get('access_token')
    user_id = session.query(User).filter_by(access_token=access_token).first()
    

    if not access_token or not user_id:
        return jsonify({'error': 'Missing required arguments'})

    if not user or str(user.user_id) != user_id:
        return jsonify({'error': 'Unauthorized access'})

    file = request.files.get('audio')

    if not file:
        return jsonify({'error': 'Missing audio file'})

    file = request.files['audio']
    file_data = file.read()


    new_record = AudioRecord(user_id=user.user_id)
    new_file = AudioFile(record_id=new_record.record_id,file_data=file_data)

    session.add(new_record)
    session.add(new_file)
    session.commit()

    return jsonify({'URL': f"https://localhost/task_2/{new_record.record_uuid}.mp3"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
