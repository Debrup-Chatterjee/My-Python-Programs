s=input("Enter a sentence: ")
l=[w for w in s.split() if('a' in w.lower() and 'e' in w.lower() and 'i' in w.lower() and 'o' in w.lower()
                            and 'u' in w.lower())]
if(len(l)==0):
     print("No such words found")
else:
     print("Words which have all the vowels are: ",l)