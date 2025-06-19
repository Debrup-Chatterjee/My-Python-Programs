import pymysql
from tabulate import tabulate
conn=pymysql.connect(
     host="localhost",
     user="root",
     password="",
     database="test"
)
cursor=conn.cursor()
query="""
SELECT student_details.RegNo,student_details.St_Name,student_details.St_Marks,marks.sub,marks.marks
FROM student_details
JOIN marks ON student_details.RegNo=marks.RegNo
WHERE student_details.St_Name LIKE %s
"""
cursor.execute(query,('%'+'R'+'%'))
# here % means one or more characters,so this query searches for any name which has 'R'(can be upper case or lowercase) in it
results=cursor.fetchall()
headers=[desc[0] for desc in cursor.description]
print(tabulate(results,headers=headers,tablefmt="grid"))
cursor.close()
conn.close()