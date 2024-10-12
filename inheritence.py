

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f'{self.name} {self.age}'
    
    def greet(self):
        return f'Hello, i\'am {self.name} '
    
class Employee(Person):
    def __init__(self, name, age,job_title):
        self.job_title = job_title
        super().__init__(name, age)
        
    def __str__(self):
        return super().__str__() + ' ' +  f'{self.job_title}'
    def greet(self):
        return super().greet() + f' i\'am your {self.job_title}'
    
new_emp = Employee('arun',25,'python engineer')
print(new_emp.greet())