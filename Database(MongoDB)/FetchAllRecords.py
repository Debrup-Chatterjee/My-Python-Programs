from pymongo import MongoClient
con=MongoClient('mongodb://localhost:27017/')
mydb=con["studentdetails"]
collection=mydb["mystud"]
mydata=collection.find() # fetch all documents from the collection
print("Print all data from the collection: ")
for doc in mydata:
     print(doc)