''' Python's argument passing model is neither pass bby value or pass by reference but it is pass by object
reference. Depending on the type of object you pass in the function, the function behaves differently. 
Immutable objects shhow pass by  value whereas mutable objects show pass by reference'''

# immutable objects like integers,floats,strings, and tuples are passed by value
def value_change(a):
     a=10 # this a is local to the function value_change
     print("Value inside function= ",a)
a=3
value_change(a)
print("Value outside function=",a)# here a is the global a(of main part)

# mutable objects like list,dictionaries are passed by reference
def list_change(l):
     for i in range(0,len(l)):
          l[i]=l[i]+1
     print("Inside Function: ",l)
l=[1,2,3,4,5]
list_change(l)
print("\nOutside Function: ",l)