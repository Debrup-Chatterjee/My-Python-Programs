import re
pat=r"hello"
str="hello code Hub Sodepur"
match=re.match(pat,str)#re.match() matches only the beginning of the string and returns a re.Match object
if match:
     print("Match Found: ",match.group()) #re.MatchObject.group() returns the complete matched 
     #subgroup by default or a tuple of matched subgroups depending on the number of arguments
else:
     print("No Match")
'''
Regex Special sequences:
"\d" for Digit(0-9)
"\D" for Non-digit
"\w" for Word character(letters,digits,...)
"\W" for Non-word character
"\s" for Whitespace(space,tab,newline)
"\S" for Non-whitespace
"\A" returns a match if the specified characters are at the beginning of the string
"\B" returns a match where the specified characters are present,but NOT at the BEGINNING or END
"\Z" returns a match if the specified characters are at the end of the string
"\b" asserts a word boundary,which means it matches positions where one side matches the pattern and the 
other side does not match  the pattern,can be used at BEGINNING and END of string to match a pattern
'''
