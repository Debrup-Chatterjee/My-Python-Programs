import pymysql
con=pymysql.connect(host="localhost",user="root",password="",database="test")
cursor=con.cursor()
# Here RegNo is the primary key of student_details table and is a foreign key in marks table
update_query="""UPDATE marks 
SET marks=marks-5 
WHERE RegNo IN (SELECT RegNo FROM student_details where St_Marks>100)"""
try:
     cursor.execute(update_query)
     con.commit()
     print(f"{cursor.rowcount} rows were updated.")
except pymysql.MySQLError as err:
     print(f"Error: {err}")
     con.rollback() # rollback() does the opposite of commit(),i.e., it undos the last changes commited
cursor.close()
con.close()