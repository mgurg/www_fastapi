import logging
import os

from pathlib import Path
from dotenv import load_dotenv

from functools import lru_cache
from pydantic import BaseSettings

env_path = Path(".") / "app"/".env"
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    ENV: str = os.getenv("WORKING_ENVIRONMENT", "dev")
    NAME: str = os.getenv("APP_NAME", "no-name")

    HOST: str = os.getenv("HOST", "127.0.0.1")
    PORT: int = os.getenv("PORT", 5000)

    REGISTRATION_TOKEN_LIFETIME: int = 60*60
    APP_NAME = "FAW"
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    TOKEN_ALGORITHM = "HS256"

    db_connection: str = os.getenv("DB_CONNECTION")
    db_host: str = os.getenv("DB_HOST")
    db_port: int = os.getenv("DB_PORT")
    db_database: str = os.getenv("DB_DATABASE")
    db_username: str = os.getenv("DB_USERNAME")
    db_password: str = os.getenv("DB_PASSWORD")

    class Config:
        env_prefix = ""
        env_file_encoding = "utf-8"
        env_file = ".env"


@lru_cache()
def get_settings() -> BaseSettings:
    return Settings()
