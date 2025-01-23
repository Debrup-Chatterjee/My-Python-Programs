from PIL import Image,ImageFilter
image=Image.open("E:/My Python programs/Image processing/img.jpeg")
res_image=image.resize((300,300))
res_image.show()
res_image.save("E:/My Python programs/Image processing/resizeimg.jpg")
blur_image=image.filter(ImageFilter.BLUR)
blur_image.save("E:/My Python programs/Image processing/newblur.jpg")
blur_image.show()