from pprint import pprint


class Employee:
    def __init__(self, name,base_pay,bonus) -> None:
        self.name = name
        self.base_pay = base_pay
        self.bonus = bonus
    
    def get_pay(self):
        return self.base_pay + self.bonus    





