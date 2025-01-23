import re
txt="python pound apple orange pond proud"
pat=r"\bp\w*" #starting with p
wrd=re.findall(pat,txt,re.IGNORECASE)
print("Words starting with 'p' are: ",wrd)
patt=r"\w+n\b" #ending with n
wd=re.findall(patt,txt,re.IGNORECASE)
print("Words ending with 'n' are: ",wd)