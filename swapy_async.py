import aiohttp
import asyncio
import time
from more_itertools import chunked

from typing import Iterable

BOTLE_NECK = 10


async def get_persons(session: aiohttp.client.ClientSession(), range_person_id: Iterable[int]):
    for person_id_chank in chunked(range(1, 110), BOTLE_NECK):
        get_person_tasks = [asyncio.create_task(get_person(session, person_id)) for person_id in person_id_chank]
        persons = await asyncio.gether(*get_person_tasks)
        for person in persons:
            yield person


async def get_person(session: aiohttp.client.ClientSession, person_id: int) -> dict:
    async with session.get(f"https://swapi.dev/api/people/{person_id}") as response:
        response_json = await response.json()
        return response_json


async def main():
    async with aiohttp.client.ClientSession() as session:
        async for person in get_persons(session, range(1, 100)):
            print(person)


stat = time.time()
asyncio.run(main())
print(f"Время работы {time.time() - stat}")
