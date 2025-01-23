import numpy as np
from PIL import Image
image=Image.open("E:/My Python programs/Image processing/img.jpeg")
image_array=np.array(image) # Convert to a numpy array
print("Image shape: ",image_array.shape)# There appears three values for rgb(color) images and two values 
# for grayscale(black and white) images