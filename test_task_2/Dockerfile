FROM python:3
EXPOSE 5000

RUN apt-get update && apt-get install -y ffmpeg

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "-u", "main.py" ]
