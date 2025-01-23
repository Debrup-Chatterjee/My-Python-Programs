#Taking user input in list
l=[]
n=int(input("Enter size of the list: "))
print("Enter ",n," values into the list...")
for i in range(n):
     a=int(input())
     l.append(a)
#searching without loop
k=int(input("Enter value to be searched: "))
if k in l:
     print("Value Found")
else:
     print("Value not found")
#slicing to print last three values in the list
print("The last three values in the list are: ")
print(l[len(l)-3:])
print("Same thing in reverse: ")
print(l[-1:-4:-1])
print(l[0:5:2])