n=int(input("Enter the dimension of the matrix: "))
arr=[]
lsum=0 #to store left diagonal sum
rsum=0 #to store right diagonal sum
bsum=0 #to store boundary sum
nbsum=0 #to store non boundary sum
print("Enter ",n*n," values in row major order: ")
for i in range(n):
     a=[]
     for j in range(n):
          x=int(input())
          a.append(x)
     arr.append(a)
print("\nThe matrix is: ")
for i in range(n):
     if(i==0 or i==n-1):
          bsum+=sum(arr[i])
     else:
          bsum+=arr[i][0]+arr[i][n-1]
     if(i!=0 and i!=n-1):
          nbsum+=sum(arr[i])-(arr[i][0]+arr[i][n-1])
     lsum+=arr[i][i]
     rsum+=arr[i][n-i-1]
     print(arr[i])
print("\nBoundary Sum = ",bsum)
print("Non Boundary Sum = ",nbsum)
print("Left Diagonal Sum = ",lsum)
print("Right Diagonal Sum = ",rsum)