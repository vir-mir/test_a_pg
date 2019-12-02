from contextlib import contextmanager

import psycopg2

import settings


@contextmanager
def create_db(db_name):
    conn = psycopg2.connect(
        database=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST
    )
    cur = conn.cursor()
    try:
        cur.execute(f'CREATE TABLE {db_name} (id integer, data varchar(255))')
        conn.commit()
        yield
    finally:
        cur.execute(f'DROP TABLE {db_name}')
        conn.commit()
        conn.close()
        cur.close()
