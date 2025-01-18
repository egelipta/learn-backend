from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from models.user import User
from schemas.user import UserCreate, UserLogin, TokenResponse
# from secure.jwt import create_access_token
from secure.security import hash_password, verify_password, create_access_token
from secure.config import settings

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/login")  # Sesuaikan dengan endpoint login

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = await User.filter(username=username).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    return user

@router.post("/login", response_model=TokenResponse)
async def login(user_data: UserLogin):
    user = await User.filter(username=user_data.username).first()
    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/protected-route")
async def protected_route(current_user: User = Depends(get_current_user)):
    return {"message": "You have access", "user": current_user.username}
