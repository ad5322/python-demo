from pprint import pprint

class Htmldocument:
    
    def __init__(self,extension = 'HTML8',version = 5.0):
        self.ext = extension
        self.ver = version
        
    def content(self):
        return f'{self.ext} {self.ver} here is some content'
    
    @classmethod
    def anon(cls):
        return Htmldocument('javascript',10)
    
x = Htmldocument()
print(x.content())
anon = Htmldocument.anon()
print(anon.content())
