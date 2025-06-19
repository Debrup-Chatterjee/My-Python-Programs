num=int(input("Enter a number: "))
n=num
l=[]
while n!=0:
     l.insert(0,n%10)
     n//=10
while True:
     if sum(l)<num:
          l.append(sum(l))
          l.pop(0)
     elif sum(l)==num:
          exit("It is a Keith number.")
     else:
          exit("It is not a Keith number.")





