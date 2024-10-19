import keyword
from pprint import pprint
import random

counter = 0
while counter < 10:
    counter += 1
    if not counter % 2:
        continue
    print(counter)