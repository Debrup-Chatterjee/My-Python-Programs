#Taking input in two lists
n1=int(input("Enter the length of the first list: "))
l1=[]
print("Enter ",n1," numbers into the first list:")
for i in range(0,n1):
     x=int(input())
     l1.append(x)
n2=int(input("Enter the length of the second list: "))
l2=[]
print("Enter ",n2," numbers into the second list:")
for i in range(0,n2):
     x=int(input())
     l2.append(x)
#Finding common elements
s=set(l1) & set(l2) 
if(s==0):
     print("No common elements present in the list")
else:
     print("The common elements are: ",list(s))