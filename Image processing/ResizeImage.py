from PIL import Image
image=Image.open("E:/My Python programs/Image processing/img.jpeg") # Open an image file
image.show() # Display the original image
res_image=image.resize((300,200)) # Resize the image
res_image.show() # Display the resized image