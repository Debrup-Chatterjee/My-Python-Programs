from pymongo import MongoClient
con=MongoClient('mongodb://localhost:27017/') # connect to the MongoDB server
mydb=con["studentdetails"] # create a new database or connects to an existing db with this name
collection=mydb["mystud"] # create a collection "mystud"
sdata={"name":"Soumya","age":21,"city":"Sodepur"}
collection.insert_one(sdata) # insert one record into the collection
print(f"collection '{"mystud"}' created successfully! ")