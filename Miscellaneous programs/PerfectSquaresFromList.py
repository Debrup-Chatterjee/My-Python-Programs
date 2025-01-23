import math
size=int(input("Enter how many numbers you want to enter: "))
l=[]
print(f"Enter {size} numbers into the list: ")
for i in range(size):
     x=int(input())
     l.append(x)

ps=list(filter(lambda x:x>=0 and math.sqrt(x)==math.ceil(math.sqrt(x)),l))
print("The perfect square numbers in the list are: ",ps)