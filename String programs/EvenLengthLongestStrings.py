sentence=(input("Enter a sentence: ")).strip()
words=list(set(filter(lambda x:len(x)%2==0,sentence.split()))) #list of words with even length
if len(words)==0:
     exit("No even length words present in the sentence.")
maxLen=len(max(words,key=len))# finding the max even length
maxLenWords=list(filter(lambda x: len(x)==maxLen,words)) # list of all words with the highest even length
print("The words with the max even length are: ",maxLenWords)