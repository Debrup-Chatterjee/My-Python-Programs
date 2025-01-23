print("Hello World\n")
a=int(input("Enter value of a="))
b=int(input("Enter value of b="))
c=a+b
print ("Sum of a and b=",c)
print()

l1=[1,2,3.6,4,"hi"]
l2=[6,"wassup",8.9]
print("The list is: ",l1+l2,"\n")
print(l1[0:8])
print()

print("For loop(incremented by 2):")
for i in range(1,6,2):
     print(i)
print()

print("For loop(reverse):")
for i in range(5,0,-1):
     print(i)
print()

print("While loop:")
i=1
while i<=3:
     print(i)
     i+=1
