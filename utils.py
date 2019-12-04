import asyncio
import sys
import time


def log_time(fn):
    def wrapper(*args, **kwargs):
        t = time.time()
        data = fn(*args, **kwargs)
        fname = fn.__name__
        total = time.time() - t
        print(f'time for {fname} / {round(total, 2)} sec')
        return data

    return wrapper


if sys.version_info >= (3, 7, 0):
    get_running_loop = asyncio.get_running_loop
else:
    def get_running_loop() -> asyncio.AbstractEventLoop:
        loop = asyncio.get_event_loop()
        if not loop.is_running():
            raise RuntimeError('no running event loop')
        return loop
