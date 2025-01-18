from fastapi import FastAPI
from tortoise import Tortoise
from database.config import TORTOISE_ORM
from api.api import api_router
from secure.config import settings


application = FastAPI(title="LEARN_BACKEND")

# Menghubungkan router ke aplikasi FastAPI
application.include_router(api_router)

@application.on_event("startup")
async def startup():
    await Tortoise.init(config=TORTOISE_ORM)
    # await Tortoise.generate_schemas()
    

app = application
