FROM python:3
EXPOSE 80


COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "-u", "test.py" ]
