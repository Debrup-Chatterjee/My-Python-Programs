class MyClass:
     count=0 # class-level attribute
     @classmethod
     def counter(cls):
          cls.count +=1
          print(f"Count: {cls.count}")
MyClass.counter()
MyClass.counter()
MyClass.counter() 
ob=MyClass()
ob.counter()
'''Here we see that we can call the class method counter() both by classname.method() and also by
objectname.method() as the class attributes are shared by all instances of the class.'''
