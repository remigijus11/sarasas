FROM python:3.8-slim
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt requirements.txt
run pip3 install -r requirements.txt

COPY . .
CMD ["flask", "run"]