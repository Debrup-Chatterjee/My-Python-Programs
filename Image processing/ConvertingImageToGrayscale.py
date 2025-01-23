from PIL import Image
image=Image.open("E:/My Python programs/Image processing/img.jpeg")
gray_img=image.convert("L")
gray_img.save("E:/My Python programs/Image processing/mygrayscale.jpeg")
gray_img.show()
