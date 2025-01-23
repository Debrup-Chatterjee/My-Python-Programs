import numpy as np
arr=np.array([4,0,9,1,6,8,2,3,7,5])
print("ORIGINAL ARRAY IS : ",arr)
arr.sort()
print("SORTED ARRAY IS : ",arr)
'''
A numpy array can be sorted using the sort() method of the NumPy module.The syntax of the sort()
function can be given as:
          numpy.sort(array,axis=-1,kind='quicksort',order=None)
Here,
"array" is the numpy array that has to be sorted.
"axis" is the axis along which the array will be sorted.Default value is -1,i.e.,the last axis.
"kind" specifies the type of sorting algorithm to be used.Values can be "mergesort","heapsort","stable"
and "quicksort".
"order" can be a single column name or list of clumn names along which sorting needs to be done.
'''