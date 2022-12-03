import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
import os
from jsonplaceholder_requests import fetch_data, users_service, posts_service
from models import User, Session, Post, create_tables


async def get_data():
    all_data = await asyncio.gather(fetch_data(users_service), fetch_data(posts_service))
    for i in all_data:
        for a in i:
            print(a)
    return all_data


async def create_user(session: AsyncSession, user_name: str, username: str, email: str):
    user = User(name=user_name, username=username, email=email)
    session.add(user)
    return user


async def create_post(session: AsyncSession, body: str, title: str, user_id: int):
    post = Post(title=title, body=body, user_id=user_id)
    session.add(post)
    return post


async def async_main():
    await create_tables()

    all_data = await get_data()

    users = all_data[0]
    posts = all_data[1]

    async with Session() as db_session:
        async with db_session.begin():
            for user in users:
                name = user.get(users_service.name_field)
                username = user.get(users_service.username_field)
                email = user.get(users_service.email_field)
                await create_user(session=db_session, user_name=name, username=username, email=email)

            for post in posts:
                uid = post.get(posts_service.user_id_field)
                title = post.get(posts_service.title_field)
                body = post.get(posts_service.body_field)
                await create_post(session=db_session, user_id=uid, title=title, body=body)


def main():
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
