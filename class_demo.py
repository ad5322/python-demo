from pprint import pprint

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __bool__(self):
        if self.age < 18 or self.age > 65:
            return False
        return True
    
    def __repr__(self):
        
        return f'{self.name} {self.age}'
    


    
p1 = Person('jane',22)
p2 = Person('john',85)
p1.name = 'arun'
print(p1)

print(bool(p2))