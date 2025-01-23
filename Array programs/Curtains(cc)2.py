import textwrap
s=input("Enter the curtain colors consisting of only 'a'(aqua) or 'b'(black):")
N=len(s)
L=int(input("Enter the number of curtains in each box: "))
if(N<1 or N>50 or L<1 or L>10):
     print("Wrong Input!")
     exit()
a=[]
b=[]
a=textwrap.wrap(s,L)
b=[i.count('a') for i in a]
print("The maximum number of aqua curtains in a box is ",max(b))
