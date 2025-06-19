from abc import ABC,abstractmethod
class MyCal(ABC):
     @abstractmethod
     def add(self,a,b):
          pass
     @abstractmethod
     def subtract(self,a,b):
          pass
     @abstractmethod
     def multiply(self,a,b):
          pass
     @abstractmethod
     def divide(self,a,b):
          pass
class Calculator(MyCal):
     def add(self,a,b):
          return a+b
     def subtract(self,a,b):
          return a-b
     def multiply(self, a, b):
          return a*b
     def divide(self, a, b):
          if b==0:
               raise ValueError("Cannot divide by zero")
          return a/b
calcu=Calculator()
print(calcu.add(10,5))
print(calcu.subtract(15,5))
print(calcu.multiply(10,2))
print(calcu.divide(8,4))
'''A class with atleast one abstract method is called an Abstract Class.
A class where all methods are abstract methods is called an Interface.

Since abstract class and interface contain abstract methods whose implementation(or body) is later defined
in the sub classes,it is not possible to estimate the total memory required to create the object for the
abstract class or interface.So,PVM cannot create object to an abstract class or interface.
Once an abstract class or interface is written,we should create sub classes and all the abstract methods 
should be implemented (body should be written) in the sub classes.The,it is possible to create objects to
the sub classes.'''