import re
str=input("Enter a sentence: ")
res=re.split(r'\s+',str)
print("All words in the sentence are: \n",res)
wrd=max(res,key=len)
ln=len(wrd)
print(f"The longest word is '{wrd}' with length {ln}")