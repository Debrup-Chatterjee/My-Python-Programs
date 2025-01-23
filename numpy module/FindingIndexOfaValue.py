import numpy as np
arr=np.array([1,15,15,12,67,15,78,98])
print("The Array is: ",arr)
index=np.where(arr==15)
# np.where(arr==15) returns a tuple which has a ndarray inside it containing all the index where the value
# in arr is 15 ,i.e.,index[0][0] will represent the index of first occurence of 15 in the array, and
# index[0] will be the ndarray containing all the index.
print("The index of value 15 is: ",index[0][0])