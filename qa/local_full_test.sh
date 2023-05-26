#!/bin/bash

# Создано 25.05.23
# Скрипт для работы с API тестового задания 2

sleep 3

file_path="./Imput.wav"

# Создание нового пользователя и получение access_token и user_id
response=$(curl -s -X POST -H "Content-Type: application/json" -d '{"username":"JohnDoe2"}' http://localhost/task_2/new_user)
access_token=$(echo "$response" | grep -o '"access_token":"[^"]*' | cut -d '"' -f 4)
user_id=$(echo "$response" | grep -o '"user_id":[0-9]*' | cut -d ':' -f 2)

echo -e "User \e[34mJohnDoe2\e[0m with user_id \e[34m$user_id\e[0m and access_token: \e[34m$access_token\e[0m has been registered"

# Отправка запроса с использованием cURL
response=$(curl -s -F 'Access_token='"$access_token" -F 'User_id'="$user_id" -F "audio=@./$file_path" http://localhost/task_2/upload_audio)

# Извлечение URL из JSON-ответа
download_url=$(echo "$response" | grep -o '"URL":"[^"]*' | cut -d '"' -f 4)

echo -e "The file \e[34m$file_path\e[0m was sent and is now available for download at \e[38;5;208m$download_url\e[0m"

echo "File downloading..."

# Выполнение запроса для загрузки файла
curl -s -o file.mp3 "$download_url"

echo "End"
