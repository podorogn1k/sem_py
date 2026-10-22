from time import *

class Timer:
    def __enter__(self):
        self.start = time()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time()
        self.t = self.end - self.start
        print(self.t)

with Timer():
    a = sum([i for i in range(25)])
    sleep(0.25)