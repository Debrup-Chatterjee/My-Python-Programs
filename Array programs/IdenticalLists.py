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
if n1!=n2:
     exit("The two lists are not identical")

#Checking for identically in both the list
flag1=list(filter(lambda x: x not in l2,l1))
flag2=list(filter(lambda x: x not in l1,l2))
if len(flag1)==len(flag2)==0:
     print("The two lists are identical")
else:
     print("The two lists are not identical.The non identical elements are:\n",flag1+flag2)