import uvicorn
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

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
    uvicorn.run("main:app")
