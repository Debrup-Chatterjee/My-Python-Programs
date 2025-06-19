import re
pat=r"(\w+) (\w+) (\w+)" # Group match
str="code hub sodepur"
mat= re.search(pat,str)
if mat:
     print("Full match: ",mat.group())
     print("First group: ",mat.group(1))
     print("Second group: ",mat.group(2))
     print("Third group: ",mat.group(3))