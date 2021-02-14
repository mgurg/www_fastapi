from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from schemas.users import UserBase
from config.settings import Settings

settings = Settings()
auth_router = APIRouter()


@auth_router.post("/register", response_model=UserBase)
async def register(email:str):
    # return {"s"}
    return {"email": email}

@auth_router.post("/login", response_model=UserBase)
async def login(email:str):
    # return {"s"}
    return {"email": "Hello World"}

@auth_router.get("/verify/{token}")
async def verify(token: str):
    pass