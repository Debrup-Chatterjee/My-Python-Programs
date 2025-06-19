import pymysql
db=pymysql.connect(host="localhost",user="root",password="",database="sample")
cursor=db.cursor()
flag='y'
print("Enter department details into the table: ")
while(flag=='y'):
     deptno=int(input("Enter department number: "))
     deptname=input("Enter department name: ")
     location=input("Enter department location: ")
     sql='INSERT INTO DEPT(DEPTNO,DEPT_NAME,LOCATION) VALUES(%s,%s,%s)'
     values=(deptno,deptname,location)
     cursor.execute(sql,values)
     db.commit()
     flag=input("Do you want to keep entering? (Y/N): ").lower()
print("All values are entered into the table successfully...")
db.close()