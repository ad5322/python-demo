from pprint import pprint
class car:
    def __init__(self,door,wheel):
        self.door = door
        self.wheel = wheel
        
    def start(self):
        print('start the car')
        
    def go(self):
        print('going')

     
        
class flyable:
    def __init__(self,wing):
        self.wing = wing
        
    def start(self):
        print('start flying the car')
        
    def fly(self):
        print('flying')
        
class flying_car(flyable,car):
    def __init__(self, wing,door,wheel):
        super().__init__(wing)
        self.door = door
        self.wheel = wheel
        
    def __str__(self):
        return f'{self.door} {self.wheel} {self.wing}'
    
        
    def start(self):
        return super().start()

if __name__ == '__main__':
    new = flying_car('wing','door','wheel')
    print(new)
    new.start()
    