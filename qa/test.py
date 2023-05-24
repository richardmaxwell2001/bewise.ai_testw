import time
import requests
from requests.exceptions import ConnectionError

time.sleep(1.5)


# -----task_1 тест
url = "http://nginx/task_1"
payload = {"questions_num": 5}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

# Проверяем код состояния HTTP
if response.status_code == 200:
    # Распечатываем полученные данные в формате JSON
    print("task_1: Success")
else:
    # Если получен код ошибки, выводим сообщение об ошибке
    print("task_1 Error: ", response.text)



# ----- task_2 тест
# Создание нового пользователя
new_user_url = "http://nginx/task_2/new_user"
new_user_payload = {"username": "JohnDoe2"}
new_user_headers = {"Content-Type": "application/json"}

try:
    new_user_response = requests.post(new_user_url, json=new_user_payload, headers=new_user_headers)
    new_user_response.raise_for_status()

    # Проверяем код состояния HTTP и выводим результат
    if new_user_response.status_code == 200:
        data_task_2_new_user = new_user_response.json()
    else:
        print("task_2.new_user Error: ", new_user_response.text)

    # Извлекаем токен
    if "access_token" in data_task_2_new_user:
        access_token = data_task_2_new_user["access_token"]
        print("task_2.new_user: Success")
    else:
        print("task_2.new_user Error: no access_token")
        exit(1)

    # Загрузка аудиофайла
    upload_audio_url = "http://nginx/task_2/upload_audio"
    upload_audio_headers = {"Authorization": access_token}

    audio_file = open("./Untitled.mp3", "rb")
    upload_audio_files = {"audio": audio_file}

    try:
        # Прверка безопасности неавторизованым юзером
        wrong_upload_audio_headers = {"Authorization": "ea2ab985-06d6-4554-a47a-f3ba171ee7cb"}

        try:
            upload_audio_response = requests.post(upload_audio_url, headers=wrong_upload_audio_headers, files=upload_audio_files)
            upload_audio_response.raise_for_status()

            # Проверяем код состояния HTTP и выводим результат
            if upload_audio_response.status_code == 200:
                print("task_2.upload_audio Error: ", upload_audio_response.text)
            else:
                print("task_2.upload_audio_by_wrong_token: Success")
        except requests.exceptions.HTTPError as e:
            print("task_2.upload_audio_by_wrong_token Error: ", str(e))
            exit(2)

        # Прверка авторизованым юзером
        try:
            upload_audio_response = requests.post(upload_audio_url, headers=upload_audio_headers, files=upload_audio_files)
            upload_audio_response.raise_for_status()

            # Проверяем код состояния HTTP и выводим результат
            if upload_audio_response.status_code == 200:
                print("task_2.upload_audio: Success")
            else:
                print("task_2.upload_audio Error: ", upload_audio_response.text)
                exit(3)
        except requests.exceptions.HTTPError as e:
            print("task_2.upload_audio Error: ", str(e))
            exit(3)


    except ConnectionError as e:
        print("ConnectionError:", e)
        exit(500)

except ConnectionError as e:
    print("ConnectionError:", e)
    exit(500)
