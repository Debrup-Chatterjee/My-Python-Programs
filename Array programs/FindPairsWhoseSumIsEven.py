from itertools import combinations
# Taking input
n=int(input("Enter length of the array: "))
print("Enter ",n," elements into the array: ")
l=[]
for i in range(0,n):
     x=int(input())
     l.append(x)

odds=list(filter(lambda x: x%2!=0,l))# Finding all odd numbers
evens=list(filter(lambda x: x%2==0,l))# Finding all even numbers
EvenSumPairs=list(combinations(odds,2))+list(combinations(evens,2)) # Finding all even sum pairs
EvenSumPairs=list(dict.fromkeys(EvenSumPairs))
if len(EvenSumPairs)==0:
     print("No pairs found whose sum is even")
else:
     print("The pair of elements which have an even sum is: ",EvenSumPairs)