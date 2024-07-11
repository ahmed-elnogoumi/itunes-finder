import sqlite3
from db.models import Song
from typing import List
from pydantic import validate_call

conn = sqlite3.connect("app.db")

@validate_call
def add_songs(songs: List[Song]):
    pass