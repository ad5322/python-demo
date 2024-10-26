from pprint import pprint

class Person:
    def __init__(self,name,age):
        self._name = name
        self.age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if value.sttip() == '':
            raise ValueError('name cannot be empty')
        self._name = value
    
    @name.deleter
    def name(self):
        del self._name
        
# pprint(Person.__dict__)
person = Person('arun',31)
del person._name
print(person._name)
pprint(person.__dict__)