import pytest
from scripts.db import Database
import os

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
DB_PATH = os.path.join(PATH, "outputs/test_twitter.db")


@pytest.fixture
def db():
    try:
        os.remove(DB_PATH)
    except FileNotFoundError:
        pass
    db = Database(DB_PATH)
    db._create_tables()
    return db
