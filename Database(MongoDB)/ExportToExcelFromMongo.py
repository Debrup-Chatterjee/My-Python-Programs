import pymongo
import pandas as pd
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=client["studentdetails"]
col=mydb["mystud"]
data=list(col.find()) # fetch data from MongoDB
for rec in data:
     rec.pop('_id',None)
df=pd.DataFrame(data) # convert to Dataframe tabular format using pandas.DataFrame
# Install openpyxl module to run the below function to write into excel file
df.to_excel("E:/My Python programs/Database(MongoDB)/myexport_data.xlsx",index=False)# writes the DataFrame to an Excel file and avoid writing row indices
print("Data exported successfully...")