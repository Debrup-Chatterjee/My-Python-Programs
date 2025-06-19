# Demonstrating function overloading using variable length arguments
# *args collects all extra arguments into a tuple.Works even if zero or manyy arguments are passed.
def addition(*args):
     tot=0
     for num in args:
          tot+=num
     return tot
print(addition(2,3,5))
print(addition(3,2,4,5,6,7))

#**kwargs allows a function to accept any number of keyword arguments.These arguments are stored as a dict
def describe(**kwarg):
     for  key,value in kwarg.items():
          print(f"{key}:{value}")
describe(name="Poulami",age=21,city="Japan")
'''This wont work as we are passing a dictionary and not keyword arguments.**kwarg stores keyword arguments
as a dictionary but does not take a dictionary directly as input as given below.

d={'name':"Poulami",'age':21,'city':"Japan"}
describe(d)'''

# More example of **kwarg
def Disp_Info(**kwas):
     for key,val in kwas.items():
          print(f"{key}: {val}")
Disp_Info(name="Arpan",age=23,marks=87)
Disp_Info(name="Hari",Age=24)