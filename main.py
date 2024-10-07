from pprint import pprint

class Person:
    def __init__(self,name) -> None:
        self.name = name
  
    def greet(self):
        return f'hello, it\'s {self.name}'
    
class Employee(Person):
    def __init__(self, name,job_title) -> None:
        super().__init__(name)
        self.job_title = job_title
        

new_employee = Employee('arun','python developer')

pprint(new_employee.greet())



