# coding: utf-8
from sqlalchemy import BINARY, Column, String, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'users'

    id = Column(INTEGER, primary_key=True)
    uuid = Column(BINARY(16))
    email = Column(String(255), nullable=False, unique=True)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    confirmation = Column(BINARY(16))

# CREATE TABLE users (
#     id int unsigned PRIMARY KEY,
#   	uuid binary(16),
#     email varchar(255) UNIQUE NOT NULL,
#     hashed_password varchar(255) NOT NULL,
#     is_active boolean NOT NULL DEFAULT FALSE,
#     confirmation binary(16)
# )