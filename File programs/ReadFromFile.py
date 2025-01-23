fo=open("E:/My Python programs/File programs/abc.txt","r")
str=fo.read(15)#reads 15 characters from the first
#str=fo.read()#reads all characters from the file
print("String read is:",str)
fo.close()
print("File ",fo.name," is closed.")