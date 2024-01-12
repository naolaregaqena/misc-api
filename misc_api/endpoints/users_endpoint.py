from typing import Annotated
from fastapi import APIRouter, Depends
from misc_api.db import db
from aiosqlite import Connection

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("")
async def get_all_users(db: Annotated[Connection, Depends(db)]):
    return await (await db.execute("SELECT * FROM users;")).fetchall()