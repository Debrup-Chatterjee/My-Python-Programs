'''Class variables also known as Static variables are not unique to each instance of a class ,i.e., they
are unique to the class and are shared by every instance of a class.Class variables can be accessed both
by an object of the class or directly by the class name since all instances of a class share the same
class variable.The Change done to the state of an class variable through a specific object can also be 
seen by accessing the class variable through other objects of the same class.
Class or static variables are always created and initialized outside all functions in a class at the 
beginning, and for every method in the class which requires access to the class variables,the function 
should have "cls" as parameter and have the @classmethod decorator above it.The methods which access the 
class variables of a class using cls are called class methods. '''
class Sample:
     x=10 
     # class/static varibles are always created and initialized outside all functions at the beginning 
     # inside a class
     @classmethod
     def modify(cls):# this is a class method
          cls.x+=1
# Creating 2 instances of Sample class
s1=Sample()
s2=Sample()
print("The class variable value is ",Sample.x)# We can access x directly by using the class name also
print("Before change: ")
print('x in s1= ',s1.x)
print('x in s2= ',s2.x)
print("After change: ")
s1.modify()# changing the value of x through one instance changes the value of x in other instances too
print('x in s1= ',s1.x)
print('x in s2= ',s2.x)