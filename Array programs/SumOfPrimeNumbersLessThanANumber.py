'''Write a function that takes an integer n and returns the sum of all prime numbers less than n.
Eg: Input: n=10
    Output: 17
The prime numbers less than 10 are 2,3,5 and 7.Their sum is 17. '''
import math
def isPrime(num):
     if num<=1: return False
     c=0
     for i in range(2,int(math.sqrt(num))+1):
          if num%i==0: c+=1
     return True if c==0 else False
n=int(input("Enter a number: "))
l=list(range(2,n))
primes=list(filter(isPrime,l))
if len(primes)==0:
     print("No prime numbers present")
else:
     print("The sum of all prime numbers is ",sum(primes))