import keyword
from pprint import pprint
import random

def sum(n):
    return n + sum(n-1) if n > 0 else 0
      
    
print(sum(100))

    
# def sum(x):    
#     total = 0
#     for y in range(x+1):
#         total = y + total
    
#     return total

# print(sum(100))