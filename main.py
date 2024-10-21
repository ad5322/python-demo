import keyword
from pprint import pprint
import random

def greet(name,greet='hi'):
    return print(f'{greet} {name}')

greet('arun','hello')
greet('arun',greet='hey!.')