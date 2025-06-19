from abc import ABC,abstractmethod
class Adder(ABC): #Abstract method
     @abstractmethod
     def addition(self,a,b):
          pass
class Divider(ABC): #Abstract class Divider
     @abstractmethod
     def division(self,a,b):
          return a//b
class Calculator(Adder,Divider): #Calculator class implementing both abstract classes
     def addition(self,a,b):
          return a+b
     def division(self, a, b):
          return a/b
calc=Calculator()
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
print(f"{a} + {b} = {calc.addition(a,b)}")
print(f"{a} / {b} = {calc.division(a,b)}")
'''In this program,we can see that the division() method inside Divider abstract class is marked with a
@abstractmethod decorator but still has a body.This can be done that is we can write an abstract method 
with a body,however this body will be diregarded,i.e.,we still need to define division() method in one
of the sub classes of Divider class.In this program, the return a//b is disregarded and the new definition
of division return a/b inside Calculator subclass is considered.
Note that we can create an object of a class only if all the abstract methods of its parent abstract
classes have been defined.'''