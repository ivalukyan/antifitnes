FROM python:3.10

RUN mkdir /app_bot
WORKDIR /app_bot

ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

