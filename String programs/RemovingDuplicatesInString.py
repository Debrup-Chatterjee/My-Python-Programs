s=input("Enter a word: ")
l=sorted(set(s),key=s.index)
print("".join(l))