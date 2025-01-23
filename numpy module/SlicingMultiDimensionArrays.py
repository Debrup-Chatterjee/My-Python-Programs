import numpy as np
arr=np.reshape(np.arange(11,36,1),(5,5))
print("First element : ",arr[0][0])
print("Entire 2d array : \n",arr[:,:])#or just write arr2 instead of arr2[:,:]
print("Entrie second row : ",arr[1,:])#or just write arr2[1] instead of arr2[1,:]
print("Entire second column : ",arr[:,1])
print("Top left 2 rows and 3 columns : \n",arr[0:2,0:3])
print("Top right 2 rows and 3 columns : \n",arr[0:2,2:])
print("Alternate rows : \n",arr[0:5:2])
print("First 3 rows with alternate elements : \n",arr[0:3,::2])