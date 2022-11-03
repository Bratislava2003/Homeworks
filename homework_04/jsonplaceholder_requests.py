import asyncio, aiohttp
from dataclasses import dataclass
from loguru import logger


@dataclass(frozen=True)
class Service_Users:
    url: str
    name_field: str
    username_field: str
    email_field: str


@dataclass(frozen=True)
class Service_Posts:
    url: str
    user_id_field: str
    title_field: str
    body_field: str


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

users_service = Service_Users(url=USERS_DATA_URL, name_field="name", username_field="username", email_field="email")
posts_service = Service_Posts(url=POSTS_DATA_URL, user_id_field="userId", title_field="title", body_field="body")


async def fetch_json(session: aiohttp.ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        data = await response.json()
        return data


async def fetch_data_users(service):
    async with aiohttp.ClientSession() as session:
        data: dict = await fetch_json(session, service.url)
        # iter_dict = list(users_service.__dict__.keys())[1:]
        result_users = [
            list(data_item.get(service.name_field) for data_item in data),
            list(data_item.get(service.username_field) for data_item in data),
            list(data_item.get(service.email_field) for data_item in data)
        ]
        return result_users


async def fetch_data_posts(service):
    async with aiohttp.ClientSession() as session:
        data: dict = await fetch_json(session, service.url)
        result_posts = [
            list(data_item.get(service.user_id_field) for data_item in data),
            list(data_item.get(service.title_field) for data_item in data),
            list(data_item.get(service.body_field) for data_item in data)
        ]
        return result_posts


async def get_users():
    logger.info("getting users...")
    res = await fetch_data_users(users_service)
    return res


async def get_posts():
    logger.info("Getting posts...")
    res = await fetch_data_posts(posts_service)
    return res


def main():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    logger.info("Started main")
    users = asyncio.run(get_users())
    posts = asyncio.run(get_posts())
    logger.info("List of users: {}", users)
    logger.info("Posts list: {}", posts)


if __name__ == '__main__':
    logger.info("Users service info: {}", list(users_service.__dict__.values())[1:])
    main()
