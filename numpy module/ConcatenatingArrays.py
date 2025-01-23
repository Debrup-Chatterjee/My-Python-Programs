import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6]])
concat=np.concatenate((a,b),axis=0)
print("Concatenated Array:\n",concat)