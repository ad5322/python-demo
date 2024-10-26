class Person:
    def __init__(self,name):
        self.name = name
        
    def greet(self):
        return f'hello {self.name}'
    
class Employee(Person):
    def __init__(self,name,job_title):
        self.name = name
        self.job_title = job_title
        
class SalesEmployee(Employee):
    pass
        
    
arun = Employee('Arun','Web Developer')
print(arun.greet())