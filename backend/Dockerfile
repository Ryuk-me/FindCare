FROM python:3.10
ENV ENV=prod 
ENV TZ='Asia/Kolkata'
COPY requirements.txt requirements.txt
COPY . .
RUN pip3 install -r requirements.txt