fo=open("E:/My Python programs/File programs/output.txt","r")
lines=fo.readlines()
print("The total number of lines in the file are: ",len(lines))
fo.close()

fo=open("E:/My Python programs/File programs/output.txt","r")
print("The total number of words in the file are: ",len((fo.read()).split()))
fo.close()