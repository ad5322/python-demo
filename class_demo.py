from pprint import pprint

class Person():
    def __init__(self,f_name,l_name,age):
        self.first_name = f_name
        self.last_name = l_name
        self.age = age
        
    def __str__(self):
        return f'Person - {self.first_name} {self.last_name} {self.age}'
    
    # def __repr__(self):
    #     return f'{self.first_name} '
person  = Person('arun','deepak',31)
print(person)
print(repr(person))
print(person)