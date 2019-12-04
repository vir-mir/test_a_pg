import os
import timeit

from db import create_db

with create_db('asyncpg_create'):
    path = os.path.join(os.getcwd(), 'test2', 'asyncpg_create.py')
    with open(path) as f:
        print('asyncpg:', timeit.timeit(f.read(), number=10))


with create_db('aiopg_create'):
    path = os.path.join(os.getcwd(), 'test2', 'aiopg_create.py')
    with open(path) as f:
        print('aiopg:', timeit.timeit(f.read(), number=10))
