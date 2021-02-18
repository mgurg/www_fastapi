from jose import jwt
from jose.exceptions import JOSEError
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBasicCredentials, HTTPBearer

from config.settings import get_settings

settings = get_settings()


security = HTTPBearer()


async def has_access(credentials: HTTPBasicCredentials = Depends(security)):
    """
        Function that is used to validate the token in the case that it requires it
    """
    token = credentials.credentials

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.TOKEN_ALGORITHM, options={"verify_signature": False,
                                                                                                       "verify_aud": False,
                                                                                                       "verify_iss": False})
        print("payload => ", payload)
    except JOSEError as e:  # catches any exception
        raise HTTPException(
            status_code=401,
            detail=str(e))
            
    return "fake_token"
