import os
from dotenv import load_dotenv

# Memuat file .env
load_dotenv()

TORTOISE_ORM = {
    "connections": {
        "conn": {
            "engine": "tortoise.backends.mysql",
            "credentials": {
                "host": os.getenv("PDA_MYSQL_HOST", "localhost"),
                "user": os.getenv("PDA_MYSQL_USER", "user"),
                "password": os.getenv("PDA_MYSQL_PASSWORD", "rahasia123"),
                "port": int(os.getenv("PDA_MYSQL_PORT", 3306)),
                "database": os.getenv("PDA_MYSQL_DATABASE_NAME", "inidatabase"),
            },
        }
    },
    "apps": {
        "models": {
            "models": ["models.user"],
            "default_connection": "conn",
        },
    },
}
