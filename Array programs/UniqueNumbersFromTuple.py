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