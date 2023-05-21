
--создание пользователей
CREATE USER task_1;
ALTER USER task_1 WITH PASSWORD '0e0S6af9s6a5DswfcV7HgrDjeed';

CREATE USER task_2;
ALTER USER task_2 WITH PASSWORD 'a41a9ASc363d4G6Q1027F2a50eH867';



--база данных для первого задания

CREATE DATABASE task_1_database;


--гарантия прав созданым пользователям
GRANT CONNECT ON DATABASE task_1_database TO task_1;

\c task_1_database;

-- Создание таблицы questions
CREATE TABLE public.questions (
  id SERIAL PRIMARY KEY,
  question_id INTEGER,
  question_text TEXT,
  answer_text TEXT,
  creation_date TIMESTAMP
);

GRANT SELECT, INSERT ON TABLE questions TO task_1;
GRANT USAGE, SELECT ON SEQUENCE questions_id_seq TO task_1;


--база данных для второго задания

CREATE DATABASE task_2_database;

