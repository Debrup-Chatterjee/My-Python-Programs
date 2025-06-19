import pymysql
#Open database connection
db=pymysql.connect(host="localhost",user="root",password="",database="sample")
#prepare a cursor object using cursor() method
cursor=db.cursor()
#execute SQL query using execute() method
cursor.execute("select version()")
#Fetch a single row using fetchone() method
data=cursor.fetchone()
print("Database version: ",data)
#disconnect from server
db.close()
