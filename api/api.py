from fastapi import APIRouter
from api.endpoints import user, auth

api_router = APIRouter(prefix="/api/v1")

# Mendaftarkan endpoint user
api_router.include_router(auth.router, tags=["OAuth2"])
api_router.include_router(user.router, tags=["Users"])

# api_router.include_router(auth_router)