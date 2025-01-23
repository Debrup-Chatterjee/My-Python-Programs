#To work with matrices,numpy provides a special object called matrix.In numpy,a matrix is a specialized 2d 
#array that retains its 2d nature through operations.
import numpy as np
#Creating Matrix
arr1=np.matrix([[1,2,3],[4,5,6]])
a=np.array([[1,2,3],[4,5,6]])
arr2=np.matrix(a)
s="1 2 3; 4 5 6"
arr3=np.matrix(s)
#A matrix can be made from a list,2d array or a string with semicolons denoting end of each row

#Though 2d array and matrix might appear similar but they are different objects
print(type(a))
print(type(arr2))