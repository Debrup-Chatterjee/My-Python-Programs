from pymongo import MongoClient
client=MongoClient('mongodb://localhost:27017/')
db=client['studentdetails']
coll1=db['mystud']
coll2=db['stud']

print("Sample records froms studinfo:")
for rec in coll1.find().limit(5):
     print(rec)

print("Sample records from stud:")
for rec in coll2.find().limit(5):
     print(rec)

last_threeRec=list(coll1.find().sort('_id',-1).limit(3)) # shows last three records
# here we sort on '_id' as _id stores the timestamp, therefor sorting in descending order based on _id gives us the last three inserted records
print("Last 3 records from mystud...")
for record in last_threeRec:
     print(record)

client.close()