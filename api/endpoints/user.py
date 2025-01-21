from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from models.user import User
from schemas.user import UserCreate, UserLogin, TokenResponse, UserUpdate
from core.utils import hash_password, verify_password, create_access_token, oauth2_login
from core.message import the_response, fail, success, notfound
from jose import JWTError, jwt
from secure.config import settings

router = APIRouter()

@router.post("/user/register")
async def register_user(user: UserCreate, token: str = Depends(oauth2_login)):
    existing_user = await User.get_or_none(username=user.username)
    if existing_user:
        return fail(msg=f"username {user.username} already exists!")

    hashed_password = hash_password(user.password)
    new_user = await User.create(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        password=hashed_password,
    )
    # token = create_access_token({"sub": new_user.username})
    # return {"access_token": token, "token_type": "bearer"}
    return success(msg=f"Username {user.username} created!")

@router.get("/users/current-user")
async def get_current_user(token: str = Depends(oauth2_login)):
    try:
        # Decode JWT token
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        # Ambil data pengguna dari database
        user = await User.filter(username=username).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        # Kembalikan informasi pengguna
        return {
            "id": user.id,
            "name": user.full_name,
            "username": user.username,
            "email": user.email
        }
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


@router.get("/users/get-all-users")
async def get_all_users(token: str = Depends(oauth2_login)):
    users = await User.all()
    total = await User.all().count()  # Hitung total pengguna
    data = [
        {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "full_name": user.full_name,
        }
        for user in users
    ]
    return the_response(code=True, data=data, total=total)


@router.get("/users/{user_id}")
async def get_user(user_id: int, token: str = Depends(oauth2_login)):
    user = await User.filter(id=user_id).first()
    if user:
        return {"id": user.id, "username": user.username, "email": user.email}
    else:
        return notfound(msg=f"User Not Found")

@router.post("/user/login", response_model=TokenResponse)
async def login(login_data: UserLogin):
    # Ambil user dari database berdasarkan username
    user = await User.filter(username=login_data.username).first()

    # Verifikasi apakah user ada dan password yang dimasukkan benar
    if not user or not verify_password(login_data.password, user.password):
        raise HTTPException(status_code=401, detail="Unauthorized")

    # Membuat dan mengembalikan access token
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}


@router.put("/users/update")
async def update_user(user_data: UserUpdate, token: str = Depends(oauth2_login)):
    # Cari user berdasarkan ID
    user = await User.filter(id=user_data.id).first()
    
    if not user:
        return notfound(msg=f"User Not Found")

    # Hapus 'id' dari data update
    update_data = user_data.dict(exclude_unset=True, exclude={"id"})  

    # Jika password diubah, hash dulu
    if "password" in update_data:
        update_data["password"] = hash_password(update_data["password"])  

    # Update data user
    await User.filter(id=user_data.id).update(**update_data)

    # Ambil data terbaru setelah update
    updated_user = await User.filter(id=user_data.id).first()

    return success(msg=f"User {user.username} Updated")


@router.delete("/users/delete/{user_id}")
async def delete_user(user_id: int, token: str = Depends(oauth2_login)):
    # Cari user berdasarkan ID
    user = await User.filter(id=user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Hapus user
    await user.delete()

    return {
        "code": True,
        "message": "User deleted successfully"
    }

