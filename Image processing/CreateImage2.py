from PIL import Image,ImageDraw
img=Image.new("RGB",(400,400),"lightblue")# Create a blank light blue image
draw=ImageDraw.Draw(img)
circle=(100,100,300,300)
draw.ellipse(circle,outline="blue",width=6,fill="red")# Draw the circle
img.save("E:/My Python programs/Image processing/circleImg.jpg")
img.show()
