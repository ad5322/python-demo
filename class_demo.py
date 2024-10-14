from pprint import pprint

class Person:
    pass
    
    # def __init__(self,name,age):
    #     self.name = name
    #     self.age = age
        
if __name__ == '__main__':
    # x = Person('arun',78)
    x = Person()
    # print(f'{x.name} {x.age}')
    print(x.__dict__)