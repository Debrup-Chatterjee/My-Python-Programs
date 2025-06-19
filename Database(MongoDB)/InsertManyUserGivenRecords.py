from pymongo import MongoClient
con=MongoClient('mongodb://localhost:27017/')
mydb=con["studentdetails"]
mycoll=mydb["mystud"]
def InsertRec():
     while True:
          name=input("Enter student name: ")
          age=int(input("Enter student age: "))
          city=input("Enter student city: ")
          stud_data={"name":name,"age":age,"city":city}
          mycoll.insert_one(stud_data)
          print("Student data inserted successfully!")
          ch=input("Do you want to add another student? (yes/no): ").lower()
          if ch!="yes":
               break
InsertRec()
print(f"Data successfully added to the collection '{mycoll.name}' !")