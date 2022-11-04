"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from jsonplaceholder_requests import get_posts, get_users
from models import User, async_session, Post, create_tables


async def get_data():
    reformed_list = []
    all_data = await asyncio.gather(get_users(), get_posts())
    for data_half in all_data:
        for data_block in data_half:
            reformed_list.append(data_block)
    return reformed_list


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

    names = all_data[0]
    usernames = all_data[1]
    emails = all_data[2]

    bodies = all_data[5]
    titles = all_data[4]
    user_ids = all_data[3]

    async with async_session() as db_session:
        async with db_session.begin():
            for i in range(len(all_data[0])):
                namev = names[i]
                usernamev = usernames[i]
                emailv = emails[i]
                await create_user(db_session, namev, usernamev, emailv)

            for d in range(len(all_data[3])):
                bodyv = str(bodies[d])
                titlev = str(titles[d])
                user_idsv = int(user_ids[d])
                await create_post(db_session, bodyv, titlev, user_idsv)


def main():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
