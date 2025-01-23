import re
pat=r"hub"
str="Hello Code Hub Sodepur Hub"
mat=re.search(pat,str,re.IGNORECASE) #re.search() searches the entire string for a match of the pattern and
# returns only first match found as a re.Match object. re.IGNORECASE ignores the case while searching the
# string.
if mat:
     print("Ignore case match found: ",mat.group())