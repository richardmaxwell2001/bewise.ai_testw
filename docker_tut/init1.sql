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
    record_url VARCHAR(255) NOT NULL
);


-- Создание таблицы "audioFiles"
CREATE TABLE public.audioFiles (
    record_id INTEGER PRIMARY KEY REFERENCES audioRecords (record_id),
    file_data BYTEA NOT NULL
);

--права на таблицы
GRANT SELECT, INSERT ON TABLE users, audioRecords, audioFiles TO task_2;
