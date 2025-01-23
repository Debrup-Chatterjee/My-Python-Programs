import csv
head=["Name","Area","CountryCode"]
dt=[["India","91","IN"],["Japan","90","JP"]]
with open("E:/My Python programs/File programs/country.csv","w") as f:
     csvwriter=csv.writer(f)#Creating writer object of csv module to write into csv file
     csvwriter.writerow(head)#write a single row into csv file
     csvwriter.writerows(dt)#write all rows into csv file
print("Written into csv file Successfully")