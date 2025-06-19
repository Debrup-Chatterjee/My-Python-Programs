'''Print the elements of a tuple which are uique numbers.
eg: Input: 1,121,233,45,66
    Output: 1,45 since 1 and 45 are unique numbers'''
t=[]
n=int(input("Enter how many numbers you want to enter: "))
for i in range(n):
     x=int(input())
     t.append(x)
t=tuple(t)
l=[v for v in t if len(set(str(v)))==len(str(v))]
if(len(l)==0):
     exit("No Unique numbers are found")
print("The unique numbers in the tuple are:",str(l).replace("[","").replace("]",""))