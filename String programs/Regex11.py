import re
str="welcome to, code-hub sodepur! 2025"
string=re.sub(r'[^a-zA-Z0-9]','',str)#replacing all characters except a-z,A-Z and 0-9 with ''
print(string)