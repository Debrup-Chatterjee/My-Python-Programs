import pymysql as mysql
import csv
conn=mysql.connect(host="localhost",user="root",password="",database="test")
cursor=conn.cursor()
def display_stud(): # display all student records
     print("\nAll Student Records: ")
     cursor.execute("SELECT * FROM student_details")
     for row in cursor.fetchall():
          print(row)

def count_stud(): # count total number of students
     cursor.execute("SELECT COUNT(*) FROM student_details")
     print("\nTotal Students: ",cursor.fetchone()[0])

def display_sortedrec(): # display students sorted by Reg No
     cursor.execute("SELECT * FROM student_details ORDER BY RegNo DESC")
     print("\nStudents sorted by Reg No (high to low): ")
     for row in cursor.fetchall():
          print(row)

def export_to_csv(myfile): # export data from database into a csv file
     cursor.execute("SELECT * FROM student_details")
     records=cursor.fetchall()
     with open(myfile,mode='w',newline='') as file:
          writer=csv.writer(file)
          writer.writerow(['Reg No','Student Name','Roll No'])
          writer.writerows(records)
     print(f"\nData exported successfully to {myfile}")
     
display_stud()
count_stud()
display_sortedrec()
export_to_csv('E:/My Python programs/Database(MySQL)/student_data.csv')
cursor.close()