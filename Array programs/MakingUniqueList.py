l=[]
n=int(input("Enter how many numbers you want to enter: "))
if(n<=0):
     exit("Invalid choice of input...please enter a positive natural number !")
print(f"Enter {n} numbers into the list: ")
for i in range(0,n):
     x=int(input())
     l.append(x)
# Making unique list
'''x=list(set(l))
print("The unique list is: ",sorted(x,key=l.index))
'''
x=list(dict.fromkeys(l))# returns the unique elements as keys of a dictionary
print("The unique list is: ",x)