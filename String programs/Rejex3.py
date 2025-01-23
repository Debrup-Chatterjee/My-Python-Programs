import re
pat=r"\s" # Matches Whitespace
str="hello code hub"
nstr=re.sub(pat,"-",str) #re.sub() replaces all occurences of a pattern with a replacement string
print("Replaced sting: ",nstr)
'''
Regex Sets:
[arn] returns a match where one of the specified characters(a,r, or n) is present
[a-n] returns a match for any lower case character,alphabetically between a and n
[^arn] returns a match for any character except a,r, and n
[0-5][0-9] returns a match for any two-digit numbers from 00 to 59
[a-zA-Z] returns a match for any character alphabetically between a and z,Lower case or Upper case
[+] In sets, +,*,.,|,(),$,{} has no special meaning, so [+] means return a match for any + character in the
string.
'''