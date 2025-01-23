l=[]
n=int(input("Enter how many words you want to enter: "))
for i in range(n):
     x=input()
     l.append(x)
p=[]
s=[]
for v in l:
     if v==v[::-1]:
          p.append(v)
     if v[0]==v[-1] and len(v)!=1:
          s.append(v)
if(len(p)==0):
     print("No Palindrome Words are present...")
else:
     print("The palindrome words in the list are:",str(p).replace("[","").replace("]",""))
if(len(s)==0):
     print("No Special Words are present...")
else:
     print("The special words in the list are:",str(s).replace("[","").replace("]",""))
