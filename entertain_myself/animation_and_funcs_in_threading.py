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



flag = True


def animate():
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
    global flag
    flag = False
    return wrapper

@cache
def fib(n=888):
    if n < 2:
        return 1

    return fib(n-2) + fib(n-1)


def main():
    funcs = [animate, fib]
    threads = []
    for func in funcs:
        threads.append(TreadTasks(func.__name__, func, ()))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()