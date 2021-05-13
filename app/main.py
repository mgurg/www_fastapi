import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from config.bearer_auth import has_access

from typing import Optional

from routers.auth import auth_router
from routers.static import static_router

from config.settings import get_settings

settings = get_settings()
app = FastAPI()

origins = [
    "http://127.0.0.1:5000",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# routes
PROTECTED = [Depends(has_access)]


app.include_router(
    auth_router,
    prefix='/auth',
    tags=['Authentication'],
)

app.include_router(
    static_router,
    prefix='/static',
    tags=['Static HTML'],
    dependencies=PROTECTED
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users")
async def read_users(skip: int = 0, limit: int = 100):
    return {"skip": skip,
            "limit": limit}


@app.get("/auth_only/")
async def read_items(token: str = Depends(has_access)):
    return {"token": "tkny"}

if __name__ == '__main__':
    if settings.ENV != "production":
        uvicorn.run("main:app", host=settings.HOST,
                    port=settings.PORT, reload=True, debug=True)
    else:
        uvicorn.run("main:app")
