import re
txt="Hello reckon n session in hi man"

pat=r"\w*n\b" # Matches all words ending with 'n' which have some or even no word characters before the 'n' 
# ,i.e., even a single 'n' appearing in the sentence will be counted in this.
mat=re.findall(pat,txt)
print(r"\w*n\b = ",mat)

pat2=r"\w+n\b" # Matches all words ending with 'n' which have one or more word characters before the 'n'
# i.e., single 'n' will not be counted in this.
mat=re.findall(pat2,txt)
print(r"\w+n\b = ",mat)

pat3=r"\wn\b" # Matches all parts of the string ending with 'n' which have a single word character 
# before the 'n'.
mat=re.findall(pat3,txt)
print(r"\wn\b = ",mat)