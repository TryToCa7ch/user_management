import os
from dotenv import load_dotenv


class Config:

    def __init__(self):
        if os.path.exists(".env"):
            load_dotenv()

            DB_URL = os.environ.get("DB_URL")

            MIKROTIK_API_HOST = os.environ.get("MIKROTIK_API_HOST")
            MIKROTIK_API_PORT = os.environ.get("MIKROTIK_API_PORT")
            MIKROTIK_USER = os.environ.get("MIKROTIK_USER")
            MIKROTIK_PASSWORD = os.environ.get("MIKROTIK_PASSWORD")

            PORTAINER_API_HOST = os.environ.get("PORTAINER_API_HOST")
            PORTAINER_API_KEY = os.environ.get("PORTAINER_API_KEY")
        else:
            print("No .env file found, environment variables not loaded.")
