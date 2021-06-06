from sqlalchemy.orm import Session
from config.settings import get_settings
from models.users import User
from tools.notification import Notify
from tools.mailer import Mailer

from passlib.context import CryptContext

from datetime import datetime, timedelta
from pydantic import UUID4
import uuid
from jose import jwt
import bcrypt


settings = get_settings()


def user_exists(db: Session, user_mail: int) -> int:
    return db.query(User).filter(User.email == user_mail).count()


def user_uuid_exists(db: Session, user_uuid: str):
    return db.query(User).filter(User.uuid == user_uuid).one_or_none()


def authenticate_user(db: Session, username: str, password: str) -> str:
    user = db.query(User).filter(User.email == username).first()

    hash_pass = user.hashed_password

    if bcrypt.checkpw(password.encode('utf8'), hash_pass.encode('utf8')):
        return Auth.get_session_token(user.uuid)

    return None


def create_user(db: Session, username: str, password: str, uuid_id: str):
    hashed_password = Auth.get_password_hash(password)
    confirmation = Auth.get_confirmation_token(uuid_id)

    # print("jti: ")
    # print(confirmation['jti'])

    # print("token: ")
    # print(confirmation['token'])

    db_user = User(email=username, hashed_password=hashed_password,
                   uuid=str(uuid_id), confirmation=str(confirmation['jti']))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    Notify.send_confirmation_message(confirmation["token"])
    # Mailer.send_confirmation_message(confirmation["token"], "mgurgul@telecube.pl")
    return db_user


class Auth:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def get_password_hash(cls, password: str) -> str:
        # bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
        return cls.pwd_context.hash(password)

    @staticmethod
    def get_token(data: dict, expires_delta: int):
        to_encode = data.copy()
        to_encode.update({
            "exp": datetime.utcnow() + timedelta(seconds=expires_delta),
            "iss": settings.APP_NAME
        })
        return jwt.encode(
            to_encode,
            settings.SECRET_KEY,
            algorithm=settings.TOKEN_ALGORITHM
        )

    @staticmethod
    def get_confirmation_token(user_id: UUID4):
        jti = uuid.uuid4()
        claims = {
            "sub": str(user_id),
            "scope": "registration",
            "jti": str(jti)
        }
        return {
            "jti": jti,
            "token": Auth.get_token(
                claims,
                settings.REGISTRATION_TOKEN_LIFETIME
            )
        }

    @staticmethod
    def get_session_token(user_id: UUID4):
        jti = uuid.uuid4()
        claims = {
            "sub": str(user_id),
            "scope": "login",
            "jti": str(jti)
        }
        return {
            "jti": jti,
            "token": Auth.get_token(
                claims,
                settings.REGISTRATION_TOKEN_LIFETIME
            )
        }
