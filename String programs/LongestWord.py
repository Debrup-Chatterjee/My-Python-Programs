s=input("Enter a sentence: ")
l=sorted(s.split(),key=len)
print("The word with the highest length is: ",l[-1])