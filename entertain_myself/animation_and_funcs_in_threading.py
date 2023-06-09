import sys
import time
import threading
import _thread
from functools import wraps


class TreadTasks(threading.Thread):
    def __init__(self, name, func, args):
        super().__init__()
        self.name = name
        self.func = func
        self.args = args
        self.result = None

    def get_result(self):
        return self.result

    def run(self):
        self.result = self.func(*self.args)


def animate(flag=True, lock=None):
    def get_symbol():
        yield '┃'

    counter = 0
    while True:
        if not flag:
            break
        if counter % 17 == 0:
            sys.stdout.write('\r')
        sys.stdout.write(next(get_symbol()))
        sys.stdout.flush()
        time.sleep(0.1)
        counter += 1
    sys.stdout.write('\rDone')
    lock.release()


def cache(func):
    memo = {}
    @wraps(func)
    def wrapper(*args):

        if args in memo:
            return memo[args]
        else:
            f = func(*args)
            memo[args] = f
            return f

    return wrapper

@cache
def fib(n=888):
    if n < 2:
        return 1
    print(n, end=' ')
    return fib(n-2) + fib(n-1)


def main():
    funcs = [animate, fib]

    locks = []
    for _ in range(len(funcs)):
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for _ in range(len(funcs)):
        _thread.start_new_thread(funcs[_], ())

    for _ in range(len(funcs)):
        while locks[_].locked():
            pass


if __name__ == '__main__':
    main()