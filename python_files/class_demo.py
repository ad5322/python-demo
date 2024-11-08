from pprint import pprint
import re

class Parser:
    phone_pattern = r'\d{3}-\d{3}-\d{4}'
    
    def __init__(self,text):
        self.text = text
        
    def email(self):
        match = re.search(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+',self.text)
        if match:
            return match.group(0)
        return None
    
    def phone(self):
        match = re.search(self.phone_pattern, self.text)
        if match:
            return match.group(0)
        return None
    
    def parse(self):
        return {
            'email':self.email(),
            'phone':self.phone()
        }

class UKparser(Parser):
    phone_pattern = r'(\+\d{1}-\d{3}-\d{3}-\d{4})'
 
        
if __name__ == '__main__':       
    s = 'Contact us via 408-205-5663 or email@gmail.com'
    parse = Parser(s)
    print(parse.parse())