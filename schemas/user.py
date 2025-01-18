# from pydantic import BaseModel

# class UserCreate(BaseModel):
#     username: str
#     email: str
#     full_name: str = None
#     password: str

from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    full_name: str = None

class UserLogin(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
