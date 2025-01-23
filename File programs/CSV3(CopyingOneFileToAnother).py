import csv
file1=open("E:/My Python programs/File programs/test.csv","r")
file2=open("E:/My Python programs/File programs/output.csv","w",newline="")
#newline parameter removes the default blank row inserted between eacch row while witing to a csv file,not
# giving this enters a balnk row between each row
r=csv.reader(file1)
w=csv.writer(file2)
for row in r:
     w.writerow(row)
print("File Copied Successfully")
file1.close()
file2.close()