from datetime import timedelta, datetime
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer

from jose import JWTError, jwt
from decouple import config

SECRET_KEY = config("SECRET_KEY")
ALGORITHM = config("ALGORITHM")

oauth2_scheme = OAuth2AuthorizationCodeBearer(tokenUrl="token")

def create_access_token(data: dict, expire_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = 
    
    
def generate_expire_date(expire_delta: Optional[timedelta] = None):
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(days=1)
    return expire
