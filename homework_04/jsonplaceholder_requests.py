import asyncio
import os

import aiohttp
from dataclasses import dataclass


@dataclass(frozen=True)
class ServiceUsers:
    url: str
    name_field: str
    username_field: str
    email_field: str


@dataclass(frozen=True)
class ServicePosts:
    url: str
    user_id_field: str
    title_field: str
    body_field: str


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

users_service = ServiceUsers(url=USERS_DATA_URL, name_field="name", username_field="username", email_field="email")
posts_service = ServicePosts(url=POSTS_DATA_URL, user_id_field="userId", title_field="title", body_field="body")


async def fetch_json(session: aiohttp.ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        data = await response.json()
        return data


async def fetch_data(service):
    async with aiohttp.ClientSession() as session:
        data: dict = await fetch_json(session, service.url)
        return data


def main():
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


if __name__ == '__main__':
    main()
