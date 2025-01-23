class class_method:
     count=0 # class-level attribute
     @classmethod
     def counter(cls):
          cls.count +=1
          print(f"Count: {cls.count}")
class_method.counter()
class_method.counter()
class_method.counter()