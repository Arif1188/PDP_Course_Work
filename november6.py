class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
    def area(self):
        return (self.width + self.height)/2
    
    def perimetr(self):
        return (self.width + self.height)* self.area()
    
    
rt = Rectangle(20,40)
print(rt.area())