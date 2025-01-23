#Taking Input in list
l=[]
n=int(input("Enter the number of elements you want to enter:"))
print("Enter ",n," values in the list:")
for i in range(n):
     x=int(input())
     l.append(x)
#Finding pairs which add up to 0
l2=list(set(l))
c=0
print("The pairs which add up to 0 are: ")
while(len(l2)!=0):
     if -l2[0] in l2:
          c=c+1
          print("(",l2[0],",",-l2[0],") ",end="")
          l2.remove(-l2[0])
     l2.remove(l2[0])
if(c==0):
     print("There are no such pairs found...")