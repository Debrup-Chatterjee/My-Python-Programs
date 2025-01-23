import numpy
arr=[]
a=int(input("size of array: "))
for i in range(a):
     arr.append(float(input("Elements: ")))
print(arr)
arr=numpy.array(arr)
print(arr)