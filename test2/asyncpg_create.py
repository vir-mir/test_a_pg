import asyncio

import asyncpg

import settings

DB_NAME = 'asyncpg_create'


async def insert():
    conn = await asyncpg.connect(
        database=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST
    )

    for x in range(1, 1000):
        await conn.execute(
            f"insert into {DB_NAME} values ($1, $2);",
            x, str(x)
        )
    await conn.close()

asyncio.run(insert())
