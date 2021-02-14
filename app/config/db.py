from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# import os

from config.settings import get_settings

settings = get_settings()

user = settings.db_username  # os.getenv("DB_USERNAME")
password = settings.db_password  # os.getenv("DB_PASSWORD")
host = settings.db_host  # os.getenv("DB_HOST")
database = settings.db_database  # os.getenv("DB_DATABASE")
port = settings.db_port

database = f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}?charset=utf8'

engine = create_engine(database,
                       encoding="utf-8",
                       echo=True,
                       pool_recycle=3600)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# model
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    # Base.metadata.create_all(bind=engine)
    # model.clients.Base.metadata.create_all(bind=engine)
    pass