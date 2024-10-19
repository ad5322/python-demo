import keyword
from pprint import pprint
import random

for x in range(1,10):
    for y in range(0,10):
        if y == 2:
            break
        print(f'{x},{y}')