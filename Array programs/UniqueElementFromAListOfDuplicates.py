'''Find the unique element(s) from a list where all other elements occur twice,i.e.,find the elements which
occur only once.
Constraints: cannot use set'''
from collections import Counter
#Taking input
n=int(input("Enter how many numbers you want to enter: "))
l=[]
print("Enter ",n," numbers into the list: ")
for i in range(0,n):
     x=int(input())
     l.append(x)
#Finding unique elements
c=0
print("The unique characters are: ")
d=dict(Counter(l))
f=list(filter(lambda x: d[x]==1,d.keys()))
if len(f)==0:
     print("No unique characters present.")
else:
     print(f)