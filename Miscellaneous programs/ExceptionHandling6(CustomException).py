class small_number_error(Exception):
     def __init__(self,divisor,message="Divisor is small. It's greater than 2"):
          self.divisor=divisor
          self.message=message
          super().__init__(self.message) # calls constructor of super class Exception
try:
     num=30
     divisor=int(input("Enter a divisor: "))
     if divisor<=2:
          raise small_number_error(divisor) # raises the custom exception with divisor as the argument
     result=num/divisor
     print(f"Result: {result}")
except small_number_error as o: # gives an alias o to the custom exception
     print(f"Error: {o} (Divisor: {o.divisor})")