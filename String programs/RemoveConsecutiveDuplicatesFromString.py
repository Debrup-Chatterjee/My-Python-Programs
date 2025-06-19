'''Remove the consecutive duplicates from a string.
eg: Input: aaaabbbbcccccdddeeeaa
    Output: abcdea'''
s=input("Enter a string: ")
s2=s[0]
for i in range(1,len(s)):
     if s[i]!=s2[-1]:
          s2=s2+s[i]
print("The string after removing duplicates is ",s2)