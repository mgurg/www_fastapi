from typing import List, Optional

from pydantic import BaseModel, EmailStr

class CreateUser(BaseModel):
    email: EmailStr
    password : str

class Token(BaseModel):
    access_token: str
    token_type: str