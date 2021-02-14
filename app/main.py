import uvicorn
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from config.settings import Settings

settings = Settings()

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def read_users(skip: int = 0, limit: int = 100):
    return {"skip" : skip,
	    "limit" : limit}

@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}

if __name__ == '__main__':
    if settings.env != "production":
        uvicorn.run("main:app", host=settings.HOST, port=settings.PORT, reload=True, debug=True)
    else:
        uvicorn.run("main:app")