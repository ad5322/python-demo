from pprint import pprint

class counter:
    def __init__(self):
        self.__current = 0
    
    def increment(self):
        self.__current += 1
        
    def value(self):
        return self.__current
        
    def reset(self):
        self.__current = 0
        
c = counter()
c.increment()
c.increment()
print(c.value())
c._counter__current = -999
print(c._counter__current)
