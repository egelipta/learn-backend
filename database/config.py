import os
from dotenv import load_dotenv

# Memuat file .env
load_dotenv()

TORTOISE_ORM = {
    "connections": {
        "conn": {
            "engine": "tortoise.backends.mysql",
            "credentials": {
                "host": os.getenv("CONF_MYSQL_HOST", "localhost"),
                "user": os.getenv("CONF_MYSQL_USER", "user"),
                "password": os.getenv("CONF_MYSQL_PASSWORD", "rahasia123"),
                "port": int(os.getenv("CONF_MYSQL_PORT", 3306)),
                "database": os.getenv("CONF_MYSQL_DATABASE_NAME", "database"),
            },
        }
    },
    "apps": {
        "user": {"models": ["models.user"],"default_connection": "conn"},
    },
}
