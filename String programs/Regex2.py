import re
pat=r"\d+" # digits matches one or more
str="There are 256 Java programs and 412 Python programs."
mat=re.findall(pat,str)# findall() finds and returns all the occurences of the pattern in the string as a 
# list
print("All matches: ",mat)
'''
Regex Metacharacters:
"[]" for A set of characters
"\" Signals a special sequence(can also be used to escape special characters)
"." for any character except newline
"^" for Start of string
"$" for End of string
"+" for One or more times
"*" for Zero or more times
"?" for Zero or one time
"{n}" for exactly n time
"{n,m}" for Between n and m times
"|" for Either Or
"()" for Capture and group
'''