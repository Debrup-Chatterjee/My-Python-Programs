import math
def prime(num,f):
     if f==int(math.sqrt(num)):
          return 0
     elif(num%f==0):
          return 1+prime(num,f-1)
     else:
          return prime(num,f-1)
n=int(input("Enter a number: "))
if n>1 and prime(n,n-1)==0:
     print("It is a Prime Number")
else:
     print("It is a Composite Number")