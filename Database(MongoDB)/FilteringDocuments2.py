from pymongo import MongoClient
client=MongoClient("localhost",27017)
db=client["studentdetails"]
col=db["mystud"]
s20=s21=0

for sal in col.find({'age':21}):
     s21+=sal["marks"]
for sal in col.find({'age':20}):
     s20+=sal["marks"]

print("Total sum marks of students aged 20: ",s20)
print("Total sum marks of students aged 21: ",s21)