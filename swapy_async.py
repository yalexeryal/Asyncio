import asyncio
import aiohttp
import time


async def get_person(person_id: int) -> dict:
    session = aiohttp.client.ClientSession()
    response = await session.get(f"https://swapi.dev/api/people/{person_id}")
    json_response = await response.json()
    await session.close()
    return json_response


async def main():
    get_person_coroutimes = []
    for person_id in range(1, 110):
        get_person_coro = await get_person(person_id)
        get_person_coroutimes.append(get_person_coro)
    persons = await asyncio.gather(*get_person_coroutimes)
    print(persons)


stat = time.time()
asyncio.run(main())
print(f"Время работы {time.time() - stat}")
