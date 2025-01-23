import csv
file=open("E:/My Python programs/File programs/test.csv","r")
csvreader=csv.reader(file)#Creating reader object of csv module to read a csv file
arr=[]
arr=next(csvreader)#next() moves on to the next row
print(arr)
rows=[]
for row in csvreader:
     rows.append(row)
print(rows)
file.close()