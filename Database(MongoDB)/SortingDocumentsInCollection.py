from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client.student
collection=db.student_details
print("Sorted by marks(ascending): ")# sort by price in ascending order
for doc in collection.find().sort("st_marks",1):
     print(doc)
print("\nSorted by marks(descending): ")
for doc in collection.find().sort("st_marks",-1): # sort by price in descending order
     print(doc)