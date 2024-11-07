class Point:
    asa = 0
    def __new__(cls,*args, **kwargs):
        cls.asa +=1
        return super().__new__(cls)
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        print(self.x,self.y)
        
        
        
pt = Point(1,4)
pt = Point(1,4)
pt = Point(1,4)
print(Point.asa)