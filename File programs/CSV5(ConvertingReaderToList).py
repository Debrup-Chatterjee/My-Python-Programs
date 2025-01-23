import csv
with open("E:/My Python programs/File programs/test.csv","r") as file:
     reader=list(csv.reader(file))#Convert the reader to a list
     header=reader[0]
     print("Header: ",header)
     print("Last 3 records: ")
     for row in reader[-3:]: #Slice the last 3 rows
          print(row)