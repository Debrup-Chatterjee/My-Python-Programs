def perfect(num,f):
     if f==1:
          return 1
     elif num%f==0 and f>1:
          return f+perfect(num,f-1)
     elif num%f!=0 and f>1:
          return perfect(num,f-1)
n=int(input("Enter a number: "))
if(n==perfect(n,n-1)):
     print("It is a Perfect Number")
else:
     print("It is not a Perfect Number")