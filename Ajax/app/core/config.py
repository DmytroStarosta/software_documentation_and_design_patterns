from os import getenv
from dotenv import load_dotenv

load_dotenv()
DATABASE_URI = getenv("DATABASE_URI")