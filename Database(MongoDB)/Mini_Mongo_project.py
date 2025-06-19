from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/")
db=client["college"]
students=db["students"]

def add_stud():
     name=input("Enter name: ")
     age=int(input("Enter age: "))
     marks=float(input("Enter marks: "))
     student={"name":name,"age":age,"marks":marks}
     students.insert_one(student)
     print("Student added successfully.\n")

def view_studrecd():
     print("\n Student Records.......")
     for student in students.find():
          print(f"ID: {student['_id']}, Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}")
     print()

def update_stud():
     name=input("Enter the name of the student to update: ")
     student=students.find_one({"name":name})
     if student:
          new_marks=float(input("Eter new marks: "))
          students.update_one({"name":name}, {"$set": {"marks":new_marks}})
          print("student marks updated.\n")
     else:
          print("Student not found.\n")

def delete_stud():
     name=input("Enter the name of the student to delete: ")
     result=students.delete_one({"name":name})
     if result.deleted_count:
          print("Student deleted successfully.\n")
     else:
          print("Student not found.\n")

while True:
     print("1. Add Student")
     print("2. View Students")
     print("3. Update Student Marks")
     print("4. Delete Student")
     print("5. Exit")
     choice=input("Enter your choice: ")

     if choice=="1":
          add_stud()
     elif choice=="2":
          view_studrecd()
     elif choice=="3":
          update_stud()
     elif choice=="4":
          delete_stud()
     elif choice=="5":
          print("Exiting...")
          break
     else:
          print("Invalid choice. Try again. \n")