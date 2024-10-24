import keyword
from pprint import pprint
import random

call_list = []

for i in (1,2,3):
    call_list.append(lambda a = i : a * a)
    
for func in call_list:
    print(func())