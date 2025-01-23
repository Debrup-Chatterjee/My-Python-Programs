#Taking Input in list
l=[]
n=int(input("Enter the number of elements you want to enter: "))
print("Enter ",n," values in the list: ")
for i in range(n):
     x=int(input())
     l.append(x)
t=int(input("Enter the Target Sum: "))
#Finding pairs which add up to t
l2=list(set(l))
c=0
print(f"The pairs which add up to {t} are: ")
while(len(l2)>=1):
     if (t-l2[0]) in l2[1:]:
          c=c+1
          print(f"({l2[0]},{t-l2[0]}) ",end="")
          l2.remove(t-l2[0])
     l2.remove(l2[0])
if l.count(t/2)>1:
     c=c+1
     print(f"({int(t/2)},{int(t/2)})")
if(c==0):
     print("There are no such pairs found...")