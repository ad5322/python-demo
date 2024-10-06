class Person:
    
    def __init__(self,fname,lname) -> None:
        self.fname = fname
        self.lname = lname
        
    def __str__(self) -> str:
        return f'hello {self.fname} {self.lname}'
    
arun = Person('arun','deepak')

print(arun)