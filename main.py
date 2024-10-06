class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def __repr__(self) -> str:
        return f'person {self.first_name} {self.last_name} {self.age}'
    
    def __eq__(self, other) -> bool:
         return self.age == other.age , self.last_name == other.last_name , \
         self.first_name == other.first_name
         
    

                
                
        
arun  = Person('arun','deepak',31)
kali = Person('kali','deepak',31)

print(arun == kali)



