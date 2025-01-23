import re
txt="Hello code    hub sodepur"
pat=r"\s+" # Split word based on whitespace
wrd=re.split(pat,txt)# re.split() splits a string into a list using the pattern as a delimiter and returns
# a list of strings
for w in wrd:
     print(w)
print("Words: ",wrd)
