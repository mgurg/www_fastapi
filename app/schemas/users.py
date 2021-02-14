from typing import List, Optional

from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr