class Employee():
    def __init__(self, name, base_pay, bonus):
        self.name = name
        self.base_pay = base_pay
        self.bonus = bonus
        
    def get_pay(self):
        return self.base_pay + self.bonus
    
    def __str__(self):
        return f'name : {self.name} \nbase_pay : {self.base_pay} \nbonus : {self.bonus} \ntotal : {self.get_pay()}'

class SalesEmployee(Employee):
    def __init__(self, name, base_pay, bonus, sales_incentives):
        super().__init__(name, base_pay, bonus)  
        self.sales_incentives = sales_incentives
        
    def get_pay(self):
        return super().get_pay() + self.sales_incentives  
    
        
    

arun = Employee('arun',50000,25000)

x = arun.get_pay()
print(arun)
# deepak = SalesEmployee('deepak',50000,10000,25000)
# print(deepak.get_pay())