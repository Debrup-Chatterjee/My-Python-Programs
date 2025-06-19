l=[]
n=int(input("Enter how many numbers you want to enter: "))
if(n<=0):
     exit("Invalid choice of input...please enter a positive natural number !")
print(f"Enter {n} numbers into the list: ")
for i in range(0,n):
     x=int(input())
     l.append(x)
k=int(input("Enter the rotation position: "))
if(k<0 or k>=len(l)):
     exit("Invalid rotation position entered!")
print("The list before rotation is: ",l)
print("The list after rotation is: ",l[k+1:]+l[0:k+1])