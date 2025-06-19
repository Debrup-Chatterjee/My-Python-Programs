'''Instance variables are unique to each instance of a class ,i.e., a fresh copy of the instance variables
is generated everytime an instance of the class is created.Changing or modifying the state of an instance
variable of a specific object does not affect the instance variables of other objects of the same class.
Instance variables are always created and initialized using a constructor and for every method in the class
which requires access to the instance variables,the function should have "self" as parameter.The methods
which access the instance variables of a class using self are called instance methods. '''
class Sample:
     def __init__(self):
          self.x=10 # Instance variables are always created and initialized inside the constructor.
     
     def modify(self): # this is an instance method
          self.x+=1
#Creating 2 instances/objects of Sample class
s1=Sample()
s2=Sample()
print("Before Change: ")
print('x in s1= ',s1.x)
print('x in s2= ',s2.x)
s1.modify()# Modifying x of s1 does not affect the x of s2
print("\nAfter change: ")
print('x in s1= ',s1.x)
print('x in s2= ',s2.x)