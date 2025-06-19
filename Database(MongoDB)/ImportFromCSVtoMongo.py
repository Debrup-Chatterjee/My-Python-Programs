import pandas as pd
from pymongo import MongoClient
df=pd.read_csv("E:/My Python programs/Database(MongoDB)/student_data.csv") # load CSV into DataFrame
client=MongoClient("mongodb://localhost:27017/")
db=client["studentdetails"]
collection=db["mystud"]
data=df.to_dict(orient="records") # convert dataframe to dictionary and insert
collection.insert_many(data)
print("CSV data imported successfully into MongoDB......")
client.close()