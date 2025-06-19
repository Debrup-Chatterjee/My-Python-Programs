import pymysql
from tabulate import tabulate
conn=pymysql.connect(
     host="localhost",
     user="root",
     password=""
)
try:
     with conn.cursor() as cursor:
          # Creating the database if does not exists
          cursor.execute("""CREATE DATABASE IF NOT EXISTS seller_db""")
          print("\n******Seller database created successfully******\n")
          conn.commit()
except pymysql.Error as e:
     print("Error: ",e)
finally:
     conn.close()

conn=pymysql.connect(
     host="localhost",
     user="root",
     password="",
     database="seller_db"
)
cursor=conn.cursor()
try:
          # Creating the table if does not exists
          cursor.execute("""CREATE TABLE IF NOT EXISTS seller_details(
               S_id int,S_name varchar(20),Age int,Rating int,PRIMARY KEY(S_id))""")
          print("******Seller details table created successfully******\n")
          conn.commit()

          # Deleting all previous entries from the table
          cursor.execute("DELETE FROM seller_details")
          conn.commit()

          # Inserting records inside the table
          choice="Y"
          print("Enter Seller details...")
          while(choice=="Y"):
               id=input("Enter seller id: ")
               name=input("Enter seller name: ")
               age=input("Enter seller age: ")
               rating=input("Enter seller rating out of 10: ")
               cursor.execute("""INSERT INTO seller_details VALUES(%s,%s,%s,%s)""",(id,name,age,rating))
               choice=input("\nDo you want to enter more sellers(Y/N) ? ").upper()
               if choice=="N":
                    break
          print("\n******Inserted records into the table succesfully******")
          conn.commit()

          # Increasing rating of all sellers by 2
          cursor.execute("""UPDATE seller_details SET Rating=Rating+2""")
          conn.commit()
          print("\n******Increased all seller ratings by 2 successfully******\n")

          # Showing details of sellers whose age is greater than 40
          print("******Sellers who are older than 40: ******")
          cursor.execute("""SELECT * FROM seller_details WHERE Age>40""")
          result=cursor.fetchall()
          if result:
               headers=[desc[0] for desc in cursor.description]
               print(tabulate(result,headers=headers,tablefmt="grid"))
          else:
               print("No sellers present who are older than 40...\n")

          # Displaying details of all users
          print("\n******Details of all sellers are: ******")
          cursor.execute("""SELECT * FROM seller_details""")
          result=cursor.fetchall()
          headers=[desc[0] for desc in cursor.description]
          print(tabulate(result,headers=headers,tablefmt="grid"))

          # Showing details of sellers whose age is greater than 20 and less than 40
          print("\n******Sellers who are older than 20 and less than 40: ******")
          cursor.execute("""SELECT * FROM seller_details WHERE Age>20 AND Age<40""")
          result=cursor.fetchall()
          if result:
               headers=[desc[0] for desc in cursor.description]
               print(tabulate(result,headers=headers,tablefmt="grid"))
          else:
               print("No sellers present whose age are between 20 and 40...\n")
except pymysql.Error as e:
     print("Error: ",e)
finally:
     conn.close()