FROM python:3.9-alpine

# 작업 디렉토리 설정
WORKDIR /home

# requirements.txt 설치
COPY requirements.txt /home/
RUN pip install -r requirements.txt

