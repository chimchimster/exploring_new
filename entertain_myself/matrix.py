import random
import sys
from itertools import cycle
from string import ascii_letters

initial_matrix = [[0 for _ in range(10)] for _ in range(10)]

while True:
    counter = 0
    for lst in initial_matrix:
        lst[random.randint(0, 9)] = random.choice(ascii_letters)
        if counter % 2 == 0:
            sys.stdout.write('\t')
            sys.stdout.flush()
            counter = 0
        sys.stdout.write('\n'.join(map(str, lst)))
        sys.stdout.flush()
        counter += 1
