FROM python:3.10


ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию внутри Docker контейнера
WORKDIR /app_bot


COPY requirements.txt /app_bot/


RUN pip install -r requirements.txt


COPY . /app_bot/


EXPOSE 8000

