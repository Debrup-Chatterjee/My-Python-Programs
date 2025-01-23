import numpy as np
array=np.array([101,21,33,4,5,6,7,10,11])
even_numbers=array[array%2!=0]
print("Even Numbers: ",even_numbers)
masked_array=np.ma.masked_where(array>7,array)
print("Masked Array: ",masked_array)