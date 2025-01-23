#The reshape() function is useful to convert a 1d array or a list into a multidimensional(2d or 3d) array.
import numpy as np
arr=np.arange(1,13)
reshaped_arr=arr.reshape((3,4))
print("Orginal Array:\n",arr)
print("Reshaped Array:\n",reshaped_arr)
flattened=reshaped_arr.flatten()
print("Flattened Array:\n",flattened)

