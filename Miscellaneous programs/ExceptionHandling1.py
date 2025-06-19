try:
     a=int(input("First Number: "))
     b=int(input("Second Number: "))
     result=a/b
     print("Result= ",result)
except ZeroDivisionError: # printed when ZeroDivisionError occurs in the try block
     print("Division by Zero error")
else:
     print("Successful Division")# printed when ZeroDivisionError does not occur in the try block
