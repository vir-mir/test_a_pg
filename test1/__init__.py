import os
import timeit

from db import create_db

with create_db('thread_async'):
    path = os.path.join(os.getcwd(), 'test1', 'thread_async.py')
    with open(path) as f:
        print('thread:', timeit.timeit(f.read(), number=10))


with create_db('corutine_async'):
    path = os.path.join(os.getcwd(), 'test1', 'corutine_async.py')
    with open(path) as f:
        print('corutine:', timeit.timeit(f.read(), number=10))
