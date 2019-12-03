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
