'''Arguments/Parameters of a function  can be declared and passed in different ways in Python.This program 
demostrates this very concept''' 
def value_change(a):# here a is 'Required Argument',i.e.,you HAVE to give it
     a=10
     print("Value inside function= ",a)
     return
a=int(input("Enter a number: "))
value_change(a)#not giving a will result in error 
print("Value outside function= ",a)
print()

#demonstrating 'Keyword Arguments'
def studentinfo(rollno,name,course):
     print("Roll Number: ",rollno)
     print("Name: ",name)
     print("Course: ",course)
studentinfo(course="UG",rollno=50,name="Jack")# parameter can be in any order by this way
print()

#demonstrating 'Default Arguments'
def studentinfo(rollno,name,course="UG"):
     print("Roll Number: ",rollno)
     print("Name: ",name)
     print("Course: ",course)
studentinfo(course="UG",rollno=50,name="Jack")#works when course is passed
studentinfo(rollno=51,name="Tom")#works even when course is not passed in function call as course is a
#default argument which has the value "UG" mentioned in the function definition
studentinfo(course="PG",rollno=52,name="Jason")#here the value passed im function call takes precedence
#over the value written in function definition,thus there is overriding
print()

#demonstrating 'Variable-length Arguments'
def variablelengthfunction(*argument):#putting a * before argument allows us to pass variable length 
#arguments in a function by making argument a tuple.
     if(len(argument)==0):
          print("No arguments are passed...")
     else:
          print(len(argument)," arguments are passed,they are:")
          for i in argument: print(i)
variablelengthfunction(10)#can pass one value
variablelengthfunction(1,2,3,4,5)#can pass multiple values
variablelengthfunction(1,"hello",3.4)#can pass multiple heterogeneous values
variablelengthfunction()#can even pass no arguments
variablelengthfunction([33,24,57],{"a":1,"b":2,"c":3})#can pass different data type like list and 
#dictionary separately or even together