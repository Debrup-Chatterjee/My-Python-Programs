from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/")
db=client["studentdetails"]
collection=db["stud"]
sample_document=collection.find_one() # Fetch a sample document
if sample_document:
     print("Sample Document Structure:")
     for key in sample_document:
          print(f"{key}: {type(sample_document[key])}")
else:
     print("No documents found in the collection.")