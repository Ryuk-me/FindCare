FROM python:3.8
ADD backend/requirements.txt requirements.txt
ADD backend/main.py main.py
ADD backend/okteto-stack.yaml okteto-stack.yaml
RUN pip install -r requirements.txt
EXPOSE 8080
COPY backend .
CMD ["uvicorn", "app.main:app", "--port", "8008", "--reload"]