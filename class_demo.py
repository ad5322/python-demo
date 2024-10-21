from pprint import pprint

class Person():
    def __init__(self,name,age):
        self.name = name
        self._age = age
        
    @property
    def age(self):
        return self._age
    
    def __repr__(self):
        
        return f'{self.name} {self._age}'
    
    def __eq__(self, other):
        return isinstance(other,Person) and self.age == other.age
    def __hash__(self):
        return hash(self.age)

    
p1 = Person('jane',22)
p2 = Person('john',22)
members = {
    'p1':Person('jane',22),
    'p2':Person('john',22)
}

# print(hash(p1))
# print(hash(p2))
# print(p1 == p2)
print(members['p1'])