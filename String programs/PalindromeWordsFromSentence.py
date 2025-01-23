s=input("Enter a sentence: ")
l=[w for w in s.split() if w==w[::-1]]
if(len(l)==0):
     print("No Palindrome words found !")
else:
     print("Palindrome words in the sentence are:\n",str(l).replace("[","").replace("]","").
          replace(",","\n").replace("'",""))