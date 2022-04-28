from pydantic import BaseSettings
import os

try:
    ENV = os.environ['ENV']
except:
    ENV = None


class Settings(BaseSettings):
    BASE_API_V1: str
    DATABASE_HOSTNAME: str
    DATABASE_PORT: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    DATABASE_USERNAME: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    FIRST_SUPERUSER_EMAIL: str
    FIRST_SUPERUSER_PASSWORD: str
    FIRST_SUPERUSER_NAME: str

    class Config:
        env_file = ".env"


settings = Settings()

if ENV == 'prod':
    settings.DATABASE_HOSTNAME = "postgres"
