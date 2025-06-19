import pymysql
from tabulate import tabulate
conn=pymysql.connect(
     host="localhost",
     user="root",
     password="",
     database="test"
)
try:
     with conn.cursor() as cursor:
          # Finding students who have got the highest total marks(St_Marks)
          cursor.execute("""
               select student_details.RegNo,St_Name,St_Marks
               from student_details
               where student_details.St_Marks=(select max(St_Marks) from student_details)
               """)
          result=cursor.fetchall()
          headers=[desc[0] for desc in cursor.description]
          if result:
               print("People with highest marks: ")
               print(tabulate(result,headers=headers,tablefmt="grid"))

          # Finding students who have got the lowest total marks
          cursor.execute("""
               select student_details.RegNo,St_Name,St_Marks
               from student_details
               where student_details.St_Marks=(select min(St_Marks) from student_details)
               """)
          result=cursor.fetchall()
          headers=[desc[0] for desc in cursor.description]
          if result:
               print("\nPeople with lowest marks: ")
               print(tabulate(result,headers=headers,tablefmt="grid"))
except pymysql.Error as e:
     print("Error: ",e)
finally:
     conn.close()