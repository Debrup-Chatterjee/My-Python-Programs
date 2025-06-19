import pymysql
try:
     conn=pymysql.connect(
          host="localhost",
          user="root",
          password="",
          database="test"
     )
     with conn.cursor() as cursor:
          query="""
          SELECT student_details.St_Name,St_Marks,marks.sub,marks
          FROM student_details
          INNER JOIN marks ON student_details.RegNo=marks.RegNo
          ORDER BY student_details.St_Name ASC
          """ # SQL query to join tables and sort by St_Name
          cursor.execute(query)
          results=cursor.fetchall()
          if results:
               for row in results:
                    print("Name: ",row[0],",Total Marks: ",row[1],",Subject: ",row[2],",Marks: ",row[3])
          else:
               print("No records found.")
except pymysql.Error as err:
     print(f"Error: {err}")
finally:
     if conn:
          conn.close()