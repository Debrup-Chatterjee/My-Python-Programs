def Shift(l):
     for i in range(len(l)):
          if l[i]==0:
               l.pop(i)
               l.insert(0,0)
n=int(input("How many numbers you want to enter? "))
l=[]
for i in range(n):
     x=int(input())
     l.append(x)
print("Input list: ",l)
Shift(l)
print("Output list: ",l)