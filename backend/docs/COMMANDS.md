#

> ## Start server

- `uvicorn app.main:app --port 8009 --reload` or `uvicorn_start.bat`

> ## Migration

- `alembic revision --autogenerate -m "comment"`
- `alembic upgrade head`

> ## To use docker

- Install docker
- `docker-compose up --build`
- now visit `localhost:8009`
  
> ## Seed in DB it will be done in env.py alembic

- Dont seed any data now because database is in its WIP phase.
