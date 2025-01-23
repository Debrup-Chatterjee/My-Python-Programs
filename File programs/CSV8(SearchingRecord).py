import csv
ser_field="Marks"
ser_val="99"
with open("E:/My Python programs/File programs/test.csv","r") as file:
     reader=csv.DictReader(file) # USe DictReader to access columns by name
     found=False
     for row in reader:
          if row[ser_field]==ser_val:
               print("Record Found: ",row)
               found=True
               break
     if not found:
          print(f"No record found with {ser_field}={ser_val}")