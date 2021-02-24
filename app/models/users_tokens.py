# coding: utf-8
from sqlalchemy import Column, Integer, String, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class UsersToken(Base):
    __tablename__ = 'users_tokens'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    auth_token = Column(String(255), nullable=False)


# CREATE TABLE `users_tokens` (
#   `id` int NOT NULL AUTO_INCREMENT,
#   `user_id` int NOT NULL,
#   `auth_token` varchar(255) NOT NULL,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci