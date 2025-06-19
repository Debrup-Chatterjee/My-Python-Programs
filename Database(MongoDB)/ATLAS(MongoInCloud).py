from pymongo import MongoClient
from urllib.parse import quote_plus

# Since username and password might contain special characters like @,:,/,?,$,#,etc. therefore it is always safer to URL-encode the username and password
username= quote_plus("Debrup")
password = quote_plus("Debrup@31")  # Output will be 'Debrup%4031'

#Replace this with your actual connection string
conn_str=f"mongodb+srv://{username}:{password}@mycluster.zjhfjfe.mongodb.net/?retryWrites=true&w=majority&appName=MyCluster"

#Connect to MongoDB Atlas
client=MongoClient(conn_str)

#Select database and collection
db=client["student_details"]
collection=db["student"]

# Insert a document
st= {"Name":"Rupsa","Roll":2,"Marks":100}
collection.insert_one(st)
print("Student added successfully...")

# Find all students
print("All Students:")
for doc in collection.find():
     print(doc)