n=int(input("Enter number of values you want to enter(atleast 3): "))
if(n<=2):
     exit("Invalid Input! Number of values must be atleast 3")
l=[]
print("Enter ",n," values in the list: ")
for i in range(n):
     x=int(input())
     l.append(x)
for i in range(1,n-1):
     if(sum(l[0:i])==sum(l[i+1:])):
          print("Index Found! The index is: ",i)
          exit()
print("No such index found with required criteria")