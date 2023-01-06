> ## Start server

- `uvicorn app.main:app --port 8009 --reload` or `uvicorn_start.bat`

> ## Migration

- `alembic revision --autogenerate -m "comment"`
- `alembic upgrade head`

> ## To use docker

- Install docker
- `docker-compose up --build`
- now visit `localhost:8009`
