import keyword
from pprint import pprint
import random

x = int(input('enter your age \n'))

if x <= 5:
    ticket_price = 5
elif (x > 5 and x < 25):
    ticket_price = 25
else:
    ticket_price = 30

print(f'your ticket price is ${ticket_price}')