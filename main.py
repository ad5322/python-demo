import keyword
from pprint import pprint
import random

age = int(input('enter your age \n'))

ticket_price = 20 if age >= 18 else 5

print(f'your ticket price is ${ticket_price}')