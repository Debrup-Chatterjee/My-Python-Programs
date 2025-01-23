#Taking Input in list
l=[]
n=int(input("Enter the number of elements you want to enter:"))
print("Enter ",n," values in the list:")
for i in range(n):
     x=int(input())
     l.append(x)
#Finding elements which are not unique
d={num:l.count(num) for num in set(l)}
dup_keys=[key for key,value in d.items() if value!=1]
if(len(dup_keys)==0):
     print("There are no duplicate elements in the list")
else:
     print("The elements which appear more than once in the list are:")
     print(str(dup_keys).replace('[','').replace(']','') )
#Finding the second largest element in the list
s=set(l)
s.remove(max(s))
print("The second largest element in the list is: ",max(s))

