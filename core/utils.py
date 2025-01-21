import datetime
from jose import jwt
from secure.config import settings
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm="HS256")
    return encoded_jwt

# OAuth2PasswordBearer is used to define the token URL to authenticate users
oauth2_login = OAuth2PasswordBearer(
    tokenUrl=settings.SWAGGER_UI_OAUTH2_REDIRECT_URL, 
    scopes={"is_admin": "Super Administrator", "not_admin": "Ordinary Administrator"}
    )

