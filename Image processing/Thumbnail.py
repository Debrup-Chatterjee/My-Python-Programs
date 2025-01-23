from PIL import Image
image=Image.open("E:/My Python programs/Image processing/img.jpeg")
image.thumbnail((50,50))
#The difference between resize() and thumbnail() is simply that in case of resize we need to store it in 
# another object, and in case of thumbnail the original object is itself changed
image.save("E:/My Python programs/Image processing/mythumbnail.jpg")
image.show()