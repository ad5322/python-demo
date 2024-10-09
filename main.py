from pprint import pprint
from abc import ABC


class Point2D:
    __slots__ = ('x','y')
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'Piont2D {self.x} {self.y}'
    
    
class Point3D(Point2D):
    __slots__ = ('z',)
    def __init__(self, x,y,z):
        super().__init__(x, y)
        self.z = z
        
if __name__ == '__main__':
    point = Point3D(1,2,3)
    pprint(point.__slots__)
    

