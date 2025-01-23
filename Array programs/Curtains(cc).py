a=[]
s=input("Enter the curtain colors consisting of only 'a'(aqua) or 'b'(black):")
N=len(s)
L=int(input("Enter the number of curtains in each box: "))
if(N<1 or N>50 or L<1 or L>10):
     print("Wrong Input!")
     exit()
max=0
for i in range(0,N):
     if(i%L==0):
          if(a.count('a')>max):
               max=a.count('a')
          a.clear()
     a.append(s[i])
if(a.count('a')>max):
    max=a.count('a')
print("The maximum number of aqua curtains in a box is ",max)
