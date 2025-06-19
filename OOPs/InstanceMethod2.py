class Hello:
     def fun(self):
          print("Hello World")
ob=Hello()
ob.fun()
'''When no constructor is written, a default constructor is given implicitly.
Note that fun() does not access any instance variables but then also we have to write self otherwise we
would get error.'''