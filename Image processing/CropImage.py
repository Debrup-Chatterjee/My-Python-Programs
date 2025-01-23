from PIL import Image
img=Image.open("E:/My Python programs/Image processing/img.jpeg") # Open an image file
img.show()
box=(150,150,350,350) # (left, upper, right, lower)
'''The origin(0,0) is at top left corner of the image.The first two are start cropping pixels,and last two 
are end cropping pixels.For example,here the origin is at top left corner and then crop 150 pixels from 
left to right...and then crop 150 pixels from up to down...and stop cropping at 350 pixels in the right and
in the bottom'''
crop_img= img.crop(box)
crop_img.show()