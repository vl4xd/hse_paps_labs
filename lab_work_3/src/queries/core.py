import asyncio
from sqlalchemy import text
from database import async_session_factory


# проверка подключения к базе данных
async def get_db_version():
    version = None
    # контекстный менеджер
    async with async_session_factory() as session:
        res = await session.execute(text('SELECT VERSION()'))
        version = res.first()[0]
    return version
