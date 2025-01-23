#fo=open("abc.txt","w")#Open file in current directory
fo=open("E:/My Python programs/File programs/abc.txt","w")#Open file in a specified path
print("Name of the file: ",fo.name)
print("Closed or not: ",fo.closed)
print("Opening mode: ",fo.mode)
fo.close()#Closing opened file
print("Closed or not: ",fo.closed)

'''We can also use 'with open()' instead of 'open()',when using 'with open()' instead of 'open()' the 
difference is that we do not need to manually close the file which  we have to when using 'open()',it is
automatically closed'''
with open("E:/My Python programs/File programs/output.txt","w") as f:
     f.write("hello")
print("Closed or not: ",f.closed)