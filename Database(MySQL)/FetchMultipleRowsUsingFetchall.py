import pymysql
# Open database connection
db=pymysql.connect(host="localhost",user="root",password="",database="sample")
# Prepare a cursor object using cursor() method
cursor=db.cursor()
# Prepare sql query
sql="SELECT LOCATION FROM DEPT"
cursor.execute(sql)
# Fetches all the records
rows=cursor.fetchall()
for row in rows:
     print("Location: ",row[0])
#disconnect from server
db.close()