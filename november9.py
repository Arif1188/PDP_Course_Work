class Pearson:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name = name
    
    @name.deleter
    def name(self):
        del self.__name
        
ps = Pearson(3,4)
print(ps.name)
ps.name = "John"
print(ps.name)
del ps.name
print(ps.name)
#----------------------------
