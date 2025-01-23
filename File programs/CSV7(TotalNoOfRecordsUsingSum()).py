import csv
with open("E:/My Python programs/File programs/test.csv","r") as fp:
     reader=csv.reader(fp)
     count=sum(1 for row in  reader)-1
     print(f"Total records: {count}")