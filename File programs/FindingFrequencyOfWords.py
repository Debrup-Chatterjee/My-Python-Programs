from collections import Counter
fo=open("E:/My Python programs/File programs/output.txt","r")
s=str(Counter(((fo.read()).lower()).split()))
s=s.replace("Counter({","").replace("})","").replace(",","\n")
print("Frequency of each word in the file are:\n",s)
fo.close()