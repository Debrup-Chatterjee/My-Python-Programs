from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client['student']
collection=db["student_details"]
sorted_marks=collection.find().sort({"st_marks":-1,"name":1}) #sorting marks on descending manner and people who get same marks their names will be sorted ascending
for doc in sorted_marks:
     print(doc)