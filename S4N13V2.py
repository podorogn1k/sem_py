from time import *
from contextlib import contextmanager

@contextmanager
def Timer():
    start = time()
    try:
        yield
    finally:
        end = time()
        t = end - start
        print(t)

with Timer():
    a = ([i for i in range(25)])
    sleep(0.25)