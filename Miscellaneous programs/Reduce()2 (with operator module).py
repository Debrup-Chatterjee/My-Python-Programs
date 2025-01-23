from functools import reduce
import operator
arr1=[1,2,4,3,5,6]
arr2=["I","Love","CodeHub"]
s=reduce(operator.add,arr1)
product=reduce(operator.mul,arr1)
con_str1=reduce(operator.concat,arr2)
con_str2=reduce(operator.add,arr2)
print(f"Sum of all elements in arr1 : {s}\n")
print(f"Product of all elements in arr1 : {product}\n")
print(f"Concatenated string by using operator.concat : {con_str1}\n")
print(f"Concatenated string by using operator.add : {con_str2}\n")
print("Subtration of all elements in arr1 : ",reduce(operator.sub,arr1))