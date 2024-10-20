from pprint import pprint

class Person:
    def __init__(self,f_name,l_name,age):
        self.first_name = f_name
        self.last_name = l_name
        self.age = age
    
    def __eq__(self, value):
        if isinstance(value,Person):
            return self.age == value.age
        return False
    def __eq__(self, value):
         if isinstance(value,Person):
            return self.last_name == value.last_name
         return False    
     
john = Person('john','doe',25)
jane = Person('jane','doe',27)
print(john == jane)
    
