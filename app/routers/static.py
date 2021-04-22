from fastapi import APIRouter
from fastapi import Depends, HTTPException, status

from config.settings import get_settings

settings = get_settings()
static_router = APIRouter()


@static_router.get("/hello")
async def hello():
    return {"message": "Hello World"}
