import asyncio

import psycopg2

import settings
from utils import get_running_loop

DB_NAME = 'corutine_async'


def ready(conn, waiter):
    loop = get_running_loop()
    fileno = conn.fileno()
    state = conn.poll()
    if state == psycopg2.extensions.POLL_OK:
        loop.remove_writer(fileno)
        loop.remove_reader(fileno)
        waiter.set_result(None)
    elif state == psycopg2.extensions.POLL_WRITE:
        loop.add_writer(fileno, ready, conn, waiter)
    elif state == psycopg2.extensions.POLL_READ:
        loop.remove_writer(fileno)
        loop.add_reader(fileno, ready, conn, waiter)
    else:
        raise psycopg2.OperationalError("poll() returned %s" % state)


async def wait(conn):
    waiter = get_running_loop().create_future()
    ready(conn, waiter)
    await asyncio.wait_for(waiter, 100)


async def ainsert(data_range, tid, sleep):
    aconn = psycopg2.connect(
        database=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        async_=1
    )
    await wait(aconn)
    acurs = aconn.cursor()

    for id in data_range:
        acurs.execute(f"insert into {DB_NAME} values ({id},'{tid}');")
        await wait(acurs.connection)

    acurs.close()
    aconn.close()


def run_ainsert():
    loop = asyncio.get_event_loop()
    tasks = [
        loop.create_task(ainsert(range(1, 9999), 1, 0.1)),
        loop.create_task(ainsert(range(1, 9999), 2, 0.2)),
    ]
    loop.run_until_complete(asyncio.wait(tasks))


run_ainsert()
