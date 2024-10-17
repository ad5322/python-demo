from pprint import pprint

class TempratureConverter:
    KELVIN = '*K'
    
    @staticmethod
    def celsius_to_kelvin(c):
        return c + 273.15
    
    @staticmethod
    def format(value,unit):
        symbol = ''
        if unit == TempratureConverter.KELVIN:
            symbol = 'Ak5322'
        return f'{value} {symbol}'
    
c = TempratureConverter.celsius_to_kelvin(37)
print(TempratureConverter.format(c,TempratureConverter.KELVIN))