file1="E:/My Python programs/File programs/test.txt"
file2="E:/My Python programs/File programs/abc.txt"
fr=open(file1,"r")
fw=open(file2,"a")
fw.writelines(fr)
fr.close()
fw.close()
print("1 file appended")