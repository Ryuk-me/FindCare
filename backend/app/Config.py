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

    if ENV == 'prod':
        class Config:
            env_file = ".env"
    else:
        class Config:
            env_file = ".env.local"


settings = Settings()

if ENV == 'prod':
    settings.DATABASE_HOSTNAME = "postgres"
    settings.API_HOSTED_ROOT_URL = "https://nextcare-api-ryuk-me.cloud.okteto.net/"
    settings.MAIL_USERNAME = os.environ['MAIL_USERNAME']
    settings.MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
    settings.MAIL_FROM = os.environ['MAIL_FROM']
    settings.MAIL_PORT = os.environ['MAIL_PORT']
    settings.MAIL_SERVER = os.environ['MAIL_SERVER']
    settings.MAIL_FROM_NAME = os.environ['MAIL_FROM_NAME']
