import pymysql
#Open database connection
db=pymysql.connect(host="localhost",user="root",password="",database="sample")
#prepare a cursor object using cursor() method
cursor=db.cursor()
#prepare SQL query to delete records from a table
sql="delete from dept where location='Delhi'"
cursor.execute(sql)
db.commit()
#disconnect from server
db.close()