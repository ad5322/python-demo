from pprint import pprint

class Item:
    def __init__(self,name,qty,price):
        self.name = name
        self.qty = qty
        self.price = price
        
    @property
    def amount(self):
        return self.price * self.qty
    
    def __str__(self):
        return f'{self.name} {self.qty} ${self.price} ${self.amount}'
    
class Cart:
    