s=input("Enter a sentence: ")
l=sorted(s.split(),key=len)
print("Words sorted according to length:\n"," ".join(l))
print("Word with the highest length: ",l[-1])