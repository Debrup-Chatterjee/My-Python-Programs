r=int(input("Enter the number of rows: "))
c=int(input("Enter the number of columns: "))
arr=[]
print("Enter the values in row major order: ")
for i in range(r):
     a=[]
     for j in range(c):
          x=int(input())
          a.append(x)
     arr.append(a)
print("Original Matrix: ")
for i in range(r):
     for j in range(c):
          print(arr[i][j],end=" ")
     print()
#Finding tranpose of the user given matrix
arr2=[]
for j in range(c):
     a=[]
     for i in range(r):
          a.append(arr[i][j])
     arr2.append(a)
print("Transpose :")
for i in range(c):
     for j in range(r):
          print(arr2[i][j],end=" ")
     print()
