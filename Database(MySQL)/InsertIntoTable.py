import pymysql
#Open database connection
db=pymysql.connect(host="localhost",user="root",password="",database="sample")
#prepare a cursor object using cursor() method
cursor=db.cursor()
#prepare SQL query to INSERT a record into the tabl
sql="INSERT INTO DEPT(DEPTNO,DEPT_NAME,LOCATION) VALUES(10,'SALES','CHENNAI')"
cursor.execute(sql)
db.commit()
#disconnect from server
db.close()