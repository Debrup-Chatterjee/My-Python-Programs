import csv
with open("E:/My Python programs/File programs/test.csv","r") as file:
     reader=csv.reader(file)
     header=next(reader) #Skip the header row
     print("Header: ",header)
     for i,row in enumerate(reader):
          if i<2:
               print(row)
          else:
               break