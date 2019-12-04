import asyncio

import aiopg

import settings

DB_NAME = 'aiopg_create'


def _paginate(seq, page_size):
    page = []
    it = iter(seq)
    while True:
        try:
            for i in range(page_size):
                page.append(next(it))
            yield page
            page = []
        except StopIteration:
            if page:
                yield page
            return


async def execute_batch(cur, sql, argslist, page_size=100):
    for page in _paginate(argslist, page_size=page_size):
        sqls = [cur.mogrify(sql, args) for args in page]
        await cur.execute(b";".join(sqls))


async def insert():
    async with aiopg.connect(
            database=settings.DB_NAME,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            host=settings.DB_HOST,
    ) as conn:
        args = enumerate(range(1, 1000))
        sql = f"insert into {DB_NAME} values (%s,'%s');"
        async with conn.cursor() as cur:
            await execute_batch(cur, sql, args)

asyncio.run(insert())
