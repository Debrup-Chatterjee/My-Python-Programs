def BinToDec(n,c):
     if n==0:
          return 0
     else:
          return (2**c)*(n%10)+BinToDec(n//10,c+1)
def DecToBin(n):
     if(n==0):
          return 0
     else:
          return DecToBin(n//2)*10+(n%2)
print("Choice 1: Decimal to Binary Conversion")
print("Choice 2: Binary to Decimal Conversion")
print("Enter any other Choice to quit the program...")
c=int(input("Enter your choice: 1 or 2 ? "))
if(c==1):
     n=int(input("Enter a Decimal Number: "))
     print("The Binary Equivalent is: ",DecToBin(n))
elif(c==2):
     n=int(input("Enter a Binary Number: "))
     print("The Decimal Equivalent is: ",BinToDec(n,0))