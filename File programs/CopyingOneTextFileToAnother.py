file1="E:/My Python programs/File programs/test.txt"
file2="E:/My Python programs/File programs/abc.txt"
fr=open(file1,"r")
fw=open(file2,"w")
for line in fr.readlines():
     fw.write(line)
fr.close()
fw.close()
print("1 file copied")