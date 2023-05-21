import requests
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_request():
    data = request.get_json()
    questions_num = data.get('questions_num')

    # Отправка запроса на https://jservice.io/api/random с параметром count=questions_num
    response = requests.get(f"https://jservice.io/api/random?count={questions_num}")

    # Сохранение пар загадка-ответ в файл
    data = response.json()
    with open('response.txt', 'w') as file:
        for item in data:
            file.write(f"Question: {item['question']}\nAnswer: {item['answer']}\n\n")

    # Возвращаем ответ в формате JSON
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
