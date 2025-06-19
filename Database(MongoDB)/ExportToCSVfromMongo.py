import csv
from pymongo import MongoClient
client=MongoClient('mongodb://localhost:27017/')
db=client['studentdetails']
col=db['mystud']
data=list(col.find())

if data:
     all_keys=set() # collect all unique keys across all documents
     for doc in data:
          all_keys.update(doc.keys())
     keys=list(all_keys)

     with open('E:/My Python programs/Database(MongoDB)/myfile.csv','w',newline='') as newcsv:
          writer=csv.DictWriter(newcsv,fieldnames=keys)
          writer.writeheader()
          for row in data:
               # row['_id']=str(row['_id']) # convert object id to sring for CSV compatibility
               writer.writerow(row)
     
     print("Data exported to myfile.csv successfully.....")
else:
     print("No data found in collection.")