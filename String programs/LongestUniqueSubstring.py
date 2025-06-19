s=input("Enter a string: ")
s2=""
m=""
if len(s)==1:
     exit("The longest unique substring is the string itself...")
for i in s:
     if i not in s2:
          s2+=i
     else:
          if(len(s2)>len(m)):
               m=s2
          s2=s2[s2.index(i)+1:]+i
if(s2==s or len(s2)>len(m)):
     m=s2
print("The longest unique substring is: ",m)