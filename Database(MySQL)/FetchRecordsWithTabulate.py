import pymysql
from tabulate import tabulate
conn=pymysql.connect(
     host="localhost",
     user="root",
     password="",
     database="test"
)
print("Successfully connected",conn)
try:
     with conn.cursor() as cursor:
          cursor.execute("""
               SELECT student_details.St_Name,St_Marks,marks.*
               FROM student_details
               INNER JOIN marks on student_details.RegNo=marks.RegNo""")
          result=cursor.fetchall()
          headers=[desc[0] for desc in cursor.description]# extracts the column names from the description and stores them in the headers list
          print(tabulate(result,headers=headers,tablefmt="grid"))
except pymysql.Error as e:
     print("Error: ",e)
finally:
     conn.close()