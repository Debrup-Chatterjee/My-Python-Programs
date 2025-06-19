import pymysql
db=pymysql.connect(host="localhost",user="root",password="",database="sample")
cursor=db.cursor()
cursor.execute("SELECT * FROM DEPT") # * denotes all fields from the table
for i in range(cursor.rowcount):
     row=cursor.fetchone()
     if row: 
          print(row)
db.close()