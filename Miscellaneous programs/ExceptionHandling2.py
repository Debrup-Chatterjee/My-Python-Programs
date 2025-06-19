try:
     a=int(input("First Number: "))
     b=int(input("Second Number: "))
     result=a/b
     print("Result= ",result)
except: # this catches for all errors
     print("Error Occured")
else:
     print("Successful Division")