from pymongo import MongoClient
con=MongoClient("localhost",27017)
db=con["studentdetails"]
col=db["mystud"]

students=col.aggregate([{'$group':{'_id':'$age','total_marks':{'$sum':'$marks'}}}])
for doc in list(students):
     print(f"Total sum of marks of students aged {doc['_id']} is {doc['total_marks']}")