import asyncio

import aiopg

import settings

DB_NAME = 'aiopg_create'


async def insert():

    async with aiopg.connect(
            database=settings.DB_NAME,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            host=settings.DB_HOST,
    ) as conn:
        async with conn.cursor() as cur:
            for x in range(1, 1000):
                await cur.execute(
                    f"insert into {DB_NAME} values ({x},'{x}');"
                )


asyncio.run(insert())
