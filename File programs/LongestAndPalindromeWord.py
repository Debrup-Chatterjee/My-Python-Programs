from functools import reduce
fo=open("E:/My Python programs/File programs/output.txt","r")
l=(fo.read()).split()
print("The longest word is: ",reduce(lambda x,y:x if len(x)>len(y) else y, l))

print("The palindrome words in the file are :")
p=list(filter(lambda x:(x==x[::-1]),l))
if(len(p)==0):
     print("No Palindrome words found!")
else:
     print("\n".join(p))
fo.close()