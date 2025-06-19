'''When we create object of Child class then only Child class constructor is fired.To call Parent class
constructor too from Derived class, we write super().__init__()'''
class Parent:
     def __init__(self):
          print("Parent class Constructor fired")
     def display(self):
          print("Hello Parent")
     
class Child(Parent):
     def __init__(self):
          super().__init__() # Calling Parent class constrcutor
          print("Child class Constructor fired")
     def display(self):
          print("Hello Child")

obj=Child()
obj.display()