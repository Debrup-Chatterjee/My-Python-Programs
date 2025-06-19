import pymysql
#Open database connection
db=pymysql.connect(host="localhost",user="Debrup",password="Debrup@31",database="sample")
#Prepare a cursor object using cursor() method
cursor=db.cursor()
#Prepare SQL query to UPDATE records into a table
sql="""update dept set location='Delhi' where dept_name='SALES'"""
cursor.execute(sql)
db.commit()
#disconnect from server
db.close()