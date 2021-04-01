# coding: utf-8
from sqlalchemy import BINARY, Column, String, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'users'

    id = Column(INTEGER, primary_key=True)
    uuid = Column(String(255))
    email = Column(String(255), nullable=False, unique=True)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    confirmation = Column(String(255))


# CREATE TABLE `users` (
#   `id` int unsigned NOT NULL AUTO_INCREMENT,
#   `uuid` varchar(255) DEFAULT NULL,
#   `email` varchar(255) NOT NULL,
#   `hashed_password` varchar(255) NOT NULL,
#   `is_active` tinyint(1) NOT NULL DEFAULT '0',
#   `confirmation` varchar(255) DEFAULT NULL,
#   PRIMARY KEY (`id`),
#   UNIQUE KEY `email` (`email`)
# ) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
