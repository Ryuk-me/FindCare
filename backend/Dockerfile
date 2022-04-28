FROM python:3.10
ENV ENV=prod 
COPY ./backend/requirements.txt requirements.txt
COPY backend .
RUN pip3 install -r requirements.txt