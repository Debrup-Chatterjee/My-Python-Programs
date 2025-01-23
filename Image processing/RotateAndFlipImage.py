from PIL import Image
img=Image.open("E:/My Python programs/Image processing/img.jpeg") # Open an image file
img.show() 
rotated_image=img.rotate(180) # Rotate 180 degrees
flipped_image=img.transpose(Image.FLIP_LEFT_RIGHT) # Flip horizontally
# Write Image.FLIP_TOP_BOTTOM to flip vertically
rotated_image.show()
flipped_image.show()
