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
    EMAIL_VERIFICATION_TOKEN_EXPIRE_MINUTES: int
    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int
    FIRST_SUPERUSER_EMAIL: str
    FIRST_SUPERUSER_PASSWORD: str
    FIRST_SUPERUSER_NAME: str
    API_HOSTED_ROOT_URL: str
    MAIL_USERNAME :str
    MAIL_PASSWORD :str
    MAIL_FROM:str
    MAIL_PORT:int
    MAIL_SERVER:str
    MAIL_FROM_NAME: str

    class Config:
        env_file = ".env"


settings = Settings()

if ENV == 'prod':
    settings.DATABASE_HOSTNAME = "postgres"
    settings.API_HOSTED_ROOT_URL = "https://nextcare-api-ryuk-me.cloud.okteto.net"
