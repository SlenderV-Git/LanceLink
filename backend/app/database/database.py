from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import get_settings
from app.database import Base


engine = create_async_engine(url=get_settings().db.create_url())

async_session = async_sessionmaker(engine, class_=AsyncSession)


async def get_session() -> AsyncSession: # type: ignore
    async with async_session() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()