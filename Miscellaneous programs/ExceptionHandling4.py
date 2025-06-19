try:
     a=int(input("First Number: "))
     b=int(input("Second Number: "))
     result=a/b
     print("Result= ",result)
except:# this is printed when any error occurs inside the try block
     print("Error Occured")
finally:# this is printed always regardless of whether an error occurs or not
     print("Executed always")