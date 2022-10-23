FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN apt-get update -y && apt-get install -y gcc

RUN pip3 install -r requirements.txt
