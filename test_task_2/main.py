from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, LargeBinary
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, request, jsonify
import uuid
import base64

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


class AudioRecord(Base):
    __tablename__ = 'audiorecords'

    record_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    record_uuid = Column(String, nullable=False, unique=True, default=lambda: str(uuid.uuid4()))


class AudioFile(Base):
    __tablename__ = 'audiofiles'

    record_id = Column(Integer, ForeignKey('audiorecords.record_id'), primary_key=True)
    file_data = Column(LargeBinary, nullable=False)


@app.route('/task_2/new_user', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    
    if not username:
        return jsonify({'error': 'Missing username argument!'})       
    
    new_user = User(username=username)
    session.add(new_user)
    session.commit()

    return jsonify({
        'user_id': new_user.user_id,
        'access_token': new_user.access_token
    })


@app.route('/task_2/upload_audio', methods=['POST'])
def upload_audio():
    json = request.get_json()
    
    access_token = json.get('Access_token')
    user_id = json.get('User_id')
    
    if not access_token:
        return jsonify({'error': 'Missing access_token argument!'})        

    if not user_id:
        return jsonify({'error': 'Missing user_id argument!'})                

    if not session.query(User).filter_by(access_token=access_token, user_id=user_id).first():
        return jsonify({'error': 'Unauthorized access'})

    file_data = json.get('data')

    if not file_data:
        return jsonify({'error': 'Missing audio file'})

    file_data_bin = base64.b64decode(file_data)

    new_record = AudioRecord(user_id=user_id)
    session.add(new_record)
    session.commit()
    
    new_file = AudioFile(record_id=new_record.record_id,file_data=file_data_bin)
    session.add(new_file)
    session.commit()

    return jsonify({'URL': f"http://localhost/task_2/download?user_id={user_id}&rec_id={new_record.record_id}.mp3"})


@app.route('/download', methods=['GET'])
def download_file():
    record_id = request.args.get('id')
    user_id = request.args.get('user')

    print(f"download {record_id} by {user_id}")


    if not record_id:
        return jsonify({'error': 'Missing record_id argument!'})

    if not user_id:
        return jsonify({'error': 'Missing user_id argument!'})

    record = session.query(AudioRecord).filter_by(record_id=record_id, user_id=user_id).first()

    if not record:
        return jsonify({'error': 'Record not found or unauthorized access'})

    audio_file = session.query(AudioFile).filter_by(record_id=record.record_id).first()

    if not audio_file:
        return jsonify({'error': 'Audio file not found for the record'})

    file_data = audio_file.file_data
    filename = f"{record.record_uuid}.mp3"

    return send_file(BytesIO(file_data), attachment_filename=filename, as_attachment=True)

app.add_url_rule('/download', 'download_file', download_file, methods=['GET'])






if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
