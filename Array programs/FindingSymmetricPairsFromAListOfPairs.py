'''Find the Symmetric pairs from a list of pairs.
input: [1,2],[2,1],[3,4],[4,5],[5,4],[7,8],[1,9]
output: [2,1],[5,4]'''
l=[]
c=0
n=int(input("Enter how many pairs you want to enter: "))
print("Enter ",n," pairs: ")
for i in range(0,n):
     e1=int(input("Enter element 1: "))
     e2=int(input("Enter element 2: "))
     l.append([e1,e2])
print("The list is: ",l)

print("The Symmetric pairs are: ")
for i in range(0,n-1):
     if l[i][::-1] in l:
          print(l[i][::-1])
          c+=1
if c==0:
     print("No Symmetric pairs are present.")