import numpy as np
#Creating 2D arrays
arr1=np.array([np.arange(1,4),np.arange(4,7)])
print("Original matrix is ",arr1)

#Transpose of a 2D array
print("\nTranspose is ",arr1.T)#we can also use arr1.transpose() instead of arr1.T

#Sum and Subtraction of two 2d arrays
arr2=np.array([np.arange(5,8),np.arange(8,11)])
print("\nMatrix 1: ",arr1)
print("Matrix 2: ",arr2)
print("Sum of two matrices: ",arr1+arr2)
print("Subtraction of two matrices: ",arr1-arr2)

#Product of two 2d arrays
print("\nMatrix 1: ",arr1)
print("Matrix 2: ",arr2)
arr2=np.array([[7,8],[9,1],[2,3]])
print("Product of two matrices: \n",np.dot(arr1,arr2))
