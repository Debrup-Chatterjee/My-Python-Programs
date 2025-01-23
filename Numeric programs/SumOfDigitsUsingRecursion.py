def SumOfDigits(num):
     if(num==0):
          return 0
     else:
          return (num%10)+SumOfDigits(num//10)
n=int(input("Enter a number: "))
print("Sum of the digits is ",SumOfDigits(n))