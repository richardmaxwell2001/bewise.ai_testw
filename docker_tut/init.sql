
--создание пользователей
CREATE USER task_1;
ALTER USER task_1 WITH PASSWORD '0e0S6af9s6a5DswfcV7HgrDjeed';

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

--права на таблицу
GRANT SELECT, INSERT ON TABLE questions TO task_1;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public to task_1;


CREATE USER task_2;
ALTER USER task_2 WITH PASSWORD 'a41a9ASc363d4G6Q1027F2a50eH867';


--база данных для второго задания
CREATE DATABASE task_2_database;


--гарантия прав созданым пользователям
GRANT CONNECT ON DATABASE task_2_database TO task_2;

\c task_2_database

-- Создание таблицы "users"
CREATE TABLE public.users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    access_token UUID NOT NULL
);

-- Создание таблицы "audioRecords"
CREATE TABLE public.audioRecords (
    record_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES public.users (user_id),
    record_uuid UUID NOT NULL,
);

-- Создание таблицы "audioFiles"
CREATE TABLE public.audioFiles (
    record_id INTEGER PRIMARY KEY REFERENCES audioRecords (record_id),
    file_data BYTEA NOT NULL
);

--права на таблицы
GRANT SELECT, INSERT ON TABLE users, audioRecords, audioFiles TO task_2;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public to task_2;
