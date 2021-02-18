from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from models.users import User
from schemas.users import CreateUser, Token
from services.auth import user_exists, create_user, authenticate_user
from config.settings import get_settings
from config.db import get_db


from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, HTTPBearer

from pydantic import EmailStr
import uuid
from jose import jwt

settings = get_settings()
auth_router = APIRouter()


security = HTTPBearer()


@auth_router.post("/register", response_model=CreateUser)
# async def register(email:EmailStr, password : str):
# async def register(form_data: CreateUser = Depends() ):
async def register(form_data: OAuth2PasswordRequestForm = Depends() , db: get_db = Depends()):
    # check if user not exist
    if user_exists(db, form_data.username) != 0 :
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )

    uuid_id = uuid.uuid4()

    create_user(db, form_data.username, form_data.password, uuid_id)

    return {"email": form_data.username,
            "password": form_data.password}


@auth_router.get("/verify/{token}")
async def verify(token: str):
    invalid_token_error = HTTPException(status_code=400, detail="Invalid token")
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.TOKEN_ALGORITHM)
    except jwt.JWTError:
        raise HTTPException(status_code=403, detail="Token has expired")
    if payload['scope'] != 'registration':
        raise invalid_token_error

    # user = await users.UserModel.get_or_none(id=payload['sub'])
    # if not user or str(user.confirmation) != payload['jti']:
    #     raise invalid_token_error
    # if user.is_active:
    #     raise HTTPException(status_code=403, detail="User already activated")
    # user.confirmation = None
    # user.is_active = True
    # await user.save()
    # return await users.User_Pydantic.from_tortoise_orm(user)




@auth_router.post("/login",  response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends() , db: get_db = Depends()):
    user_uuid = authenticate_user(db, form_data.username, form_data.password)
    
    print("LENGHT: ", len(user_uuid['token']))
    print("")
    print(user_uuid['token'])

    return {"access_token": user_uuid['token'], "token_type": "bearer"}
 
 
        

