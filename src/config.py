import os
from dotenv import load_dotenv

try:
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
DATABASE_FILE_PATH = os.path.join(
    os.path.dirname(__file__), "..", "data", DATABASE_FILENAME)
