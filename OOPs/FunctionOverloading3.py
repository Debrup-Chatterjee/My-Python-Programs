class funOverload:
     def check(self,a=None,b=None):
          if a is not None and b is not None:
               print(f"Result: {a*b}")
          elif a is not None:
               c=a**2
               print(f"Result: {c}")
          else:
               print("No arguments present")
ob=funOverload()
ob.check(6)
ob.check(5,8)
ob.check()