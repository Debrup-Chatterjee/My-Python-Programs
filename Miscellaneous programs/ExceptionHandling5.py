a=int(input("Enter the parameter value: "))
try:
     if a<0:
          raise ValueError("Not a Positive Integer")
except ValueError as err:
     print(err)
else:
     print("Positive Integer= ",a)