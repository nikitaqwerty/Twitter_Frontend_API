import pytest
from scripts.db import Database
import os

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


@pytest.fixture
def db():
    db = Database(PATH,'test_twitter.db',recreate=True)
    db._create_tables()
    return db

