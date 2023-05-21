import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

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

def insert_data() -> None:
    # Ввод данных для подключения
    # По хорошему надо бы их тянуть
    # username: str = "task_1"
    # password: str = "0e0S6af9s6a5DswfcV7HgrDjeed"
    username: str = "docker"
    password: str = "docker"

    # Формирование строки подключения
    connection_string: str = f'postgresql://{username}:{password}@db:5432/task_1_database'

    # Подключение к базе данных
    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Создание объекта вопроса
    question = Question(
        id=0,
        question_id=56140,
        question_text='A sign on the road to Carlsbad Caverns reads, "Do not pick up" these; "prison facilities in this area"',
        answer_text='hitchhikers',
        creation_date='2022-12-30T19:01:36.074Z'
    )

    # Добавление объекта вопроса в сессию
    session.add(question)

    # Сохранение изменений
    session.commit()

    # Закрытие сессии
    session.close()

insert_data()

'''

from sqlalchemy import create_engine, text

def insert_data() -> None:
    # Ввод данных для подключения
    # По хорошему надо бы их тянуть
    #username: str = "task_1"
    #password: str = "0e0S6af9s6a5DswfcV7HgrDjeed"
    username: str = "docker"
    password: str = "docker"

    # Формирование строки подключения
    connection_string: str = f'postgresql://{username}:{password}@db:5432/task_1_database'

    # Подключение к базе данных
    engine = create_engine(connection_string)
    connection = engine.connect()

    # Пример вставки данных
    query: str = """
    INSERT INTO public.questions (question_id, question_text, answer_text, creation_date)
    VALUES (56140, 'A sign on the road to Carlsbad Caverns reads, "Do not pick up" these; "prison facilities in this area"', 'hitchhikers', '2022-12-30T19:01:36.074Z');
    """
    statement = text(query)
    connection.execute(statement)

    # Сохранение изменений
    connection.commit()

    # Закрытие соединения
    connection.close()

insert_data()



from sqlalchemy import create_engine

# Ввод данных для подключения
# По хорошему надо бы их тянуть
username = "task_1"
password = "0e0S6af9s6a5DswfcV7HgrDjeed"

# Формирование строки подключения
connection_string = f'postgresql://{username}:{password}@db:5432/task_1_database'

# Подключение к базе данных
engine = create_engine(connection_string)
connection = engine.connect()



# Выполнение SQL-запроса
result = connection.execute("SELECT * FROM public.questions")

# Вывод результатов
for row in result:
    print(row)

# Закрытие соединения
connection.close()



query = "SELECT datname FROM pg_database WHERE datistemplate = false;"

# Выполнение SQL-запроса
result = connection.execute(query)

'''
