import numpy as np
arr=np.array([10,20,30,40,50])#the array class under numpy doesn't require the type code unlike array class of array module
print(arr)#The printing output format is also different from that of array class of array module

'''Not having the type code might suggest that we can give heterogeneous elements..however you will notice
that changing data type of a single element implicitly changes the data type of all the elements.For 
example,if you change one of the elements to string type then in the ouput all the elements implicitly 
become strings.Therefore,even without the type code,array is not heterogeneous but homogeneous'''

#Creating Multi-dimensional arrays
arr=np.array([[1,2,3],[4,5,6]])
print(f"\n{arr}")

#User input using numpy array
arr=[]
size=int(input("\nEnter size of array: "))
print(f"Enter {size} floating point elements in the array :")
for i in range(size):
     arr.append(float(input()))
arr=np.array(arr)
print(np.floor(arr))#the floor method of numpy performs floor operation on all the elements of the array

#Creating a 2d array using arange() function
arr=np.array([np.arange(0,5),np.arange(5,10),np.arange(10,15)])
#arange() can generate sequence of numbers given the start and end
print(f"\n{arr}")

#Creating arrays using zeroes() and ones()
print("\n",np.zeros((3,4)))#creates a matrix of 3 rows and 4 columns of floating point zeros
print(np.ones((2,2),dtype=(np.int16)))#creates a matrix of 2 rows and 2 columns of ones
'''here the ones should be floating point,but instead they are integer type as we mention the date type
by using the second parameter 'dtype' of ones() function'''