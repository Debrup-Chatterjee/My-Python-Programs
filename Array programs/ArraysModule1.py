import array
a=array.array('i',[5,6,-7,8])#here 'i' represents signed integer
#also,here the first "array" respresents the array module and the second "array" represents the array class in it
print("The array elements are : ")
for element in a:
     print(element)
a=array.array('u',['a','b','c','d','e'])#here 'u' represents unicode characters
print("\nThe array elements are : ")
for ch in a:
     print(ch)

#Creating one array from another array
arr1=array.array('d',[1.5,2.5,-3.5,4])
arr2=array.array(arr1.typecode,(a*3 for a in arr1))
#here, arr1.typecode gives the type code character of the array 'arr1'
print("\nThe arr2 elements are : ")
for i in arr2:
     print(i)

#Indexing,Negative indexing and Slicing are also possible with arrays just like with lists
print(f"\n {a[0]}")
print(f"{a[-1]}")
print(f"{a[2:5]}")#while slicing,you will notice that the printing output format is different than that from lists
print(f"{a[-5::2]}")

#Creating an empty array
x=array.array('i',[])
print("\n",x)

#We cannot create Multi-dimensional arrays using array class of array module...
#However we can use array class of numpy to create multi-dimensional arrays.

#As you can see the below code gives runtime error when we try to create a matrix using array module
x=array.array('i',[[50,60,70,66,72],[60,62,71,56,70],[55,59,80,68,65]])
print(x)