from fastapi import APIRouter, HTTPException, Depends
from models.user import User
from schemas.user import UserCreate, UserLogin, TokenResponse
from secure.utils import hash_password, verify_password, create_access_token

router = APIRouter()

@router.post("/user/register", response_model=TokenResponse)
async def register_user(user: UserCreate):
    existing_user = await User.filter(username=user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_password = hash_password(user.password)
    new_user = await User.create(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password,
    )

    token = create_access_token({"sub": new_user.username})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/users/{user_id}")
async def get_user(user_id: int):
    user = await User.filter(id=user_id).first()
    if user:
        return {"id": user.id, "username": user.username, "email": user.email}
    else:
        raise HTTPException(status_code=404, detail="User not found")

@router.post("/user/login", response_model=TokenResponse)
async def login(user_login: UserLogin):
    user = await User.filter(username=user_login.username).first()
    if not user or not verify_password(user_login.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}


