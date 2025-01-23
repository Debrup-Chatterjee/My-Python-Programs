"""The function which are called from the main part must be defined anywhere above the function call.(like
in this program SumOfTwo() )
Other functions which are called from other functions can be defined anywhere, up or down, doesn't matter.
(like in this program increase() )"""

def SumOfTwo(a,b):
     return increase(a)+increase(b)
x=int(input("Enter x= "))
y=int(input("Enter y= "))
s=SumOfTwo(x,y)
print("SUM= ",s)
def increase(n):
     return n+1




