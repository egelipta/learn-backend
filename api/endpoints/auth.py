from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from models.user import User
from schemas.user import UserCreate, UserLogin, TokenResponse, UserUpdate
from core.utils import hash_password, verify_password, create_access_token, oauth2_login
from core.message import the_response, fail, success, notfound
from jose import JWTError, jwt
from secure.config import settings

router = APIRouter()

@router.post("/auth/login", response_model=TokenResponse)
async def login(user_login: OAuth2PasswordRequestForm = Depends()):
    # Fetch the user from the database
    user = await User.filter(username=user_login.username).first()

    # Verify that the user exists and the password matches
    if not user or not verify_password(user_login.password, user.password):
        raise HTTPException(status_code=401, detail="Unauthorized")

    # Create and return the access token
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

