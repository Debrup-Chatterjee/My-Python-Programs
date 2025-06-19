from abc import ABC,abstractmethod
class MyClass(ABC):
     @abstractmethod
     def calculate(self,x):
          pass
#this is sub class of MyClass
class Sub1(MyClass):
     def calculate(self,x):
          print('Square Value: ',x*x)
#this is another sub class for MyClass
import math
class Sub2(MyClass):
     def calculate(self,x):
          print('Square root= ',math.sqrt(x))
#third sub class for MyClass
class Sub3(MyClass):
     def calculate(self,x):
          print('Cube value= ',x**3)
#creating Sub1 clas object and call calculate() method
obj1=Sub1()
obj1.calculate(16)
#creating Sub2 class object and call calculate() method
obj2=Sub2()
obj2.calculate(16)
#creating Sub3 class object and call calculate() method
obj3=Sub3()
obj3.calculate(16)
'''Since all abstract classes should be derived from the meta class ABC which belongs to abc(abstract base
class) module,we should import this module into our program.A meta class is a class that defines the 
behavior of other classes.The meta class ABC defines that the class which is derived from it becomes an
abstract class.
In this program, MyClass is an abstract class since it is derived from ABC meta class.This class has an
abstract method calculate() that does not contain any code.We used @abstractmethod decorator to specify
that this is an abstract method.We have to write sub classes where this abstract method is written with 
its body(or implementation).Since the same abstract method is implemented differently for different objects,
they can perform different tasks.'''