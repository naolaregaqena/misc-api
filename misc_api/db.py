from functools import lru_cache
from aiosqlite import connect
from os.path import exists
from os import makedirs


@lru_cache
def db():
    db_path = "/var/lib/misc-api/"
    if not exists(db_path):
        makedirs(db_path)
    return connect(f"{db_path}/database.db")
