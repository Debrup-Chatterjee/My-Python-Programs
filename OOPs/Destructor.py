'''Garbage Collection(GC) is possible in Python.Python has an automatic garabage collector that manages
memory by deallocating objects that are no longer needed.
If we do not provide a destructor then a destructor is provided implicitly.If we write destructor 
explicitly, then that destructor is used to destory all objects of that class.
Destruction in python does not follow a strict LIFO mechanism like in C++.Destruction of objects occur when
obejcts go out of scope.'''
class Test:
     def __init__(self,name):
          self.name=name
          print(f"Object {self.name} is created")

     def __del__(self): # Destructor
          print(f"Object {self.name} is detroyed")
ob=Test("Arpan")
ob1=Test("Debrup")
del ob1 # calling destructor to destroy ob1 explicitly
print("End.....")
# destructor called to destroy ob explicitly as soon as ob goes out of scope