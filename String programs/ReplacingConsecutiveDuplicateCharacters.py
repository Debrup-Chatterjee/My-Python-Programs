'''Compress a string by replacing consecutive duplicate characters with {char}{count}.
eg: Input: "aabcccaaa" 
    Output: "a2b1c3a3" '''
s=input("Enter a string: ")
s2=""
ch=s[0]
c=1
for i in range(1,len(s)):
     if s[i]==ch:
          c+=1
     else:
          s2=s2+ch+str(c)
          ch=s[i]
          c=1
s2=s2+ch+str(c)
print("Compressed string is: ",s2)
