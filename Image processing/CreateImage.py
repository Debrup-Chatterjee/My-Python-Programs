from PIL import Image,ImageDraw
width,height=450,350
image=Image.new("RGB",(width,height),"pink")#create a blank image(RGB mode) with pink background
draw=ImageDraw.Draw(image)
draw.rectangle((50,50,350,250),outline="green",width=7)
draw.text((120,135),"Welcome To CodeHub sodepur",align="center",fill="blue")
image.save("E:/My Python programs/Image processing/rectangleImg.png")
image.show()