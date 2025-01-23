def Palindrome(num,sum):
     if num>0:
          sum=sum*10+num%10
          return Palindrome(num//10,sum)
     else:
          return sum
n=int(input("Enter a number: "))
if n==Palindrome(n,0):
     print("It is a Palindrome Number")
else:
     print("It is not a Palindrome Number")