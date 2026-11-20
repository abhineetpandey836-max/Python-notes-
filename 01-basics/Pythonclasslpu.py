# classes are also like combination of data members but in OOPs in security encapsulate technique we need two methods--setters and getters method
class encapsulate:
    def setter(self, a,b,c): #def _init_(self, a, b, c):
        self.a=a # public
        self._b=b # protected
        self.__c=c # private
    
    def geta(self):
        return self.a
    
    def getb(self):
        return self._b
    
    def setc(self, newc):
        self.__c=newc
    def getc(self):
        return self.__c
class deriv(encapsulate):
    pass
# why we use setter if we can use _init_ why we use setter here because setter can be called multiple times to overwrite and update the values of a, _b, and __c without needing to destroy and recreate the object
# create an empty object first (obj = deriv()) and then provide the data later in your code whenever it becomes available (obj.setter(10, 20, 30))
obj=deriv()
obj.setter(10,20,30)
print(obj.a, obj._b)
print(obj.getc())

# obj=encapsulate()
# obj.setter(10,20,30)
# print(obj.a, obj._b)
# print(obj.getc())


# Public ----> Anywhere, any method we can access
# Protected ---> Base class and derived class
# Private ---> Own Class

# There is two types of classes- Abstract classes and concrete class
# Abstract- Cannot be instantiated directly. It serves as a base template and can include both unimplemented (abstract) methods and implemented (concrete) methods.
# Concrete-  Can be instantiated directly to create objects. Every method it declares or inherits has a complete implementation.
# in abstract we use enforcement in class to initiate the method

# Abstract method
from abc import ABC, abstractmethod

class a(ABC):
    def m(self):
        pass
    
    @abstractmethod
    def m2(self):
        pass
    
    @abstractmethod
    def m3(self):
        pass
    
class b(a):
    def m2(self):
        print("abstract method")
    
    def m3(self):
        print("abstract method 2")
    
class c(a):
    def m2(self):
        print("c class method 1")
    def m3(self):
        print("c class method 2")
        
obj=b()
obj.m2()
obj.m()
obj.m3()

obj2=c()
obj2.m2()
obj2.m()
obj.m3()
    # in abstract class
    # --> it contains both concrete and abstract methods
    # --> should not implement Abstract method
    # --> should not create object for Abstract class