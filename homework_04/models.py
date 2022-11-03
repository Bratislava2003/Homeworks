import asyncio

from sqlalchemy import Column, INTEGER, String, ForeignKey
from sqlalchemy.orm import declared_attr, declarative_base, sessionmaker, relationship
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from loguru import logger

PG_CONN_URI = "postgresql+asyncpg://username:passwd!@localhost/postgres"

async_engine: AsyncEngine = create_async_engine(
    PG_CONN_URI,
    echo=True
)


class Base:
    @declared_attr
    def __tablename__(cls):
        return f'{cls.__name__.lower()}s'

    id = Column(INTEGER, primary_key=True)

    def __repr__(self):
        return str(self)


Base = declarative_base(cls=Base)


class User(Base):
    name = Column(String, unique=False, nullable=False, default="")
    username = Column(String, unique=True, nullable=False, default="")
    email = Column(String, unique=True, nullable=False, default="")
    posts = relationship("Post", back_populates="user", uselist=True)


class Post(Base):
    user_id = Column(INTEGER, ForeignKey('users.id'), unique=False, nullable=False)
    title = Column(String, unique=False, nullable=False)
    body = Column(String, unique=False, nullable=False, default="No body detected")
    user = relationship("User", back_populates="posts", uselist=False)


async_session = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=True
)


async def create_tables():
    logger.info("Starting func...")
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        logger.success("Created tables")


async def main():
    await create_tables()


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
