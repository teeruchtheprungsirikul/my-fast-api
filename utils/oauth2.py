from datetime import timedelta, datetime
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer

from jose import JWTError, jwt
from decouple import config