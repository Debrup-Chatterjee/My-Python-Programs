from pymongo import MongoClient
client=MongoClient()
client=MongoClient('localhost',27017) # Connecting to MongoDB running locally on port 27017
print(client.list_database_names())# returns a list of all existing databases on your MongoDB server
db=client.newdb # connects to a database named newdb,creates the database if not present
pricelist=[{'ProdId':1,'Name':'Laptop','Price':25000},
           {'ProdId':2,'Name':'TV','Price':40000},
           {'ProdId':3,'Name':'Printer','Price':9500}]
db.products.insert_many(pricelist)# inserts all the product documents into a collection called products(created if not present) in the newdb database
