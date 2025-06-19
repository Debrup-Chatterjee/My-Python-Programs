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
          cursor.execute("""
               select student_details.St_Name,St_Marks,marks.*
               from student_details
               inner join marks on student_details.RegNo=marks.RegNo
               where student_details.St_marks>90 
               order by student_details.St_marks desc
               .
               """)
          result=cursor.fetchall()
          headers=[desc[0] for desc in cursor.description]
          print(tabulate(result,headers=headers,tablefmt="grid"))
except pymysql.Error as e:
     print("Error: ",e)
finally:
     conn.close()