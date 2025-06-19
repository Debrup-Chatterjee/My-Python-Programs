'''Instance methods are the methods which act upon the instance variable of the class.Instance methods are
bound to instances(or Objects) and hence are called as: instancename.method().Since instance variables are
available in the instance,instance methods need to know the memory address of the instance.This is provided
through 'self' variable by defualt as first parameter for the instance method.While calling the instance
methods,we need not pass any value to the 'self' variable.
'''
class Student:
     def __init__(self,name,age,student_id,grade): #Constructor to initialize the attributes
          self.name=name # 'self.name' refers to the instance variable 'name'
          self.age=age
          self.student_id=student_id
          self.grade=grade
     
     def display_details(self):
          print(f"Student ID: {self.student_id}") # Accessing the instance variable using 'self'
          print(f"Name : {self.name}")
          print(f"Age : {self.age}")
          print(f"Grade : {self.grade}")

     def update_grade(self,new_grade):
          self.grade=new_grade
          print(f"{self.name}'s grade has been updated to {self.grade}")

student1=Student("Ramani",20,"S11367","B")#Creating
print("Student Details:")
student1.display_details()
print("\nUpdating Grade:")
student1.update_grade("A+") # Updating the grade
print("\nUpdated Student Details:")
student1.display_details()
