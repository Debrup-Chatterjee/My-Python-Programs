from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/")
db=client["studentdetails"]
collect=db["mystud"]
filter_crt={"age":{"$gt":20},"marks":{"$gt":99}}
rest=collect.find(filter_crt)
for res in rest:
     print(res)