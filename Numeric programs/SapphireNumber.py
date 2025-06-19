import math
n=int(input("Enter number: "))
if (int(math.cbrt(n+1)))**3==n+1:
     print("It is a Sapphire number")
else:
     print("It is not a Sapphire number")