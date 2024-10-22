import keyword
from pprint import pprint
import random

def get_net_price(price, discount = 0,tax = 0):
    return price * (1 + tax - discount)

x = get_net_price(discount=0.05,price=100,tax=0.06)
print(abs(x))