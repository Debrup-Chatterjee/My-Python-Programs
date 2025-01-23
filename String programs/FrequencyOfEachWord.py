from collections import Counter
s=input("Enter a sentence: ")
l=Counter(s.split())
print("Frequency of each word is:\n",str(l).replace("Counter({","").replace("})","").replace(",","\n"))