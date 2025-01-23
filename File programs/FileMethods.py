fo=open("E:/My Python programs/File programs/output.txt","w")
seq=["First Line\n","Second Line\n","Third line\n","Fourth line\n","Fifth line\n"]
fo.writelines(seq)
fo.close()

fo=open("E:/My Python programs/File programs/output.txt","r+")
line=fo.readline()#reads one line from the first
print("First Line:",line)
line=fo.readline()
print("Next Line:",line)

fo=open("E:/My Python programs/File programs/output.txt","r+")
lines=fo.readlines()#reads all lines until EOF and returns a list ..containing all the lines. There is an 
# optional parameter [sizeint],if it is present then instead of reading till EOF,whole lines approximate to
# sizeint bytes are read.
print("All lines in the file:",lines)
fo.close()
print("File closed.\n")
