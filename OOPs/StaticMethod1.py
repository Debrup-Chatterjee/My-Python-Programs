'''We need static methods when the processing is at the class level but we need not involve the class or
instances.Static methods are used when some processing is related to the class but does not need the class
or its instances to perform any work.For example, setting environmental variables,counting the number of
instances of the class or changing an attribute in another class,etc. are the tasks related to a class.Such 
tasks are handled by static methods.Also, static methods can be used to accept some values,process them
and return the result.In this case the involvement of neither the class nor the objects is needed.Static
methods are written with a decorator @staticmethod above them.Static methods are called in the form of
classname.method().In this program,we are creating a static method noObjects() that counts the number of
objects or instances created to MyClass.In MyClass,we have written a constructor that increments the class
varibale 'n' every time an instance is created.The incremented value of 'n' is displayed by the noObjects()
method. '''
class MyClass:
     #this is class var or static var
     n=0
     #constructor that increments n when an instance is created
     def __init__(self):
          MyClass.n=MyClass.n+1 
          '''A class variable can be accessed inside a instance method or constructor
          like this but we cannot access an instance variable inside a class method or static method'''
          
     #this is a static method to display the no. of instances
     @staticmethod
     def noObjects():
          print("No. of instances created: ",MyClass.n)
#Creating 3 instances
obj1=MyClass()
obj2=MyClass()
obj3=MyClass()
MyClass.noObjects()