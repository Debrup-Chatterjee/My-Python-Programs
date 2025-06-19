'''Advantages of static method: 
1. No need to create an object to call the method
2. No need to write self or cls in parameter list
3. Works without using instance or class(cls) variables
4. Clearly indicates that is independent of instance or class variables
5. @classmethod can modify the class attributes using cls, but @staticmethod cannot modify the class 
variables using cls but it can do so by writing classname.classvariable
6. Using cls inside a static method will give error.'''
class number_prog:
     @staticmethod
     def factorial(n):
          if n==0:
               return 1
          return n*number_prog.factorial(n-1)
     @staticmethod
     def gcd(a,b):
          while b:
               a,b=b,a%b
          return a
print(number_prog.factorial(5))
print(number_prog.gcd(35,10))
