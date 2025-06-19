import pandas as pd
import pymongo
df=pd.read_excel("E:/My Python programs/Database(MongoDB)/Student.xlsx") # read data from Excel
data=df.to_dict(orient='records') # converts DataFrame to a list of dictionaries
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=client["studentdetails"]
col=mydb["mystud"]
col.insert_many(data) # insert data into MongoDB collection
print("Data imported successfully from excel to mongo...")