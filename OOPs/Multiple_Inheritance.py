class Addition:
     def addition(self,a,b):
          return a+b
     def display(self):
          print("Addition display called")
class Subtract:
     def subtract(self,a,b):
          return a-b
     def display(self):
          print("Subtract display called")
class Calculation(Addition,Subtract):
     def division(self,a,b):
          Subtract().display()# Here we use class name instead of super() to specify which display() to be
          # called
          return a/b
     
calcu=Calculation()
x=int(input("Enter 1st number: "))
y=int(input("Enter 2nd number: "))
print(calcu.addition(x,y))
print(calcu.subtract(x,y))
print(calcu.division(x,y))
'''We use the class name here to call display instead of super(),if we use super() then the display() of 
the classes written in the brackets of base class will be called in left to right order.'''