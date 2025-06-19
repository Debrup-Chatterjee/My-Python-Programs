from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/")
db=client["studentdetails"]
stud_collection=db["stud"]
mystud_collection=db["mystud"]

stud=list(stud_collection.find())
mystud=list(mystud_collection.find())
results=[]
for std in stud:
     for mstd in mystud:
          if std.get("name") == mstd.get("name"): # compare two collection depeding on common fields
               combined_record={**std,**mstd} # merges all key-value pairs from both std and mstd
               results.append(combined_record)

for result in results:
     print(result)