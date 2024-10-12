import math
class Person():
    counter = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.counter += 1
        
    def greet(self):
        return f'Hello {self.name}'
    
    @classmethod
    def create_anonnymous(cls):
        return Person('deepak',99)

class TempratureConverter():
    @staticmethod
    def Celsius_to_fahrenheit(c):
        return 9 * c / 5 + 32
    
    @staticmethod
    def fahrenheit_to_Celsius(f):
        return 5 * (f - 32) / 9
    
f = TempratureConverter.fahrenheit_to_Celsius(100)
print(math.ceil(f))