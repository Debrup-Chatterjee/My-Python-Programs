#validating a email address
import re
pattern=r"[a-zA-Z0-9._%%]+@[a-zA-Z0-9.-]+\.[a-zA-Z]"
email=input("Enter a Email Address: ")
match=re.match(pattern,email)
if(match):
     print("Email address is valid.")
else:
     print("Email address is invalid.")