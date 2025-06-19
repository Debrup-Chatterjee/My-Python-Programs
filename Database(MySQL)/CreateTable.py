import pymysql
#Open database connection
db=pymysql.connect(host="localhost",user="Debrup",password="Debrup@31",database="sample")
#prepare a cursor object using cursor() method
cursor=db.cursor()
#Create table as per requirement
sql="""create table dept(deptno int,dept_name char(20),location char(25))"""
cursor.execute(sql)
db.commit()
#disconnect from server
db.close()
