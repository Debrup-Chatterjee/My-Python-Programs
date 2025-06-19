try:
     a=int(input("First Number: "))
     b=int(input("Second Number: "))
     result=a/b
     l=sum(result) #raises TypeError as we are applying sum() function to a non iterable
     print("Result= ",result)
except(ZeroDivisionError,TypeError) as e: # this catches only ZeroDivisionError and TypeError
     print(f"An error occurred: {e}")
else:
     print("Successful Division")