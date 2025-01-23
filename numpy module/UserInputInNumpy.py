import numpy as np
user_input=input("Enter numbers separated by spaces: ")
numbers=list(map(float,user_input.split()))#Convert input string to a list of numbers
array=np.array(numbers)
print("Numpy Array: ",array)