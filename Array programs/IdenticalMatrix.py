n=int(input("Enter dimension of the matrix: "))
arr=[]
print("Enter ",n*n," values in row major order: ")
for i in range(n):
     a=[]
     for j in range(n):
          x=int(input())
          a.append(x)
     arr.append(a)
for i in range(n):
     for j in range(n):
          print(arr[i][j],end=" ")
     print()
for i in range(n):
     for j in range(n):
          if(arr[i][j] != arr[j][i]):
               print("The matrix is not Identical")
               exit()
print("The matrix is Identical")