import numpy as np
arr=np.matrix([[1,3,2],[7,5,4],[6,9,8]])
print("Original matrix : ",arr)

#Getting diagonal elements
d=np.diagonal(arr)#we can also use np.trace() instead of np.diagonal()
print("Left diagonal elements : ",d)
print("Right diagonal elements : ",np.diagonal(arr[::-1]))#elements are in reverse order though9down to up)

#Max and min elements
print("Max element is : ",arr.max())
print("Min elements is : ",arr.min())

#Sum and average of elements
print("Sum : ",arr.sum())
print("Average : ",arr.mean())

#Products of elements
print("Product of all elements in each row : \n",arr.prod(1))# 1 represents row
print("Product of all elements in each column : \n",arr.prod(0))# 0 represents column

#Sorting matrix row wise and column wise
print("Sorted row wise : \n",np.sort(arr))
print("Sorted column wise : \n",np.sort(arr,axis=0))

#Transpose of a matrix
print("Transpose : \n",arr.transpose())#We can also use arr.T() or arr.getT() instead of arr.transpose()

#Sum,Subtraction,Division and Multiplication of matrices
arr2=np.matrix([[1,3,5],[0,1,2],[6,4,1]])
print("\nMatrix 1: \n",arr)
print("Matrix 2: \n",arr2)
print("Sum of two matrices :\n",arr+arr2)
print("Subtraction of two matrices :\n",arr-arr2)
print("Multiplication of matrix 1 by a contant :\n",arr*2)
print("Division of matrix 1 by a contant :\n",arr/2)
print("Matrix multiplication of matrix 1 and matrix 2 :\n",arr*arr2)