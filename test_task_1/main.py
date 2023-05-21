import requests
import json
import re
from flask import Flask, request, jsonify
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

# Определение базового класса для объявления моделей данных
Base = declarative_base()

# Определение модели данных в виде класса
class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer)
    question_text = Column(String)
    answer_text = Column(String)
    creation_date = Column(DateTime)

def strip_html_tags(text):
    # Удаление HTML-тегов из текста
    clean_text = re.sub('<.*?>', '', text)
    return clean_text

@app.route('/task_1', methods=['POST'])
def process_request():
    data = request.get_json()
    questions_num = data.get('questions_num')

    # Ввод данных для подключения к базе данных
    # По хорошему надо бы их тянуть
    username: str = "task_1"
    password: str = "0e0S6af9s6a5DswfcV7HgrDjeed"

    # Формирование строки подключения к базе данных
    connection_string: str = f'postgresql://{username}:{password}@db:5432/task_1_database'

    # Подключение к базе данных
    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Отправка запроса на https://jservice.io/api/random с параметром count=questions_num
    while True:
        response = requests.get(f"https://jservice.io/api/random?count={questions_num}")
        data = response.json()

        for item in data:
            # Проверяем, есть ли такой вопрос уже в базе данных
            existing_question = session.query(Question).filter_by(question_text=item['question']).first()
            if existing_question is None:
                # Очистка ответа от HTML-тегов
                answer_text = strip_html_tags(item['answer'])

                # Создание объекта вопроса
                question = Question(
                    question_id=item['id'],
                    question_text=item['question'],
                    answer_text=answer_text,
                    creation_date=item['created_at']
                )

                # Добавление объекта вопроса в сессию
                session.add(question)

        # Если найдены уникальные вопросы, сохраняем изменения и выходим из цикла
        if session.new:
            session.commit()
            break

    # Получение предпоследнего вопроса из базы данных
    last_question = session.query(Question).order_by(Question.id.desc()).offset(1).first()

    # Закрытие сессии
    session.close()

    # Возвращаем предпоследний вопрос или пустой объект, если такого вопроса нет
    if last_question is not None:
        result = {
            'question_id': last_question.question_id,
            'question_text': last_question.question_text,
            'answer_text': last_question.answer_text,
            'creation_date': last_question.creation_date
        }
    else:
        result = {}

    # Возвращаем результат в формате JSON
    return jsonify(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
