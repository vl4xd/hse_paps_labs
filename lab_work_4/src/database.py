from typing import Annotated
from sqlalchemy import Integer, String, create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config import settings


async_engine = create_async_engine(
    url = settings.DATABASE_URL_asyncpg,
    echo = True,
)

async_session_factory = async_sessionmaker(async_engine)


str_4 = Annotated[str, 4]
str_25 = Annotated[str, 25]
str_50 = Annotated[str, 50] 
str_100 = Annotated[str, 100]
str_256 = Annotated[str, 256]
int_4 = Annotated[int, 4]

class Base(DeclarativeBase):
    type_annotation_map = {
        str_4: String(4),
        str_25: String(25),
        str_50: String(50),
        str_100: String(100),
        str_256: String(256),
    }
