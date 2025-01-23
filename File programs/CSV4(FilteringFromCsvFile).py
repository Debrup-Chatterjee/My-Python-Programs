import csv
with  open("E:/My Python programs/File programs/test.csv","r")as fp:
     rd=csv.DictReader(fp)
     #When creating DictReader object from csv.reader() object it automatically omits the first(header) row
     for row in rd:
          if int(row['Marks'])>95 and (row['Name'])[0]=='D':
               print(row)